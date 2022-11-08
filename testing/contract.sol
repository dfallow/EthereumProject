// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DataNFT is ERC721, Ownable {
    uint256 public totalSupply;
    address private _owner;
    //mapping(uint256 => string) public tokenIdToURI;

    struct DataItem {
        string ipfsHash;
        string ipfsUrl;
    }

    DataItem[] public dataItems;

    event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);
    event Minted(address indexed minter, uint256 nftId);

    constructor(string memory ipfsHash, string memory ipfsUrl)
        payable
        ERC721("Data NFT", "DataNFT")
    {
        _transferOwnership(msg.sender);
        _saveDataItem(ipfsHash, ipfsUrl);
        _mint();
    }

    function _mint() private onlyOwner returns (uint256) {
        totalSupply++;
        uint256 tokenId = totalSupply;
        _safeMint(msg.sender, tokenId);
        emit Minted(msg.sender, tokenId);
        return tokenId;
    }

    function _saveDataItem(string memory _ipfsHash, string memory _ipfsUrl)
        private
        onlyOwner
        returns (DataItem[] memory)
    {
        require(
            bytes(_ipfsHash).length > 0,
            "missing IPFS hash for the data item"
        );
        require(
            bytes(_ipfsUrl).length > 0,
            "missing IPFS url for the data item"
        );
        dataItems.push(DataItem(_ipfsHash, _ipfsUrl));
        emit DataItemAdded(dataItems.length, _ipfsHash, _ipfsUrl);
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
