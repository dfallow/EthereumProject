import json;

abi = json.loads("""[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "itemId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsUrl",
				"type": "string"
			}
		],
		"name": "DataItemAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ipfsHash",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_ipfsUrl",
				"type": "string"
			}
		],
		"name": "addDataItem",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataItemToOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataItems",
		"outputs": [
			{
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ipfsUrl",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]""")



bytecode = "60806040523480156200001157600080fd5b506040518060400160405280600781526020017f446174614e4654000000000000000000000000000000000000000000000000008152506040518060400160405280600781526020017f444154414e465400000000000000000000000000000000000000000000000000815250816000908051906020019062000096929190620001a6565b508060019080519060200190620000af929190620001a6565b505050620000d2620000c6620000d860201b60201c565b620000e060201b60201c565b620002bb565b600033905090565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b828054620001b49062000256565b90600052602060002090601f016020900481019282620001d8576000855562000224565b82601f10620001f357805160ff191683800117855562000224565b8280016001018555821562000224579182015b828111156200022357825182559160200191906001019062000206565b5b50905062000233919062000237565b5090565b5b808211156200025257600081600090555060010162000238565b5090565b600060028204905060018216806200026f57607f821691505b602082108114156200028657620002856200028c565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b612c3a80620002cb6000396000f3fe608060405234801561001057600080fd5b50600436106101215760003560e01c80638da5cb5b116100ad578063a22cb46511610071578063a22cb4651461031b578063b88d4fde14610337578063c87b56dd14610353578063e985e9c514610383578063f2fde38b146103b357610121565b80638da5cb5b1461026257806395d89b4114610280578063968a76cf1461029e5780639ba41a65146102cf578063a1ab8166146102eb57610121565b806323b872dd116100f457806323b872dd146101c057806342842e0e146101dc5780636352211e146101f857806370a0823114610228578063715018a61461025857610121565b806301ffc9a71461012657806306fdde0314610156578063081812fc14610174578063095ea7b3146101a4575b600080fd5b610140600480360381019061013b9190611d5a565b6103cf565b60405161014d919061217b565b60405180910390f35b61015e6104b1565b60405161016b9190612196565b60405180910390f35b61018e60048036038101906101899190611e2c565b610543565b60405161019b9190612114565b60405180910390f35b6101be60048036038101906101b99190611d1a565b610589565b005b6101da60048036038101906101d59190611c04565b6106a1565b005b6101f660048036038101906101f19190611c04565b610701565b005b610212600480360381019061020d9190611e2c565b610721565b60405161021f9190612114565b60405180910390f35b610242600480360381019061023d9190611b97565b6107d3565b60405161024f919061238f565b60405180910390f35b61026061088b565b005b61026a61089f565b6040516102779190612114565b60405180910390f35b6102886108c9565b6040516102959190612196565b60405180910390f35b6102b860048036038101906102b39190611e2c565b61095b565b6040516102c69291906121b8565b60405180910390f35b6102e960048036038101906102e49190611db4565b610a9f565b005b61030560048036038101906103009190611e2c565b610b35565b6040516103129190612114565b60405180910390f35b61033560048036038101906103309190611cda565b610b68565b005b610351600480360381019061034c9190611c57565b610b7e565b005b61036d60048036038101906103689190611e2c565b610be0565b60405161037a9190612196565b60405180910390f35b61039d60048036038101906103989190611bc4565b610c48565b6040516103aa919061217b565b60405180910390f35b6103cd60048036038101906103c89190611b97565b610cdc565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061049a57507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806104aa57506104a982610d60565b5b9050919050565b6060600080546104c09061262a565b80601f01602080910402602001604051908101604052809291908181526020018280546104ec9061262a565b80156105395780601f1061050e57610100808354040283529160200191610539565b820191906000526020600020905b81548152906001019060200180831161051c57829003601f168201915b5050505050905090565b600061054e82610dca565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b600061059482610721565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415610605576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016105fc9061234f565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff16610624610e15565b73ffffffffffffffffffffffffffffffffffffffff16148061065357506106528161064d610e15565b610c48565b5b610692576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610689906122ef565b60405180910390fd5b61069c8383610e1d565b505050565b6106b26106ac610e15565b82610ed6565b6106f1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106e89061236f565b60405180910390fd5b6106fc838383610f6b565b505050565b61071c83838360405180602001604052806000815250610b7e565b505050565b6000806002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156107ca576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107c19061232f565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610844576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161083b906122cf565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b6108936111d2565b61089d6000611250565b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b6060600180546108d89061262a565b80601f01602080910402602001604051908101604052809291908181526020018280546109049061262a565b80156109515780601f1061092657610100808354040283529160200191610951565b820191906000526020600020905b81548152906001019060200180831161093457829003601f168201915b5050505050905090565b6007818154811061096b57600080fd5b906000526020600020906002020160009150905080600001805461098e9061262a565b80601f01602080910402602001604051908101604052809291908181526020018280546109ba9061262a565b8015610a075780601f106109dc57610100808354040283529160200191610a07565b820191906000526020600020905b8154815290600101906020018083116109ea57829003601f168201915b505050505090806001018054610a1c9061262a565b80601f0160208091040260200160405190810160405280929190818152602001828054610a489061262a565b8015610a955780601f10610a6a57610100808354040283529160200191610a95565b820191906000526020600020905b815481529060010190602001808311610a7857829003601f168201915b5050505050905082565b6000825111610ae3576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ada906122af565b60405180910390fd5b6000815111610b27576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610b1e906121ef565b60405180910390fd5b610b318282611316565b5050565b60086020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b610b7a610b73610e15565b838361143a565b5050565b610b8f610b89610e15565b83610ed6565b610bce576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610bc59061236f565b60405180910390fd5b610bda848484846115a7565b50505050565b6060610beb82610dca565b6000610bf5611603565b90506000815111610c155760405180602001604052806000815250610c40565b80610c1f8461161a565b604051602001610c309291906120f0565b6040516020818303038152906040525b915050919050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b610ce46111d2565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610d54576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610d4b9061222f565b60405180910390fd5b610d5d81611250565b50565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610dd38161177b565b610e12576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610e099061232f565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16610e9083610721565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b600080610ee283610721565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff161480610f245750610f238185610c48565b5b80610f6257508373ffffffffffffffffffffffffffffffffffffffff16610f4a84610543565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff16610f8b82610721565b73ffffffffffffffffffffffffffffffffffffffff1614610fe1576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610fd89061224f565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611051576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016110489061226f565b60405180910390fd5b61105c8383836117e7565b611067600082610e1d565b6001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546110b79190612540565b925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461110e91906124b9565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a46111cd8383836117ec565b505050565b6111da610e15565b73ffffffffffffffffffffffffffffffffffffffff166111f861089f565b73ffffffffffffffffffffffffffffffffffffffff161461124e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016112459061230f565b60405180910390fd5b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b6007604051806040016040528084815260200183815250908060018154018082558091505060019003906000526020600020906002020160009091909190915060008201518160000190805190602001906113729291906119ab565b50602082015181600101908051906020019061138f9291906119ab565b505050600060016007805490506113a69190612540565b9050336008600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507f6891983d42a48e510754f618abfbc8c414f4b10f9cf5d0f428133dbc60d5eb2481848460405161142d939291906123aa565b60405180910390a1505050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156114a9576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016114a09061228f565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c318360405161159a919061217b565b60405180910390a3505050565b6115b2848484610f6b565b6115be848484846117f1565b6115fd576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016115f49061220f565b60405180910390fd5b50505050565b606060405180602001604052806000815250905090565b60606000821415611662576040518060400160405280600181526020017f30000000000000000000000000000000000000000000000000000000000000008152509050611776565b600082905060005b6000821461169457808061167d9061268d565b915050600a8261168d919061250f565b915061166a565b60008167ffffffffffffffff8111156116b0576116af6127c3565b5b6040519080825280601f01601f1916602001820160405280156116e25781602001600182028036833780820191505090505b5090505b6000851461176f576001826116fb9190612540565b9150600a8561170a91906126d6565b603061171691906124b9565b60f81b81838151811061172c5761172b612794565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600a85611768919061250f565b94506116e6565b8093505050505b919050565b60008073ffffffffffffffffffffffffffffffffffffffff166002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614159050919050565b505050565b505050565b60006118128473ffffffffffffffffffffffffffffffffffffffff16611988565b1561197b578373ffffffffffffffffffffffffffffffffffffffff1663150b7a0261183b610e15565b8786866040518563ffffffff1660e01b815260040161185d949392919061212f565b602060405180830381600087803b15801561187757600080fd5b505af19250505080156118a857506040513d601f19601f820116820180604052508101906118a59190611d87565b60015b61192b573d80600081146118d8576040519150601f19603f3d011682016040523d82523d6000602084013e6118dd565b606091505b50600081511415611923576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161191a9061220f565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611980565b600190505b949350505050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b8280546119b79061262a565b90600052602060002090601f0160209004810192826119d95760008555611a20565b82601f106119f257805160ff1916838001178555611a20565b82800160010185558215611a20579182015b82811115611a1f578251825591602001919060010190611a04565b5b509050611a2d9190611a31565b5090565b5b80821115611a4a576000816000905550600101611a32565b5090565b6000611a61611a5c84612414565b6123ef565b905082815260208101848484011115611a7d57611a7c6127f7565b5b611a888482856125e8565b509392505050565b6000611aa3611a9e84612445565b6123ef565b905082815260208101848484011115611abf57611abe6127f7565b5b611aca8482856125e8565b509392505050565b600081359050611ae181612ba8565b92915050565b600081359050611af681612bbf565b92915050565b600081359050611b0b81612bd6565b92915050565b600081519050611b2081612bd6565b92915050565b600082601f830112611b3b57611b3a6127f2565b5b8135611b4b848260208601611a4e565b91505092915050565b600082601f830112611b6957611b686127f2565b5b8135611b79848260208601611a90565b91505092915050565b600081359050611b9181612bed565b92915050565b600060208284031215611bad57611bac612801565b5b6000611bbb84828501611ad2565b91505092915050565b60008060408385031215611bdb57611bda612801565b5b6000611be985828601611ad2565b9250506020611bfa85828601611ad2565b9150509250929050565b600080600060608486031215611c1d57611c1c612801565b5b6000611c2b86828701611ad2565b9350506020611c3c86828701611ad2565b9250506040611c4d86828701611b82565b9150509250925092565b60008060008060808587031215611c7157611c70612801565b5b6000611c7f87828801611ad2565b9450506020611c9087828801611ad2565b9350506040611ca187828801611b82565b925050606085013567ffffffffffffffff811115611cc257611cc16127fc565b5b611cce87828801611b26565b91505092959194509250565b60008060408385031215611cf157611cf0612801565b5b6000611cff85828601611ad2565b9250506020611d1085828601611ae7565b9150509250929050565b60008060408385031215611d3157611d30612801565b5b6000611d3f85828601611ad2565b9250506020611d5085828601611b82565b9150509250929050565b600060208284031215611d7057611d6f612801565b5b6000611d7e84828501611afc565b91505092915050565b600060208284031215611d9d57611d9c612801565b5b6000611dab84828501611b11565b91505092915050565b60008060408385031215611dcb57611dca612801565b5b600083013567ffffffffffffffff811115611de957611de86127fc565b5b611df585828601611b54565b925050602083013567ffffffffffffffff811115611e1657611e156127fc565b5b611e2285828601611b54565b9150509250929050565b600060208284031215611e4257611e41612801565b5b6000611e5084828501611b82565b91505092915050565b611e6281612574565b82525050565b611e7181612586565b82525050565b6000611e8282612476565b611e8c818561248c565b9350611e9c8185602086016125f7565b611ea581612806565b840191505092915050565b6000611ebb82612481565b611ec5818561249d565b9350611ed58185602086016125f7565b611ede81612806565b840191505092915050565b6000611ef482612481565b611efe81856124ae565b9350611f0e8185602086016125f7565b80840191505092915050565b6000611f2760228361249d565b9150611f3282612817565b604082019050919050565b6000611f4a60328361249d565b9150611f5582612866565b604082019050919050565b6000611f6d60268361249d565b9150611f78826128b5565b604082019050919050565b6000611f9060258361249d565b9150611f9b82612904565b604082019050919050565b6000611fb360248361249d565b9150611fbe82612953565b604082019050919050565b6000611fd660198361249d565b9150611fe1826129a2565b602082019050919050565b6000611ff960238361249d565b9150612004826129cb565b604082019050919050565b600061201c60298361249d565b915061202782612a1a565b604082019050919050565b600061203f603e8361249d565b915061204a82612a69565b604082019050919050565b600061206260208361249d565b915061206d82612ab8565b602082019050919050565b600061208560188361249d565b915061209082612ae1565b602082019050919050565b60006120a860218361249d565b91506120b382612b0a565b604082019050919050565b60006120cb602e8361249d565b91506120d682612b59565b604082019050919050565b6120ea816125de565b82525050565b60006120fc8285611ee9565b91506121088284611ee9565b91508190509392505050565b60006020820190506121296000830184611e59565b92915050565b60006080820190506121446000830187611e59565b6121516020830186611e59565b61215e60408301856120e1565b81810360608301526121708184611e77565b905095945050505050565b60006020820190506121906000830184611e68565b92915050565b600060208201905081810360008301526121b08184611eb0565b905092915050565b600060408201905081810360008301526121d28185611eb0565b905081810360208301526121e68184611eb0565b90509392505050565b6000602082019050818103600083015261220881611f1a565b9050919050565b6000602082019050818103600083015261222881611f3d565b9050919050565b6000602082019050818103600083015261224881611f60565b9050919050565b6000602082019050818103600083015261226881611f83565b9050919050565b6000602082019050818103600083015261228881611fa6565b9050919050565b600060208201905081810360008301526122a881611fc9565b9050919050565b600060208201905081810360008301526122c881611fec565b9050919050565b600060208201905081810360008301526122e88161200f565b9050919050565b6000602082019050818103600083015261230881612032565b9050919050565b6000602082019050818103600083015261232881612055565b9050919050565b6000602082019050818103600083015261234881612078565b9050919050565b600060208201905081810360008301526123688161209b565b9050919050565b60006020820190508181036000830152612388816120be565b9050919050565b60006020820190506123a460008301846120e1565b92915050565b60006060820190506123bf60008301866120e1565b81810360208301526123d18185611eb0565b905081810360408301526123e58184611eb0565b9050949350505050565b60006123f961240a565b9050612405828261265c565b919050565b6000604051905090565b600067ffffffffffffffff82111561242f5761242e6127c3565b5b61243882612806565b9050602081019050919050565b600067ffffffffffffffff8211156124605761245f6127c3565b5b61246982612806565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b60006124c4826125de565b91506124cf836125de565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0382111561250457612503612707565b5b828201905092915050565b600061251a826125de565b9150612525836125de565b92508261253557612534612736565b5b828204905092915050565b600061254b826125de565b9150612556836125de565b92508282101561256957612568612707565b5b828203905092915050565b600061257f826125be565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156126155780820151818401526020810190506125fa565b83811115612624576000848401525b50505050565b6000600282049050600182168061264257607f821691505b6020821081141561265657612655612765565b5b50919050565b61266582612806565b810181811067ffffffffffffffff82111715612684576126836127c3565b5b80604052505050565b6000612698826125de565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156126cb576126ca612707565b5b600182019050919050565b60006126e1826125de565b91506126ec836125de565b9250826126fc576126fb612736565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f6d697373696e6720495046532075726c20666f7220746865206461746120697460008201527f656d000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4f776e61626c653a206e6577206f776e657220697320746865207a65726f206160008201527f6464726573730000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f6d697373696e672049504653206861736820666f72207468652064617461206960008201527f74656d0000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206e6f7220617070726f76656420666f7220616c6c0000602082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206e6f7220617070726f766564000000000000000000000000000000000000602082015250565b612bb181612574565b8114612bbc57600080fd5b50565b612bc881612586565b8114612bd357600080fd5b50565b612bdf81612592565b8114612bea57600080fd5b50565b612bf6816125de565b8114612c0157600080fd5b5056fea2646970667358221220fd7eefb5b0cc27c31422e57a9b06e9f634f8e109dec1c53baaaadcf7e03f91e264736f6c63430008070033"