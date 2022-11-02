// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract FirstNFT is ERC721URIStorage, Ownable {
	using Counters for Counters.Counter; //used to keep track of tokenId and increment them
	Counters.Counter private _tokenIds;

	constructor() ERC721("FirstNFT", "NFT") {}

	// atm can't pass tokenUri from anywhere. Maybe should be a separe function?
	function mint(string memory tokenURI) public returns (uint256) {
		_tokenIds.increment();
		uint256 newItemId = _tokenIds.current();
		_safeMint(msg.sender, newItemId);
		_setTokenURI(newItemId, tokenURI);
		return newItemId;
	}
}