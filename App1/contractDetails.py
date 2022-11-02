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
		"name": "mint",
		"outputs": [],
		"stateMutability": "nonpayable",
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
				"internalType": "string",
				"name": "_tokenURI",
				"type": "string"
			}
		],
		"name": "setTokenURI",
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

bytecode =	"60806040523480156200001157600080fd5b506040518060400160405280600881526020017f46697273744e46540000000000000000000000000000000000000000000000008152506040518060400160405280600881526020017f46495253544e4654000000000000000000000000000000000000000000000000815250816000908051906020019062000096929190620001a6565b508060019080519060200190620000af929190620001a6565b505050620000d2620000c6620000d860201b60201c565b620000e060201b60201c565b620002bb565b600033905090565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b828054620001b49062000256565b90600052602060002090601f016020900481019282620001d8576000855562000224565b82601f10620001f357805160ff191683800117855562000224565b8280016001018555821562000224579182015b828111156200022357825182559160200191906001019062000206565b5b50905062000233919062000237565b5090565b5b808211156200025257600081600090555060010162000238565b5090565b600060028204905060018216806200026f57607f821691505b602082108114156200028657620002856200028c565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b612b1a80620002cb6000396000f3fe608060405234801561001057600080fd5b50600436106101165760003560e01c8063715018a6116100a2578063b88d4fde11610071578063b88d4fde146102b9578063c87b56dd146102d5578063e0df5b6f14610305578063e985e9c514610321578063f2fde38b1461035157610116565b8063715018a6146102575780638da5cb5b1461026157806395d89b411461027f578063a22cb4651461029d57610116565b80631249c58b116100e95780631249c58b146101b557806323b872dd146101bf57806342842e0e146101db5780636352211e146101f757806370a082311461022757610116565b806301ffc9a71461011b57806306fdde031461014b578063081812fc14610169578063095ea7b314610199575b600080fd5b61013560048036038101906101309190611cc5565b61036d565b60405161014291906120da565b60405180910390f35b61015361044f565b60405161016091906120f5565b60405180910390f35b610183600480360381019061017e9190611d68565b6104e1565b6040516101909190612073565b60405180910390f35b6101b360048036038101906101ae9190611c85565b610527565b005b6101bd61063f565b005b6101d960048036038101906101d49190611b6f565b61066b565b005b6101f560048036038101906101f09190611b6f565b6106cb565b005b610211600480360381019061020c9190611d68565b6106eb565b60405161021e9190612073565b60405180910390f35b610241600480360381019061023c9190611b02565b61079d565b60405161024e91906122d7565b60405180910390f35b61025f610855565b005b610269610869565b6040516102769190612073565b60405180910390f35b610287610893565b60405161029491906120f5565b60405180910390f35b6102b760048036038101906102b29190611c45565b610925565b005b6102d360048036038101906102ce9190611bc2565b61093b565b005b6102ef60048036038101906102ea9190611d68565b61099d565b6040516102fc91906120f5565b60405180910390f35b61031f600480360381019061031a9190611d1f565b610a05565b005b61033b60048036038101906103369190611b2f565b610a84565b60405161034891906120da565b60405180910390f35b61036b60048036038101906103669190611b02565b610b18565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061043857507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b80610448575061044782610b9c565b5b9050919050565b60606000805461045e9061252d565b80601f016020809104026020016040519081016040528092919081815260200182805461048a9061252d565b80156104d75780601f106104ac576101008083540402835291602001916104d7565b820191906000526020600020905b8154815290600101906020018083116104ba57829003601f168201915b5050505050905090565b60006104ec82610c06565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6000610532826106eb565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156105a3576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161059a90612277565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff166105c2610c51565b73ffffffffffffffffffffffffffffffffffffffff1614806105f157506105f0816105eb610c51565b610a84565b5b610630576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610627906121f7565b60405180910390fd5b61063a8383610c59565b505050565b600060075490506106503382610d12565b6007600081548092919061066390612590565b919050555050565b61067c610676610c51565b82610d30565b6106bb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106b2906122b7565b60405180910390fd5b6106c6838383610dc5565b505050565b6106e68383836040518060200160405280600081525061093b565b505050565b6000806002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610794576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161078b90612257565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141561080e576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610805906121d7565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b61085d61102c565b61086760006110aa565b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b6060600180546108a29061252d565b80601f01602080910402602001604051908101604052809291908181526020018280546108ce9061252d565b801561091b5780601f106108f05761010080835404028352916020019161091b565b820191906000526020600020905b8154815290600101906020018083116108fe57829003601f168201915b5050505050905090565b610937610930610c51565b8383611170565b5050565b61094c610946610c51565b83610d30565b61098b576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610982906122b7565b60405180910390fd5b610997848484846112dd565b50505050565b60606109a882610c06565b60006109b2611339565b905060008151116109d257604051806020016040528060008152506109fd565b806109dc84611350565b6040516020016109ed92919061204f565b6040516020818303038152906040525b915050919050565b610a0d61102c565b610a186007546114b1565b610a57576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610a4e90612297565b60405180910390fd5b806008600060075481526020019081526020016000209080519060200190610a80929190611916565b5050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b610b2061102c565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610b90576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610b8790612137565b60405180910390fd5b610b99816110aa565b50565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610c0f816114b1565b610c4e576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610c4590612257565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16610ccc836106eb565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b610d2c82826040518060200160405280600081525061151d565b5050565b600080610d3c836106eb565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff161480610d7e5750610d7d8185610a84565b5b80610dbc57508373ffffffffffffffffffffffffffffffffffffffff16610da4846104e1565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff16610de5826106eb565b73ffffffffffffffffffffffffffffffffffffffff1614610e3b576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610e3290612157565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610eab576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ea290612197565b60405180910390fd5b610eb6838383611578565b610ec1600082610c59565b6001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254610f119190612443565b925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254610f6891906123bc565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a461102783838361157d565b505050565b611034610c51565b73ffffffffffffffffffffffffffffffffffffffff16611052610869565b73ffffffffffffffffffffffffffffffffffffffff16146110a8576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161109f90612237565b60405180910390fd5b565b6000600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156111df576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111d6906121b7565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31836040516112d091906120da565b60405180910390a3505050565b6112e8848484610dc5565b6112f484848484611582565b611333576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161132a90612117565b60405180910390fd5b50505050565b606060405180602001604052806000815250905090565b60606000821415611398576040518060400160405280600181526020017f300000000000000000000000000000000000000000000000000000000000000081525090506114ac565b600082905060005b600082146113ca5780806113b390612590565b915050600a826113c39190612412565b91506113a0565b60008167ffffffffffffffff8111156113e6576113e56126c6565b5b6040519080825280601f01601f1916602001820160405280156114185781602001600182028036833780820191505090505b5090505b600085146114a5576001826114319190612443565b9150600a8561144091906125d9565b603061144c91906123bc565b60f81b81838151811061146257611461612697565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600a8561149e9190612412565b945061141c565b8093505050505b919050565b60008073ffffffffffffffffffffffffffffffffffffffff166002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614159050919050565b6115278383611719565b6115346000848484611582565b611573576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161156a90612117565b60405180910390fd5b505050565b505050565b505050565b60006115a38473ffffffffffffffffffffffffffffffffffffffff166118f3565b1561170c578373ffffffffffffffffffffffffffffffffffffffff1663150b7a026115cc610c51565b8786866040518563ffffffff1660e01b81526004016115ee949392919061208e565b602060405180830381600087803b15801561160857600080fd5b505af192505050801561163957506040513d601f19601f820116820180604052508101906116369190611cf2565b60015b6116bc573d8060008114611669576040519150601f19603f3d011682016040523d82523d6000602084013e61166e565b606091505b506000815114156116b4576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016116ab90612117565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611711565b600190505b949350505050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611789576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161178090612217565b60405180910390fd5b611792816114b1565b156117d2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016117c990612177565b60405180910390fd5b6117de60008383611578565b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461182e91906123bc565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a46118ef6000838361157d565b5050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b8280546119229061252d565b90600052602060002090601f016020900481019282611944576000855561198b565b82601f1061195d57805160ff191683800117855561198b565b8280016001018555821561198b579182015b8281111561198a57825182559160200191906001019061196f565b5b509050611998919061199c565b5090565b5b808211156119b557600081600090555060010161199d565b5090565b60006119cc6119c784612317565b6122f2565b9050828152602081018484840111156119e8576119e76126fa565b5b6119f38482856124eb565b509392505050565b6000611a0e611a0984612348565b6122f2565b905082815260208101848484011115611a2a57611a296126fa565b5b611a358482856124eb565b509392505050565b600081359050611a4c81612a88565b92915050565b600081359050611a6181612a9f565b92915050565b600081359050611a7681612ab6565b92915050565b600081519050611a8b81612ab6565b92915050565b600082601f830112611aa657611aa56126f5565b5b8135611ab68482602086016119b9565b91505092915050565b600082601f830112611ad457611ad36126f5565b5b8135611ae48482602086016119fb565b91505092915050565b600081359050611afc81612acd565b92915050565b600060208284031215611b1857611b17612704565b5b6000611b2684828501611a3d565b91505092915050565b60008060408385031215611b4657611b45612704565b5b6000611b5485828601611a3d565b9250506020611b6585828601611a3d565b9150509250929050565b600080600060608486031215611b8857611b87612704565b5b6000611b9686828701611a3d565b9350506020611ba786828701611a3d565b9250506040611bb886828701611aed565b9150509250925092565b60008060008060808587031215611bdc57611bdb612704565b5b6000611bea87828801611a3d565b9450506020611bfb87828801611a3d565b9350506040611c0c87828801611aed565b925050606085013567ffffffffffffffff811115611c2d57611c2c6126ff565b5b611c3987828801611a91565b91505092959194509250565b60008060408385031215611c5c57611c5b612704565b5b6000611c6a85828601611a3d565b9250506020611c7b85828601611a52565b9150509250929050565b60008060408385031215611c9c57611c9b612704565b5b6000611caa85828601611a3d565b9250506020611cbb85828601611aed565b9150509250929050565b600060208284031215611cdb57611cda612704565b5b6000611ce984828501611a67565b91505092915050565b600060208284031215611d0857611d07612704565b5b6000611d1684828501611a7c565b91505092915050565b600060208284031215611d3557611d34612704565b5b600082013567ffffffffffffffff811115611d5357611d526126ff565b5b611d5f84828501611abf565b91505092915050565b600060208284031215611d7e57611d7d612704565b5b6000611d8c84828501611aed565b91505092915050565b611d9e81612477565b82525050565b611dad81612489565b82525050565b6000611dbe82612379565b611dc8818561238f565b9350611dd88185602086016124fa565b611de181612709565b840191505092915050565b6000611df782612384565b611e0181856123a0565b9350611e118185602086016124fa565b611e1a81612709565b840191505092915050565b6000611e3082612384565b611e3a81856123b1565b9350611e4a8185602086016124fa565b80840191505092915050565b6000611e636032836123a0565b9150611e6e8261271a565b604082019050919050565b6000611e866026836123a0565b9150611e9182612769565b604082019050919050565b6000611ea96025836123a0565b9150611eb4826127b8565b604082019050919050565b6000611ecc601c836123a0565b9150611ed782612807565b602082019050919050565b6000611eef6024836123a0565b9150611efa82612830565b604082019050919050565b6000611f126019836123a0565b9150611f1d8261287f565b602082019050919050565b6000611f356029836123a0565b9150611f40826128a8565b604082019050919050565b6000611f58603e836123a0565b9150611f63826128f7565b604082019050919050565b6000611f7b6020836123a0565b9150611f8682612946565b602082019050919050565b6000611f9e6020836123a0565b9150611fa98261296f565b602082019050919050565b6000611fc16018836123a0565b9150611fcc82612998565b602082019050919050565b6000611fe46021836123a0565b9150611fef826129c1565b604082019050919050565b60006120076020836123a0565b915061201282612a10565b602082019050919050565b600061202a602e836123a0565b915061203582612a39565b604082019050919050565b612049816124e1565b82525050565b600061205b8285611e25565b91506120678284611e25565b91508190509392505050565b60006020820190506120886000830184611d95565b92915050565b60006080820190506120a36000830187611d95565b6120b06020830186611d95565b6120bd6040830185612040565b81810360608301526120cf8184611db3565b905095945050505050565b60006020820190506120ef6000830184611da4565b92915050565b6000602082019050818103600083015261210f8184611dec565b905092915050565b6000602082019050818103600083015261213081611e56565b9050919050565b6000602082019050818103600083015261215081611e79565b9050919050565b6000602082019050818103600083015261217081611e9c565b9050919050565b6000602082019050818103600083015261219081611ebf565b9050919050565b600060208201905081810360008301526121b081611ee2565b9050919050565b600060208201905081810360008301526121d081611f05565b9050919050565b600060208201905081810360008301526121f081611f28565b9050919050565b6000602082019050818103600083015261221081611f4b565b9050919050565b6000602082019050818103600083015261223081611f6e565b9050919050565b6000602082019050818103600083015261225081611f91565b9050919050565b6000602082019050818103600083015261227081611fb4565b9050919050565b6000602082019050818103600083015261229081611fd7565b9050919050565b600060208201905081810360008301526122b081611ffa565b9050919050565b600060208201905081810360008301526122d08161201d565b9050919050565b60006020820190506122ec6000830184612040565b92915050565b60006122fc61230d565b9050612308828261255f565b919050565b6000604051905090565b600067ffffffffffffffff821115612332576123316126c6565b5b61233b82612709565b9050602081019050919050565b600067ffffffffffffffff821115612363576123626126c6565b5b61236c82612709565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b60006123c7826124e1565b91506123d2836124e1565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156124075761240661260a565b5b828201905092915050565b600061241d826124e1565b9150612428836124e1565b92508261243857612437612639565b5b828204905092915050565b600061244e826124e1565b9150612459836124e1565b92508282101561246c5761246b61260a565b5b828203905092915050565b6000612482826124c1565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156125185780820151818401526020810190506124fd565b83811115612527576000848401525b50505050565b6000600282049050600182168061254557607f821691505b6020821081141561255957612558612668565b5b50919050565b61256882612709565b810181811067ffffffffffffffff82111715612587576125866126c6565b5b80604052505050565b600061259b826124e1565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156125ce576125cd61260a565b5b600182019050919050565b60006125e4826124e1565b91506125ef836124e1565b9250826125ff576125fe612639565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4f776e61626c653a206e6577206f776e657220697320746865207a65726f206160008201527f6464726573730000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206e6f7220617070726f76656420666f7220616c6c0000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f55524920717565727920666f72206e6f6e2d6578697374616e7420746f6b656e600082015250565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206e6f7220617070726f766564000000000000000000000000000000000000602082015250565b612a9181612477565b8114612a9c57600080fd5b50565b612aa881612489565b8114612ab357600080fd5b50565b612abf81612495565b8114612aca57600080fd5b50565b612ad6816124e1565b8114612ae157600080fd5b5056fea264697066735822122032aa67d5d7f48fd8787c0db7e672077afbf61b65ea4ff73b5d501d2a4814e59b64736f6c63430008070033"