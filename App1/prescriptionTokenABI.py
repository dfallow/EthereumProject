import json

abi = json.loads("""[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "patient",
				"type": "address"
			}
		],
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
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"name": "ContractOwnershipTransfered",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "minter",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Minted",
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
				"indexed": false,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "TokenOwnershipTransfered",
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
				"internalType": "uint256",
				"name": "_prescriptionTokenId",
				"type": "uint256"
			}
		],
		"name": "getMachineTokenId",
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
		"inputs": [],
		"name": "getPatient",
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
		"inputs": [
			{
				"internalType": "string",
				"name": "ipfsDataURL",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "machineTokenId",
				"type": "uint256"
			}
		],
		"name": "mintPrescriptionToken",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
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
		"name": "numberOfPrescriptionTokens",
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
		"name": "transferTokenOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]""")

bytecode = "60806040523480156200001157600080fd5b5060405162003791380380620037918339818101604052810190620000379190620002e5565b6040518060400160405280601181526020017f507265736372697074696f6e546f6b656e0000000000000000000000000000008152506040518060400160405280600381526020017f50544b00000000000000000000000000000000000000000000000000000000008152508160009080519060200190620000bb9291906200021e565b508060019080519060200190620000d49291906200021e565b505050620000f7620000eb6200015060201b60201c565b6200015860201b60201c565b62000108336200015860201b60201c565b80600960006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050620003cf565b600033905090565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8280546200022c906200034b565b90600052602060002090601f0160209004810192826200025057600085556200029c565b82601f106200026b57805160ff19168380011785556200029c565b828001600101855582156200029c579182015b828111156200029b5782518255916020019190600101906200027e565b5b509050620002ab9190620002af565b5090565b5b80821115620002ca576000816000905550600101620002b0565b5090565b600081519050620002df81620003b5565b92915050565b600060208284031215620002fe57620002fd620003b0565b5b60006200030e84828501620002ce565b91505092915050565b600062000324826200032b565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600060028204905060018216806200036457607f821691505b602082108114156200037b576200037a62000381565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600080fd5b620003c08162000317565b8114620003cc57600080fd5b50565b6133b280620003df6000396000f3fe608060405234801561001057600080fd5b50600436106101375760003560e01c80637b0f9a36116100b8578063ac2f76271161007c578063ac2f76271461033c578063b88d4fde1461036c578063c87b56dd14610388578063e985e9c5146103b8578063efc264d8146103e8578063f2fde38b1461040457610137565b80637b0f9a36146102a85780637d0cfaf7146102c65780638da5cb5b146102e457806395d89b4114610302578063a22cb4651461032057610137565b806323b872dd116100ff57806323b872dd1461020657806342842e0e146102225780636352211e1461023e57806370a082311461026e578063715018a61461029e57610137565b806301ffc9a71461013c57806304fecbd21461016c57806306fdde031461019c578063081812fc146101ba578063095ea7b3146101ea575b600080fd5b61015660048036038101906101519190612451565b610420565b60405161016391906128f6565b60405180910390f35b610186600480360381019061018191906124ab565b610502565b6040516101939190612b33565b60405180910390f35b6101a46105e7565b6040516101b19190612911565b60405180910390f35b6101d460048036038101906101cf9190612507565b610679565b6040516101e19190612858565b60405180910390f35b61020460048036038101906101ff9190612411565b6106bf565b005b610220600480360381019061021b91906122fb565b6107d7565b005b61023c600480360381019061023791906122fb565b610837565b005b61025860048036038101906102539190612507565b610857565b6040516102659190612858565b60405180910390f35b6102886004803603810190610283919061228e565b6108de565b6040516102959190612b33565b60405180910390f35b6102a6610996565b005b6102b06109aa565b6040516102bd9190612858565b60405180910390f35b6102ce6109dc565b6040516102db9190612b33565b60405180910390f35b6102ec6109e2565b6040516102f99190612858565b60405180910390f35b61030a610a0c565b6040516103179190612911565b60405180910390f35b61033a600480360381019061033591906123d1565b610a9e565b005b61035660048036038101906103519190612507565b610ab4565b6040516103639190612b33565b60405180910390f35b6103866004803603810190610381919061234e565b610b89565b005b6103a2600480360381019061039d9190612507565b610beb565b6040516103af9190612911565b60405180910390f35b6103d260048036038101906103cd91906122bb565b610cd0565b6040516103df91906128f6565b60405180910390f35b61040260048036038101906103fd9190612411565b610d64565b005b61041e6004803603810190610419919061228e565b610db6565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806104eb57507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806104fb57506104fa82610e02565b5b9050919050565b600061050c610e6c565b6000835111610550576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161054790612933565b60405180910390fd5b6001600860008282546105639190612c18565b925050819055506000600854905061057b3382610eea565b6105858185610f08565b3373ffffffffffffffffffffffffffffffffffffffff167f30385c845b448a36257a6a1716e6ad2e1bc2cbe333cde1e69fe849ad6511adfe826040516105cb9190612b33565b60405180910390a26105dd8184610f7c565b8091505092915050565b6060600080546105f690612d58565b80601f016020809104026020016040519081016040528092919081815260200182805461062290612d58565b801561066f5780601f106106445761010080835404028352916020019161066f565b820191906000526020600020905b81548152906001019060200180831161065257829003601f168201915b5050505050905090565b600061068482610fde565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b60006106ca82610857565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141561073b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161073290612af3565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1661075a611029565b73ffffffffffffffffffffffffffffffffffffffff161480610789575061078881610783611029565b610cd0565b5b6107c8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107bf90612b13565b60405180910390fd5b6107d28383611031565b505050565b6107e86107e2611029565b826110ea565b610827576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161081e90612973565b60405180910390fd5b61083283838361117f565b505050565b61085283838360405180602001604052806000815250610b89565b505050565b60008061086383611479565b9050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156108d5576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108cc90612ad3565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141561094f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161094690612a53565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b61099e610e6c565b6109a860006114b6565b565b60006109b4610e6c565b600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60085481565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b606060018054610a1b90612d58565b80601f0160208091040260200160405190810160405280929190818152602001828054610a4790612d58565b8015610a945780601f10610a6957610100808354040283529160200191610a94565b820191906000526020600020905b815481529060010190602001808311610a7757829003601f168201915b5050505050905090565b610ab0610aa9611029565b838361157c565b5050565b6000610abf826116e9565b610afe576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610af590612993565b60405180910390fd5b60005b600a80549050811015610b825782600a8281548110610b2357610b22612e91565b5b9060005260206000209060020201600001541415610b6f576000600a8281548110610b5157610b50612e91565b5b90600052602060002090600202019050806001015492505050610b84565b8080610b7a90612dbb565b915050610b01565b505b919050565b610b9a610b94611029565b836110ea565b610bd9576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610bd090612973565b60405180910390fd5b610be58484848461172a565b50505050565b60606000610bf76109e2565b9050600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161480610c8057508073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16145b610cbf576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610cb690612953565b60405180910390fd5b610cc883611786565b915050919050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b610d6c610e6c565b610d77338383610837565b7fa7c27348009168856f275fb50a95861283a8e29841e4b1f545d9756441a0e976338383604051610daa93929190612873565b60405180910390a15050565b610dbe610e6c565b610dc7816114b6565b7fd343d0dee30ef8ca0d7672d51449779c672b1c67a6c496870ff741efe62ce6ab6001604051610df791906128f6565b60405180910390a150565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610e74611029565b73ffffffffffffffffffffffffffffffffffffffff16610e926109e2565b73ffffffffffffffffffffffffffffffffffffffff1614610ee8576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610edf90612ab3565b60405180910390fd5b565b610f04828260405180602001604052806000815250611899565b5050565b610f11826116e9565b610f50576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610f4790612a73565b60405180910390fd5b80600660008481526020019081526020016000209080519060200190610f779291906120a2565b505050565b610f84610e6c565b600a6040518060400160405280848152602001838152509080600181540180825580915050600190039060005260206000209060020201600090919091909150600082015181600001556020820151816001015550505050565b610fe7816116e9565b611026576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161101d90612ad3565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff166110a483610857565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b6000806110f683610857565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16148061113857506111378185610cd0565b5b8061117657508373ffffffffffffffffffffffffffffffffffffffff1661115e84610679565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff1661119f82610857565b73ffffffffffffffffffffffffffffffffffffffff16146111f5576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111ec906129d3565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611265576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161125c90612a13565b60405180910390fd5b61127283838360016118f4565b8273ffffffffffffffffffffffffffffffffffffffff1661129282610857565b73ffffffffffffffffffffffffffffffffffffffff16146112e8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016112df906129d3565b60405180910390fd5b6004600082815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a46114748383836001611a1a565b505050565b60006002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156115eb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016115e290612a33565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31836040516116dc91906128f6565b60405180910390a3505050565b60008073ffffffffffffffffffffffffffffffffffffffff1661170b83611479565b73ffffffffffffffffffffffffffffffffffffffff1614159050919050565b61173584848461117f565b61174184848484611a20565b611780576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611777906129b3565b60405180910390fd5b50505050565b606061179182610fde565b60006006600084815260200190815260200160002080546117b190612d58565b80601f01602080910402602001604051908101604052809291908181526020018280546117dd90612d58565b801561182a5780601f106117ff5761010080835404028352916020019161182a565b820191906000526020600020905b81548152906001019060200180831161180d57829003601f168201915b50505050509050600061183b611bb7565b9050600081511415611851578192505050611894565b60008251111561188657808260405160200161186e929190612834565b60405160208183030381529060405292505050611894565b61188f84611bce565b925050505b919050565b6118a38383611c36565b6118b06000848484611a20565b6118ef576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016118e6906129b3565b60405180910390fd5b505050565b6001811115611a1457600073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16146119885780600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546119809190612c6e565b925050819055505b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614611a135780600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611a0b9190612c18565b925050819055505b5b50505050565b50505050565b6000611a418473ffffffffffffffffffffffffffffffffffffffff16611e54565b15611baa578373ffffffffffffffffffffffffffffffffffffffff1663150b7a02611a6a611029565b8786866040518563ffffffff1660e01b8152600401611a8c94939291906128aa565b602060405180830381600087803b158015611aa657600080fd5b505af1925050508015611ad757506040513d601f19601f82011682018060405250810190611ad4919061247e565b60015b611b5a573d8060008114611b07576040519150601f19603f3d011682016040523d82523d6000602084013e611b0c565b606091505b50600081511415611b52576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611b49906129b3565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611baf565b600190505b949350505050565b606060405180602001604052806000815250905090565b6060611bd982610fde565b6000611be3611bb7565b90506000815111611c035760405180602001604052806000815250611c2e565b80611c0d84611e77565b604051602001611c1e929190612834565b6040516020818303038152906040525b915050919050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611ca6576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611c9d90612a93565b60405180910390fd5b611caf816116e9565b15611cef576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611ce6906129f3565b60405180910390fd5b611cfd6000838360016118f4565b611d06816116e9565b15611d46576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611d3d906129f3565b60405180910390fd5b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a4611e50600083836001611a1a565b5050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b606060006001611e8684611f4f565b01905060008167ffffffffffffffff811115611ea557611ea4612ec0565b5b6040519080825280601f01601f191660200182016040528015611ed75781602001600182028036833780820191505090505b509050600082602001820190505b600115611f44578080600190039150507f3031323334353637383961626364656600000000000000000000000000000000600a86061a8153600a8581611f2e57611f2d612e33565b5b0494506000851415611f3f57611f44565b611ee5565b819350505050919050565b600080600090507a184f03e93ff9f4daa797ed6e38ed64bf6a1f0100000000000000008310611fad577a184f03e93ff9f4daa797ed6e38ed64bf6a1f0100000000000000008381611fa357611fa2612e33565b5b0492506040810190505b6d04ee2d6d415b85acef81000000008310611fea576d04ee2d6d415b85acef81000000008381611fe057611fdf612e33565b5b0492506020810190505b662386f26fc10000831061201957662386f26fc10000838161200f5761200e612e33565b5b0492506010810190505b6305f5e1008310612042576305f5e100838161203857612037612e33565b5b0492506008810190505b612710831061206757612710838161205d5761205c612e33565b5b0492506004810190505b6064831061208a57606483816120805761207f612e33565b5b0492506002810190505b600a8310612099576001810190505b80915050919050565b8280546120ae90612d58565b90600052602060002090601f0160209004810192826120d05760008555612117565b82601f106120e957805160ff1916838001178555612117565b82800160010185558215612117579182015b828111156121165782518255916020019190600101906120fb565b5b5090506121249190612128565b5090565b5b80821115612141576000816000905550600101612129565b5090565b600061215861215384612b73565b612b4e565b90508281526020810184848401111561217457612173612ef4565b5b61217f848285612d16565b509392505050565b600061219a61219584612ba4565b612b4e565b9050828152602081018484840111156121b6576121b5612ef4565b5b6121c1848285612d16565b509392505050565b6000813590506121d881613320565b92915050565b6000813590506121ed81613337565b92915050565b6000813590506122028161334e565b92915050565b6000815190506122178161334e565b92915050565b600082601f83011261223257612231612eef565b5b8135612242848260208601612145565b91505092915050565b600082601f8301126122605761225f612eef565b5b8135612270848260208601612187565b91505092915050565b60008135905061228881613365565b92915050565b6000602082840312156122a4576122a3612efe565b5b60006122b2848285016121c9565b91505092915050565b600080604083850312156122d2576122d1612efe565b5b60006122e0858286016121c9565b92505060206122f1858286016121c9565b9150509250929050565b60008060006060848603121561231457612313612efe565b5b6000612322868287016121c9565b9350506020612333868287016121c9565b925050604061234486828701612279565b9150509250925092565b6000806000806080858703121561236857612367612efe565b5b6000612376878288016121c9565b9450506020612387878288016121c9565b935050604061239887828801612279565b925050606085013567ffffffffffffffff8111156123b9576123b8612ef9565b5b6123c58782880161221d565b91505092959194509250565b600080604083850312156123e8576123e7612efe565b5b60006123f6858286016121c9565b9250506020612407858286016121de565b9150509250929050565b6000806040838503121561242857612427612efe565b5b6000612436858286016121c9565b925050602061244785828601612279565b9150509250929050565b60006020828403121561246757612466612efe565b5b6000612475848285016121f3565b91505092915050565b60006020828403121561249457612493612efe565b5b60006124a284828501612208565b91505092915050565b600080604083850312156124c2576124c1612efe565b5b600083013567ffffffffffffffff8111156124e0576124df612ef9565b5b6124ec8582860161224b565b92505060206124fd85828601612279565b9150509250929050565b60006020828403121561251d5761251c612efe565b5b600061252b84828501612279565b91505092915050565b61253d81612ca2565b82525050565b61254c81612cb4565b82525050565b600061255d82612bd5565b6125678185612beb565b9350612577818560208601612d25565b61258081612f03565b840191505092915050565b600061259682612be0565b6125a08185612bfc565b93506125b0818560208601612d25565b6125b981612f03565b840191505092915050565b60006125cf82612be0565b6125d98185612c0d565b93506125e9818560208601612d25565b80840191505092915050565b6000612602602283612bfc565b915061260d82612f14565b604082019050919050565b6000612625602e83612bfc565b915061263082612f63565b604082019050919050565b6000612648602d83612bfc565b915061265382612fb2565b604082019050919050565b600061266b601f83612bfc565b915061267682613001565b602082019050919050565b600061268e603283612bfc565b91506126998261302a565b604082019050919050565b60006126b1602583612bfc565b91506126bc82613079565b604082019050919050565b60006126d4601c83612bfc565b91506126df826130c8565b602082019050919050565b60006126f7602483612bfc565b9150612702826130f1565b604082019050919050565b600061271a601983612bfc565b915061272582613140565b602082019050919050565b600061273d602983612bfc565b915061274882613169565b604082019050919050565b6000612760602e83612bfc565b915061276b826131b8565b604082019050919050565b6000612783602083612bfc565b915061278e82613207565b602082019050919050565b60006127a6602083612bfc565b91506127b182613230565b602082019050919050565b60006127c9601883612bfc565b91506127d482613259565b602082019050919050565b60006127ec602183612bfc565b91506127f782613282565b604082019050919050565b600061280f603d83612bfc565b915061281a826132d1565b604082019050919050565b61282e81612d0c565b82525050565b600061284082856125c4565b915061284c82846125c4565b91508190509392505050565b600060208201905061286d6000830184612534565b92915050565b60006060820190506128886000830186612534565b6128956020830185612534565b6128a26040830184612825565b949350505050565b60006080820190506128bf6000830187612534565b6128cc6020830186612534565b6128d96040830185612825565b81810360608301526128eb8184612552565b905095945050505050565b600060208201905061290b6000830184612543565b92915050565b6000602082019050818103600083015261292b818461258b565b905092915050565b6000602082019050818103600083015261294c816125f5565b9050919050565b6000602082019050818103600083015261296c81612618565b9050919050565b6000602082019050818103600083015261298c8161263b565b9050919050565b600060208201905081810360008301526129ac8161265e565b9050919050565b600060208201905081810360008301526129cc81612681565b9050919050565b600060208201905081810360008301526129ec816126a4565b9050919050565b60006020820190508181036000830152612a0c816126c7565b9050919050565b60006020820190508181036000830152612a2c816126ea565b9050919050565b60006020820190508181036000830152612a4c8161270d565b9050919050565b60006020820190508181036000830152612a6c81612730565b9050919050565b60006020820190508181036000830152612a8c81612753565b9050919050565b60006020820190508181036000830152612aac81612776565b9050919050565b60006020820190508181036000830152612acc81612799565b9050919050565b60006020820190508181036000830152612aec816127bc565b9050919050565b60006020820190508181036000830152612b0c816127df565b9050919050565b60006020820190508181036000830152612b2c81612802565b9050919050565b6000602082019050612b486000830184612825565b92915050565b6000612b58612b69565b9050612b648282612d8a565b919050565b6000604051905090565b600067ffffffffffffffff821115612b8e57612b8d612ec0565b5b612b9782612f03565b9050602081019050919050565b600067ffffffffffffffff821115612bbf57612bbe612ec0565b5b612bc882612f03565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b6000612c2382612d0c565b9150612c2e83612d0c565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115612c6357612c62612e04565b5b828201905092915050565b6000612c7982612d0c565b9150612c8483612d0c565b925082821015612c9757612c96612e04565b5b828203905092915050565b6000612cad82612cec565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015612d43578082015181840152602081019050612d28565b83811115612d52576000848401525b50505050565b60006002820490506001821680612d7057607f821691505b60208210811415612d8457612d83612e62565b5b50919050565b612d9382612f03565b810181811067ffffffffffffffff82111715612db257612db1612ec0565b5b80604052505050565b6000612dc682612d0c565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff821415612df957612df8612e04565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f6d697373696e6720495046532075726c20666f7220746865206461746120697460008201527f656d000000000000000000000000000000000000000000000000000000000000602082015250565b7f4f6e6c792074686520646f63746f72206f72207468652070617469656e74206360008201527f616e207365652074686520555249000000000000000000000000000000000000602082015250565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206f7220617070726f76656400000000000000000000000000000000000000602082015250565b7f55524920717565727920666f72206e6f6e6578697374656e7420746f6b656e00600082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f45524337323155524953746f726167653a2055524920736574206f66206e6f6e60008201527f6578697374656e7420746f6b656e000000000000000000000000000000000000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206f7220617070726f76656420666f7220616c6c000000602082015250565b61332981612ca2565b811461333457600080fd5b50565b61334081612cb4565b811461334b57600080fd5b50565b61335781612cc0565b811461336257600080fd5b50565b61336e81612d0c565b811461337957600080fd5b5056fea26469706673582212203f5686751d6d2993a753cfb660962212b795813e90e938296cbf0c3cc8bec20564736f6c63430008070033"
