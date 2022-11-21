// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultipleFilesContract is ERC721, Ownable, ERC721URIStorage {
    uint256 public totalSupply;
    address private _owner;

    mapping(uint256 => string) public tokenIdToURI;

    event Minted(address indexed minter, uint256 nftId, string tokenURI);

    constructor() payable ERC721("Data NFT", "DataToken") {
        _transferOwnership(msg.sender);
    }

    function mintDataToken(string memory tokenURI)
        public
        onlyOwner
        returns (uint256)
    {
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

    // change ownership of a single data token
    function changeOwnerOfDataToken(address _to, uint256 _tokenId)
        public
        onlyOwner
    {
        _owner = owner();
        _transfer(_owner, _to, _tokenId);
    }

    // change ownership of all data items that belong to the current owner
    function changeOwnerOfAllDataTokens(address _to) public onlyOwner {
        _owner = owner();

        for (uint256 i = 0; i == totalSupply; i++) {
            _transfer(_owner, _to, i);
        }
    }

    // change ownership of some specified data items passed in an array form to this function
    function changeOwnerOfSomeDataTokens(
        address _to,
        uint256[] memory tokenIdArray
    ) public onlyOwner {
        _owner = owner();

        for (uint256 i = 0; i < tokenIdArray.length; i++) {
            _transfer(_owner, _to, i);
        }
    }

    function getOwnerOfDataToken(uint256 tokenId)
        public
        view
        returns (address)
    {
        address tokenOwner = ownerOf(tokenId);
        return tokenOwner;
    }
}
