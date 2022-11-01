// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/access/Ownable.sol';
import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract FirstNFT is ERC721, Ownable {
	uint256 counter;
	string private _baseURIextended;
	mapping (uint256 => string) private _tokenURIs;

	constructor() ERC721('FirstNFT', 'FIRSTNFT') {}

	function mint() public {
		uint256 tokenId = counter;
		_safeMint(msg.sender, tokenId);
		counter++;
	}

	function setBaseURI() external onlyOwner() {
		_baseURIextended = "ipfs://QmUqwqpXZXWJHW1bvHVUVpygEzFesUp2qxtryVve8Awwnc";
	}

	function _baseURI() internal view virtual override returns (string memory) {
		return _baseURIextended;
	}

}