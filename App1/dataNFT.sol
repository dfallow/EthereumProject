// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract dataNFT is ERC721, Ownable {

	constructor() ERC721("DataNFT", "DATANFT"){}

	mapping(address => DataItem[]) public dataItems;
	
	struct DataItem {
		string ipfsHash;
		string ipfsUrl;
	}

	event dataItemAdded(address user, string ipfsHash, string ipfsUrl);

	function getDataItems() public view returns (DataItem [] memory) {
		return dataItems[msg.sender];
	}

	function addDataItem(string memory _ipfsHash, string memory _ipfsUrl) public {
		require(bytes(_ipfsHash).length > 0, "missing IPFS hash for the data item");
		require(bytes(_ipfsUrl).length > 0, "missing IPFS url for the data item");

		dataItems[msg.sender].push(DataItem(_ipfsHash, _ipfsUrl));
		emit dataItemAdded(msg.sender, _ipfsHash, _ipfsUrl);
	}
}