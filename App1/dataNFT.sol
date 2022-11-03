// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract DataNFT is ERC721, Ownable {

	constructor() ERC721("DataNFT", "DATANFT"){}

	event DataItemAdded(uint256 itemId, string ipfsHash, string ipfsUrl);

	struct DataItem {
		string ipfsHash;
		string ipfsUrl;
	}

	DataItem[] public dataItems;
	
	mapping(uint256 => address) public dataItemToOwner;

	function _saveDataItem(string memory _ipfsHash, string memory _ipfsUrl) private {
		dataItems.push(DataItem(_ipfsHash, _ipfsUrl));
		uint _id = dataItems.length - 1;
		dataItemToOwner[_id] = msg.sender;
		emit DataItemAdded(_id, _ipfsHash, _ipfsUrl);

	}

	function addDataItem(string memory _ipfsHash, string memory _ipfsUrl) public returns (string memory) {
		require(bytes(_ipfsHash).length > 0, "missing IPFS hash for the data item");
		require(bytes(_ipfsUrl).length > 0, "missing IPFS url for the data item");
		_saveDataItem(_ipfsHash, _ipfsUrl);
		return "Data item saved";
	}


}