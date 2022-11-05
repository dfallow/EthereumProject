// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import '@openzeppelin/contracts/token/ERC721/ERC721.sol';
import '@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol';
import '@openzeppelin/contracts/access/Ownable.sol';

contract DataNFT is ERC721, Ownable {
    uint256 public mintPrice = 0.05 ether;
    uint256 public totalSupply;
    uint256 public maxSupply;
    bool public isMintEnabled; //Defaults to false if not defined
    mapping(address => uint256) public mintedWallets;
    mapping(uint256 => string) public tokenIdToURI;

    constructor() payable ERC721('Data NFT', 'DataNFT') {
        maxSupply = 10;
    }

    function toggleIsMintEnabled() external onlyOwner {
        isMintEnabled = !isMintEnabled;
    }

    function setMaxSupply(uint256 maxSupply_) external onlyOwner {
        maxSupply = maxSupply_;
    }

    function mint() external payable {
        require(isMintEnabled, 'minting not enabled');
        require(mintedWallets[msg.sender] < 1, 'exceeds max per wallet');
        require(msg.value == mintPrice, 'wrong value');
        require(maxSupply > totalSupply, 'sold out');

        mintedWallets[msg.sender]++;
        totalSupply++;
        uint256 tokenId = totalSupply;
        _safeMint(msg.sender, tokenId);
    }

    event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);
    event Minted(address indexed minter, uint256 nftId);

    struct DataItem {
        string ipfsHash;
        string ipfsUrl;
    }

    DataItem[] public dataItems;

    function _saveDataItem(string memory _ipfsHash, string memory _ipfsUrl)
        private
        onlyOwner
        returns (DataItem[] memory)
    {
        dataItems.push(DataItem(_ipfsHash, _ipfsUrl));
        emit DataItemAdded(dataItems.length, _ipfsHash, _ipfsUrl);
        return dataItems;
    }

    function addDataItem(string memory _ipfsHash, string memory _ipfsUrl)
        public
        returns (string memory)
    {
        require(
            bytes(_ipfsHash).length > 0,
            "missing IPFS hash for the data item"
        );
        require(
            bytes(_ipfsUrl).length > 0,
            "missing IPFS url for the data item"
        );
        _saveDataItem(_ipfsHash, _ipfsUrl);
        return "Data item saved";
    }

}