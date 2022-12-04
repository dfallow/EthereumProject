// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MachineToken is ERC721, Ownable, ERC721URIStorage {
    uint256 public numberOfTokens;

    event Minted(address indexed minter, uint256 tokenId, string tokenURI);
    event TokenOwnershipTransfered(address from, address to, uint256 tokenId);
    event ContractOwnershipTransfered(bool success);

    constructor() payable ERC721("MachineToken", "MTK") {
        _transferOwnership(msg.sender);
    }

    function mint(string memory ipfsURL) public onlyOwner returns (uint256) {
        numberOfTokens++;
        uint256 tokenId = numberOfTokens;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, ipfsURL);
        emit Minted(msg.sender, tokenId, ipfsURL);
        return tokenId;
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        address _tokenOwner = ownerOf(tokenId);
        require(
            msg.sender == _tokenOwner,
            "Only the owner of machine token can view tokenURI"
        );
        require(_exists(tokenId), "URI query for nonexistent token");
        return super.tokenURI(tokenId);
    }

    // transfer token ownership
    function transferTokenOwnership(address _to, uint256 _tokenId)
        public
        onlyOwner
    {
        safeTransferFrom(msg.sender, _to, _tokenId);
        emit TokenOwnershipTransfered(msg.sender, _to, _tokenId);
    }

    function getTokenOwner(uint256 tokenId) public view returns (address) {
        address _tokenOwner = ownerOf(tokenId);
        return _tokenOwner;
    }

    // transfer contract ownership
    function transferOwnership(address newOwner)
        public
        override(Ownable)
        onlyOwner
    {
        _transferOwnership(newOwner);
        emit ContractOwnershipTransfered(true);
    }

    // Override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }
}
