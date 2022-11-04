// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract DataNFT is ERC721 {
    uint256 private _tokenCounter;

    constructor() ERC721("DataNFT", "DATANFT") {
        _tokenCounter = 0;
    }

    event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);
    event Minted(address indexed minter, uint256 nftId);

    struct DataItem {
        string ipfsHash;
        string ipfsUrl;
    }

    DataItem[] public dataItems;

    mapping(uint256 => address) public dataItemToOwner;
    mapping(uint256 => string) public tokenIdToURI;

    function _saveDataItem(string memory _ipfsHash, string memory _ipfsUrl)
        private
        returns (DataItem[] memory)
    {
        dataItems.push(DataItem(_ipfsHash, _ipfsUrl));
        uint256 _id = dataItems.length - 1;
        dataItemToOwner[_id] = msg.sender;
        emit DataItemAdded(_id, _ipfsHash, _ipfsUrl);
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

    function mint() public returns (uint256) {
        uint256 _id = _tokenCounter;
        _safeMint(msg.sender, _id);
        _tokenCounter = _tokenCounter + 1;
        return _tokenCounter;
    }
}
