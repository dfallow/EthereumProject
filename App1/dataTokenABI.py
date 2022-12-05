import json

abi = json.loads("""[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "doctorAddress",
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
				"name": "newDoctor",
				"type": "address"
			}
		],
		"name": "changeDoctor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
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
		"name": "ContractOwnershipChanged",
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
		"name": "DataSaved",
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
		"name": "DoctorChanged",
		"type": "event"
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
			},
			{
				"internalType": "uint256",
				"name": "prescriptionTokenId",
				"type": "uint256"
			}
		],
		"name": "mintDataToken",
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
				"name": "nftId",
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
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"name": "TokenOwnershipChanged",
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
		"inputs": [],
		"name": "_doctor",
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
		"name": "_numberOfDataTokens",
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
				"internalType": "uint256[]",
				"name": "tokenIdArray",
				"type": "uint256[]"
			}
		],
		"name": "transferTokenOwnership",
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
		"name": "dataItems",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "dataTokenId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "machineTokenId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "prescriptionTokenId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "dataIpfsURL",
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
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getDataItemForToken",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "dataTokenId",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "machineTokenId",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "prescriptionTokenId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "dataIpfsURL",
						"type": "string"
					}
				],
				"internalType": "struct DataToken.DataItem",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getDoctor",
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
		"name": "numberOfDataTokens",
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
	}
]""")

