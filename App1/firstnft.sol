// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/access/Ownable.sol';
import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract FirstNFT is ERC721, Ownable {
	uint256 counter;

	constructor() ERC721('FirstNFT', 'FIRSTNFT') {}

	function mint() public {
		uint256 tokenId = counter;
		_safeMint(msg.sender, tokenId);
		counter++;
	}
}