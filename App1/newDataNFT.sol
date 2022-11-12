// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NewDataNFT is ERC721, Ownable, ERC721URIStorage {
    uint256 public totalSupply;
    address private _owner;

    mapping(uint256 => string) public tokenIdToURI;

    struct DataItem {
        string ipfsHash;
        string ipfsUrl;
    }

    DataItem[] public dataItems;

    event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);
    event Minted(address indexed minter, uint256 nftId, string tokenURI);

    constructor() payable ERC721("Data NFT", "DataNFT") {
        _transferOwnership(msg.sender);
    }

    function mint(string memory tokenURI) public onlyOwner returns (uint256) {
        totalSupply++;
        uint256 tokenId = totalSupply;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        tokenIdToURI[tokenId] = tokenURI;
        emit Minted(msg.sender, tokenId, tokenURI);
        return tokenId;
    }

    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        string memory _tokenURI = tokenIdToURI[tokenId];
        return _tokenURI;
    }

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    function saveData(string memory ipfsHash, string memory ipfsUrl)
        public
        onlyOwner
        returns (DataItem[] memory)
    {
        require(
            bytes(ipfsHash).length > 0,
            "missing IPFS hash for the data item"
        );
        require(
            bytes(ipfsUrl).length > 0,
            "missing IPFS url for the data item"
        );
        dataItems.push(DataItem(ipfsHash, ipfsUrl));
        emit DataItemAdded(dataItems.length, ipfsHash, ipfsUrl);
        return dataItems;
    }

    function changeOwnerOfToken(address _to, uint256 _tokenId)
        public
        onlyOwner
    {
        _owner = owner();
        _transfer(_owner, _to, _tokenId);
    }

    function getOwnerOfToken(uint256 tokenId) public view returns (address) {
        address tokenOwner = ownerOf(tokenId);
        return tokenOwner;
    }
}