bytecode = "60806040523480156200001157600080fd5b50604051620036a5380380620036a58339818101604052810190620000379190620002e5565b6040518060400160405280600981526020017f44617461546f6b656e00000000000000000000000000000000000000000000008152506040518060400160405280600381526020017f44544b00000000000000000000000000000000000000000000000000000000008152508160009080519060200190620000bb9291906200021e565b508060019080519060200190620000d49291906200021e565b505050620000f7620000eb6200015060201b60201c565b6200015860201b60201c565b62000108336200015860201b60201c565b80600960006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050620003cf565b600033905090565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8280546200022c906200034b565b90600052602060002090601f0160209004810192826200025057600085556200029c565b82601f106200026b57805160ff19168380011785556200029c565b828001600101855582156200029c579182015b828111156200029b5782518255916020019190600101906200027e565b5b509050620002ab9190620002af565b5090565b5b80821115620002ca576000816000905550600101620002b0565b5090565b600081519050620002df81620003b5565b92915050565b600060208284031215620002fe57620002fd620003b0565b5b60006200030e84828501620002ce565b91505092915050565b600062000324826200032b565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600060028204905060018216806200036457607f821691505b602082108114156200037b576200037a62000381565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600080fd5b620003c08162000317565b8114620003cc57600080fd5b50565b6132c680620003df6000396000f3fe608060405234801561001057600080fd5b50600436106101585760003560e01c80636352211e116100c3578063a22cb4651161007c578063a22cb465146103dc578063a85ea054146103f8578063b88d4fde14610416578063c87b56dd14610432578063e985e9c514610462578063f2fde38b1461049257610158565b80636352211e1461030357806370a0823114610333578063715018a6146103635780638da5cb5b1461036d57806395d89b411461038b578063968a76cf146103a957610158565b80631e0a1938116101155780631e0a19381461024357806323b872dd146102735780633aaa59201461028f5780633adb725f146102ad5780633cffdbff146102c957806342842e0e146102e757610158565b806301ffc9a71461015d578063064c4c9c1461018d57806306fdde03146101a957806306ff2d58146101c7578063081812fc146101f7578063095ea7b314610227575b600080fd5b61017760048036038101906101729190612336565b6104ae565b60405161018491906127f9565b60405180910390f35b6101a760048036038101906101a2919061225a565b610590565b005b6101b1610619565b6040516101be9190612814565b60405180910390f35b6101e160048036038101906101dc9190612390565b6106ab565b6040516101ee91906129f8565b60405180910390f35b610211600480360381019061020c91906123ff565b610793565b60405161021e9190612792565b60405180910390f35b610241600480360381019061023c91906122f6565b6107d9565b005b61025d600480360381019061025891906123ff565b6108f1565b60405161026a91906129d6565b60405180910390f35b61028d60048036038101906102889190612184565b610a8b565b005b610297610ac8565b6040516102a49190612792565b60405180910390f35b6102c760048036038101906102c29190612117565b610afa565b005b6102d1610b7e565b6040516102de91906129f8565b60405180910390f35b61030160048036038101906102fc9190612184565b610b84565b005b61031d600480360381019061031891906123ff565b610bc1565b60405161032a9190612792565b60405180910390f35b61034d60048036038101906103489190612117565b610c73565b60405161035a91906129f8565b60405180910390f35b61036b610d2b565b005b610375610d3f565b6040516103829190612792565b60405180910390f35b610393610d69565b6040516103a09190612814565b60405180910390f35b6103c360048036038101906103be91906123ff565b610dfb565b6040516103d39493929190612a13565b60405180910390f35b6103f660048036038101906103f191906122b6565b610ec3565b005b610400610ed9565b60405161040d9190612792565b60405180910390f35b610430600480360381019061042b91906121d7565b610eff565b005b61044c600480360381019061044791906123ff565b610f3d565b6040516104599190612814565b60405180910390f35b61047c60048036038101906104779190612144565b6110ae565b60405161048991906127f9565b60405180910390f35b6104ac60048036038101906104a79190612117565b611142565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061057957507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b80610589575061058882611185565b5b9050919050565b6105986111ef565b60005b81518110156105dc576105c933848484815181106105bc576105bb612e41565b5b6020026020010151610b84565b80806105d490612d3a565b91505061059b565b507f01d219a674d05d7b2f41665d1bc9016744ecbb0f9b5c155fc62655ddc3311b96600160405161060d91906127f9565b60405180910390a15050565b60606000805461062890612cd7565b80601f016020809104026020016040519081016040528092919081815260200182805461065490612cd7565b80156106a15780601f10610676576101008083540402835291602001916106a1565b820191906000526020600020905b81548152906001019060200180831161068457829003601f168201915b5050505050905090565b60006106b56111ef565b60008451116106f9576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106f090612836565b60405180910390fd5b60016008600082825461070c9190612b66565b9250508190555060006008549050610724338261126d565b61072e818661128b565b3373ffffffffffffffffffffffffffffffffffffffff167f30385c845b448a36257a6a1716e6ad2e1bc2cbe333cde1e69fe849ad6511adfe8260405161077491906129f8565b60405180910390a2610788818585886112ff565b809150509392505050565b600061079e826113ce565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b60006107e482610bc1565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415610855576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161084c906129b6565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff16610874611419565b73ffffffffffffffffffffffffffffffffffffffff1614806108a357506108a28161089d611419565b6110ae565b5b6108e2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108d990612936565b60405180910390fd5b6108ec8383611421565b505050565b6108f9611e65565b6109016111ef565b61090a826114da565b610949576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161094090612856565b60405180910390fd5b60005b600a80549050811015610a845782600a828154811061096e5761096d612e41565b5b9060005260206000209060040201600001541415610a71576000600a828154811061099c5761099b612e41565b5b90600052602060002090600402019050806040518060800160405290816000820154815260200160018201548152602001600282015481526020016003820180546109e690612cd7565b80601f0160208091040260200160405190810160405280929190818152602001828054610a1290612cd7565b8015610a5f5780601f10610a3457610100808354040283529160200191610a5f565b820191906000526020600020905b815481529060010190602001808311610a4257829003601f168201915b50505050508152505092505050610a86565b8080610a7c90612d3a565b91505061094c565b505b919050565b7f01d219a674d05d7b2f41665d1bc9016744ecbb0f9b5c155fc62655ddc3311b966000604051610abb91906127f9565b60405180910390a1505050565b6000610ad26111ef565b600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b610b026111ef565b80600960006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507f7c23bab3b34d1fb709f1c79112a4c71361c411e0008c57b48a0bcba1de5e6f466001604051610b7391906127f9565b60405180910390a150565b60085481565b7f01d219a674d05d7b2f41665d1bc9016744ecbb0f9b5c155fc62655ddc3311b966000604051610bb491906127f9565b60405180910390a1505050565b6000806002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415610c6a576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610c6190612996565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415610ce4576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610cdb906128f6565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b610d336111ef565b610d3d6000611546565b565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b606060018054610d7890612cd7565b80601f0160208091040260200160405190810160405280929190818152602001828054610da490612cd7565b8015610df15780601f10610dc657610100808354040283529160200191610df1565b820191906000526020600020905b815481529060010190602001808311610dd457829003601f168201915b5050505050905090565b600a8181548110610e0b57600080fd5b9060005260206000209060040201600091509050806000015490806001015490806002015490806003018054610e4090612cd7565b80601f0160208091040260200160405190810160405280929190818152602001828054610e6c90612cd7565b8015610eb95780601f10610e8e57610100808354040283529160200191610eb9565b820191906000526020600020905b815481529060010190602001808311610e9c57829003601f168201915b5050505050905084565b610ed5610ece611419565b838361160c565b5050565b600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b7f01d219a674d05d7b2f41665d1bc9016744ecbb0f9b5c155fc62655ddc3311b966000604051610f2f91906127f9565b60405180910390a150505050565b6060610f48826114da565b610f87576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610f7e90612856565b60405180910390fd5b6000610f91610d3f565b90506000610f9e84610bc1565b90508173ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614806110275750600960009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16145b8061105d57508073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16145b61109c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611093906128d6565b60405180910390fd5b6110a584611779565b92505050919050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b61114a6111ef565b7f05654f36e2550343773cc40980261000be3091f4642ecb17b89d3fc29d3aec81600060405161117a91906127f9565b60405180910390a150565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b6111f7611419565b73ffffffffffffffffffffffffffffffffffffffff16611215610d3f565b73ffffffffffffffffffffffffffffffffffffffff161461126b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161126290612976565b60405180910390fd5b565b61128782826040518060200160405280600081525061188c565b5050565b611294826114da565b6112d3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016112ca90612916565b60405180910390fd5b806006600084815260200190815260200160002090805190602001906112fa929190611e8d565b505050565b6113076111ef565b600a6040518060800160405280868152602001858152602001848152602001838152509080600181540180825580915050600190039060005260206000209060040201600090919091909150600082015181600001556020820151816001015560408201518160020155606082015181600301908051906020019061138d929190611e8d565b5050507f94664aaa7bd5908cb6951b3228ee44bafa43ac0c3faea16ad8926065c3d8d05560016040516113c091906127f9565b60405180910390a150505050565b6113d7816114da565b611416576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161140d90612996565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff1661149483610bc1565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b60008073ffffffffffffffffffffffffffffffffffffffff166002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614159050919050565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141561167b576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611672906128b6565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c318360405161176c91906127f9565b60405180910390a3505050565b6060611784826113ce565b60006006600084815260200190815260200160002080546117a490612cd7565b80601f01602080910402602001604051908101604052809291908181526020018280546117d090612cd7565b801561181d5780601f106117f25761010080835404028352916020019161181d565b820191906000526020600020905b81548152906001019060200180831161180057829003601f168201915b50505050509050600061182e6118e7565b9050600081511415611844578192505050611887565b60008251111561187957808260405160200161186192919061276e565b60405160208183030381529060405292505050611887565b611882846118fe565b925050505b919050565b6118968383611966565b6118a36000848484611b40565b6118e2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016118d990612876565b60405180910390fd5b505050565b606060405180602001604052806000815250905090565b6060611909826113ce565b60006119136118e7565b90506000815111611933576040518060200160405280600081525061195e565b8061193d84611cd7565b60405160200161194e92919061276e565b6040516020818303038152906040525b915050919050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614156119d6576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016119cd90612956565b60405180910390fd5b6119df816114da565b15611a1f576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611a1690612896565b60405180910390fd5b611a2b60008383611e38565b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611a7b9190612b66565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a4611b3c60008383611e3d565b5050565b6000611b618473ffffffffffffffffffffffffffffffffffffffff16611e42565b15611cca578373ffffffffffffffffffffffffffffffffffffffff1663150b7a02611b8a611419565b8786866040518563ffffffff1660e01b8152600401611bac94939291906127ad565b602060405180830381600087803b158015611bc657600080fd5b505af1925050508015611bf757506040513d601f19601f82011682018060405250810190611bf49190612363565b60015b611c7a573d8060008114611c27576040519150601f19603f3d011682016040523d82523d6000602084013e611c2c565b606091505b50600081511415611c72576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611c6990612876565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611ccf565b600190505b949350505050565b60606000821415611d1f576040518060400160405280600181526020017f30000000000000000000000000000000000000000000000000000000000000008152509050611e33565b600082905060005b60008214611d51578080611d3a90612d3a565b915050600a82611d4a9190612bbc565b9150611d27565b60008167ffffffffffffffff811115611d6d57611d6c612e70565b5b6040519080825280601f01601f191660200182016040528015611d9f5781602001600182028036833780820191505090505b5090505b60008514611e2c57600182611db89190612bed565b9150600a85611dc79190612d83565b6030611dd39190612b66565b60f81b818381518110611de957611de8612e41565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600a85611e259190612bbc565b9450611da3565b8093505050505b919050565b505050565b505050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b6040518060800160405280600081526020016000815260200160008152602001606081525090565b828054611e9990612cd7565b90600052602060002090601f016020900481019282611ebb5760008555611f02565b82601f10611ed457805160ff1916838001178555611f02565b82800160010185558215611f02579182015b82811115611f01578251825591602001919060010190611ee6565b5b509050611f0f9190611f13565b5090565b5b80821115611f2c576000816000905550600101611f14565b5090565b6000611f43611f3e84612a84565b612a5f565b90508083825260208201905082856020860282011115611f6657611f65612ea4565b5b60005b85811015611f965781611f7c8882612102565b845260208401935060208301925050600181019050611f69565b5050509392505050565b6000611fb3611fae84612ab0565b612a5f565b905082815260208101848484011115611fcf57611fce612ea9565b5b611fda848285612c95565b509392505050565b6000611ff5611ff084612ae1565b612a5f565b90508281526020810184848401111561201157612010612ea9565b5b61201c848285612c95565b509392505050565b60008135905061203381613234565b92915050565b600082601f83011261204e5761204d612e9f565b5b813561205e848260208601611f30565b91505092915050565b6000813590506120768161324b565b92915050565b60008135905061208b81613262565b92915050565b6000815190506120a081613262565b92915050565b600082601f8301126120bb576120ba612e9f565b5b81356120cb848260208601611fa0565b91505092915050565b600082601f8301126120e9576120e8612e9f565b5b81356120f9848260208601611fe2565b91505092915050565b60008135905061211181613279565b92915050565b60006020828403121561212d5761212c612eb3565b5b600061213b84828501612024565b91505092915050565b6000806040838503121561215b5761215a612eb3565b5b600061216985828601612024565b925050602061217a85828601612024565b9150509250929050565b60008060006060848603121561219d5761219c612eb3565b5b60006121ab86828701612024565b93505060206121bc86828701612024565b92505060406121cd86828701612102565b9150509250925092565b600080600080608085870312156121f1576121f0612eb3565b5b60006121ff87828801612024565b945050602061221087828801612024565b935050604061222187828801612102565b925050606085013567ffffffffffffffff81111561224257612241612eae565b5b61224e878288016120a6565b91505092959194509250565b6000806040838503121561227157612270612eb3565b5b600061227f85828601612024565b925050602083013567ffffffffffffffff8111156122a05761229f612eae565b5b6122ac85828601612039565b9150509250929050565b600080604083850312156122cd576122cc612eb3565b5b60006122db85828601612024565b92505060206122ec85828601612067565b9150509250929050565b6000806040838503121561230d5761230c612eb3565b5b600061231b85828601612024565b925050602061232c85828601612102565b9150509250929050565b60006020828403121561234c5761234b612eb3565b5b600061235a8482850161207c565b91505092915050565b60006020828403121561237957612378612eb3565b5b600061238784828501612091565b91505092915050565b6000806000606084860312156123a9576123a8612eb3565b5b600084013567ffffffffffffffff8111156123c7576123c6612eae565b5b6123d3868287016120d4565b93505060206123e486828701612102565b92505060406123f586828701612102565b9150509250925092565b60006020828403121561241557612414612eb3565b5b600061242384828501612102565b91505092915050565b61243581612c21565b82525050565b61244481612c33565b82525050565b600061245582612b12565b61245f8185612b28565b935061246f818560208601612ca4565b61247881612eb8565b840191505092915050565b600061248e82612b1d565b6124988185612b39565b93506124a8818560208601612ca4565b6124b181612eb8565b840191505092915050565b60006124c782612b1d565b6124d18185612b4a565b93506124e1818560208601612ca4565b6124ea81612eb8565b840191505092915050565b600061250082612b1d565b61250a8185612b5b565b935061251a818560208601612ca4565b80840191505092915050565b6000612533602283612b4a565b915061253e82612ec9565b604082019050919050565b6000612556601f83612b4a565b915061256182612f18565b602082019050919050565b6000612579603283612b4a565b915061258482612f41565b604082019050919050565b600061259c601c83612b4a565b91506125a782612f90565b602082019050919050565b60006125bf601983612b4a565b91506125ca82612fb9565b602082019050919050565b60006125e2606183612b4a565b91506125ed82612fe2565b608082019050919050565b6000612605602983612b4a565b91506126108261307d565b604082019050919050565b6000612628602e83612b4a565b9150612633826130cc565b604082019050919050565b600061264b603e83612b4a565b91506126568261311b565b604082019050919050565b600061266e602083612b4a565b91506126798261316a565b602082019050919050565b6000612691602083612b4a565b915061269c82613193565b602082019050919050565b60006126b4601883612b4a565b91506126bf826131bc565b602082019050919050565b60006126d7602183612b4a565b91506126e2826131e5565b604082019050919050565b60006080830160008301516127056000860182612750565b5060208301516127186020860182612750565b50604083015161272b6040860182612750565b50606083015184820360608601526127438282612483565b9150508091505092915050565b61275981612c8b565b82525050565b61276881612c8b565b82525050565b600061277a82856124f5565b915061278682846124f5565b91508190509392505050565b60006020820190506127a7600083018461242c565b92915050565b60006080820190506127c2600083018761242c565b6127cf602083018661242c565b6127dc604083018561275f565b81810360608301526127ee818461244a565b905095945050505050565b600060208201905061280e600083018461243b565b92915050565b6000602082019050818103600083015261282e81846124bc565b905092915050565b6000602082019050818103600083015261284f81612526565b9050919050565b6000602082019050818103600083015261286f81612549565b9050919050565b6000602082019050818103600083015261288f8161256c565b9050919050565b600060208201905081810360008301526128af8161258f565b9050919050565b600060208201905081810360008301526128cf816125b2565b9050919050565b600060208201905081810360008301526128ef816125d5565b9050919050565b6000602082019050818103600083015261290f816125f8565b9050919050565b6000602082019050818103600083015261292f8161261b565b9050919050565b6000602082019050818103600083015261294f8161263e565b9050919050565b6000602082019050818103600083015261296f81612661565b9050919050565b6000602082019050818103600083015261298f81612684565b9050919050565b600060208201905081810360008301526129af816126a7565b9050919050565b600060208201905081810360008301526129cf816126ca565b9050919050565b600060208201905081810360008301526129f081846126ed565b905092915050565b6000602082019050612a0d600083018461275f565b92915050565b6000608082019050612a28600083018761275f565b612a35602083018661275f565b612a42604083018561275f565b8181036060830152612a5481846124bc565b905095945050505050565b6000612a69612a7a565b9050612a758282612d09565b919050565b6000604051905090565b600067ffffffffffffffff821115612a9f57612a9e612e70565b5b602082029050602081019050919050565b600067ffffffffffffffff821115612acb57612aca612e70565b5b612ad482612eb8565b9050602081019050919050565b600067ffffffffffffffff821115612afc57612afb612e70565b5b612b0582612eb8565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b6000612b7182612c8b565b9150612b7c83612c8b565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115612bb157612bb0612db4565b5b828201905092915050565b6000612bc782612c8b565b9150612bd283612c8b565b925082612be257612be1612de3565b5b828204905092915050565b6000612bf882612c8b565b9150612c0383612c8b565b925082821015612c1657612c15612db4565b5b828203905092915050565b6000612c2c82612c6b565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015612cc2578082015181840152602081019050612ca7565b83811115612cd1576000848401525b50505050565b60006002820490506001821680612cef57607f821691505b60208210811415612d0357612d02612e12565b5b50919050565b612d1282612eb8565b810181811067ffffffffffffffff82111715612d3157612d30612e70565b5b80604052505050565b6000612d4582612c8b565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff821415612d7857612d77612db4565b5b600182019050919050565b6000612d8e82612c8b565b9150612d9983612c8b565b925082612da957612da8612de3565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f6d697373696e6720495046532075726c20666f7220746865206461746120697460008201527f656d000000000000000000000000000000000000000000000000000000000000602082015250565b7f55524920717565727920666f72206e6f6e6578697374656e7420746f6b656e00600082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f4f6e6c7920746865206f776e6572206f6620646174612028746865207061746960008201527f656e742f736f6d656f6e652077686f20626f7567687420697429206f7220746860208201527f6520646f63746f72206f662070617469656e742063616e20766965772064617460408201527f6100000000000000000000000000000000000000000000000000000000000000606082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f45524337323155524953746f726167653a2055524920736574206f66206e6f6e60008201527f6578697374656e7420746f6b656e000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206e6f7220617070726f76656420666f7220616c6c0000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b61323d81612c21565b811461324857600080fd5b50565b61325481612c33565b811461325f57600080fd5b50565b61326b81612c3f565b811461327657600080fd5b50565b61328281612c8b565b811461328d57600080fd5b5056fea2646970667358221220191202708a78bd316ef71eff6c118dce9145cea6c1017fc79f0fa77f373ab40064736f6c63430008070033"