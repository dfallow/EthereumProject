// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NewDataNFT is ERC721, Ownable {
    uint256 public totalSupply;
    address private _owner;

    struct DataItem {
        string ipfsHash;
        string ipfsUrl;
    }

    DataItem[] public dataItems;

    event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);
    event Minted(address indexed minter, uint256 nftId);

    constructor() payable ERC721("Data NFT", "DataNFT") {
        _transferOwnership(msg.sender);
    }

    function _mint() private onlyOwner returns (uint256) {
        totalSupply++;
        uint256 tokenId = totalSupply;
        _safeMint(msg.sender, tokenId);
        emit Minted(msg.sender, tokenId);
        return tokenId;
    }

    function saveDataItem(string memory ipfsHash, string memory ipfsUrl)
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
        _mint();
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
