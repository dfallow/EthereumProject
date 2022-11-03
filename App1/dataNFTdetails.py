import json

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
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
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
		"name": "mint",
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
		"inputs": [],
		"name": "tokenCounter",
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
		"name": "tokenIdToURI",
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
	}
]""")


bytecode = "60806040523480156200001157600080fd5b506040518060400160405280600781526020017f446174614e4654000000000000000000000000000000000000000000000000008152506040518060400160405280600781526020017f444154414e465400000000000000000000000000000000000000000000000000815250816000908051906020019062000096929190620000c0565b508060019080519060200190620000af929190620000c0565b5050506000600681905550620001d5565b828054620000ce9062000170565b90600052602060002090601f016020900481019282620000f257600085556200013e565b82601f106200010d57805160ff19168380011785556200013e565b828001600101855582156200013e579182015b828111156200013d57825182559160200191906001019062000120565b5b5090506200014d919062000151565b5090565b5b808211156200016c57600081600090555060010162000152565b5090565b600060028204905060018216806200018957607f821691505b60208210811415620001a0576200019f620001a6565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b612f2d80620001e56000396000f3fe608060405234801561001057600080fd5b50600436106101215760003560e01c806370a08231116100ad578063a22cb46511610071578063a22cb46514610355578063b88d4fde14610371578063c87b56dd1461038d578063d082e381146103bd578063e985e9c5146103db57610121565b806370a082311461027657806395d89b41146102a6578063968a76cf146102c45780639ba41a65146102f5578063a1ab81661461032557610121565b8063095ea7b3116100f4578063095ea7b3146101d45780631249c58b146101f057806323b872dd1461020e57806342842e0e1461022a5780636352211e1461024657610121565b806301ffc9a7146101265780630221e7851461015657806306fdde0314610186578063081812fc146101a4575b600080fd5b610140600480360381019061013b9190612073565b61040b565b60405161014d9190612494565b60405180910390f35b610170600480360381019061016b9190612145565b6104ed565b60405161017d91906124af565b60405180910390f35b61018e61058d565b60405161019b91906124af565b60405180910390f35b6101be60048036038101906101b99190612145565b61061f565b6040516101cb919061242d565b60405180910390f35b6101ee60048036038101906101e99190612033565b610665565b005b6101f861077d565b60405161020591906126a8565b60405180910390f35b61022860048036038101906102239190611f1d565b6107a8565b005b610244600480360381019061023f9190611f1d565b610808565b005b610260600480360381019061025b9190612145565b610828565b60405161026d919061242d565b60405180910390f35b610290600480360381019061028b9190611eb0565b6108da565b60405161029d91906126a8565b60405180910390f35b6102ae610992565b6040516102bb91906124af565b60405180910390f35b6102de60048036038101906102d99190612145565b610a24565b6040516102ec9291906124d1565b60405180910390f35b61030f600480360381019061030a91906120cd565b610b68565b60405161031c91906124af565b60405180910390f35b61033f600480360381019061033a9190612145565b610c3b565b60405161034c919061242d565b60405180910390f35b61036f600480360381019061036a9190611ff3565b610c6e565b005b61038b60048036038101906103869190611f70565b610c84565b005b6103a760048036038101906103a29190612145565b610ce6565b6040516103b491906124af565b60405180910390f35b6103c5610d4e565b6040516103d291906126a8565b60405180910390f35b6103f560048036038101906103f09190611edd565b610d54565b6040516104029190612494565b60405180910390f35b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806104d657507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806104e657506104e582610de8565b5b9050919050565b6009602052806000526040600020600091509050805461050c90612943565b80601f016020809104026020016040519081016040528092919081815260200182805461053890612943565b80156105855780601f1061055a57610100808354040283529160200191610585565b820191906000526020600020905b81548152906001019060200180831161056857829003601f168201915b505050505081565b60606000805461059c90612943565b80601f01602080910402602001604051908101604052809291908181526020018280546105c890612943565b80156106155780601f106105ea57610100808354040283529160200191610615565b820191906000526020600020905b8154815290600101906020018083116105f857829003601f168201915b5050505050905090565b600061062a82610e52565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b600061067082610828565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614156106e1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106d890612668565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff16610700610e9d565b73ffffffffffffffffffffffffffffffffffffffff16148061072f575061072e81610729610e9d565b610d54565b5b61076e576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161076590612608565b60405180910390fd5b6107788383610ea5565b505050565b600061078b33600654610f5e565b600160065461079a91906127d2565b600681905550600654905090565b6107b96107b3610e9d565b82610f7c565b6107f8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107ef90612688565b60405180910390fd5b610803838383611011565b505050565b61082383838360405180602001604052806000815250610c84565b505050565b6000806002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156108d1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108c890612648565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141561094b576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610942906125e8565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b6060600180546109a190612943565b80601f01602080910402602001604051908101604052809291908181526020018280546109cd90612943565b8015610a1a5780601f106109ef57610100808354040283529160200191610a1a565b820191906000526020600020905b8154815290600101906020018083116109fd57829003601f168201915b5050505050905090565b60078181548110610a3457600080fd5b9060005260206000209060020201600091509050806000018054610a5790612943565b80601f0160208091040260200160405190810160405280929190818152602001828054610a8390612943565b8015610ad05780601f10610aa557610100808354040283529160200191610ad0565b820191906000526020600020905b815481529060010190602001808311610ab357829003601f168201915b505050505090806001018054610ae590612943565b80601f0160208091040260200160405190810160405280929190818152602001828054610b1190612943565b8015610b5e5780601f10610b3357610100808354040283529160200191610b5e565b820191906000526020600020905b815481529060010190602001808311610b4157829003601f168201915b5050505050905082565b60606000835111610bae576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ba5906125c8565b60405180910390fd5b6000825111610bf2576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610be990612508565b60405180910390fd5b610bfc8383611278565b506040518060400160405280600f81526020017f44617461206974656d2073617665640000000000000000000000000000000000815250905092915050565b60086020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b610c80610c79610e9d565b838361151e565b5050565b610c95610c8f610e9d565b83610f7c565b610cd4576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ccb90612688565b60405180910390fd5b610ce08484848461168b565b50505050565b6060610cf182610e52565b6000610cfb6116e7565b90506000815111610d1b5760405180602001604052806000815250610d46565b80610d25846116fe565b604051602001610d36929190612409565b6040516020818303038152906040525b915050919050565b60065481565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610e5b8161185f565b610e9a576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610e9190612648565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16610f1883610828565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b610f788282604051806020016040528060008152506118cb565b5050565b600080610f8883610828565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff161480610fca5750610fc98185610d54565b5b8061100857508373ffffffffffffffffffffffffffffffffffffffff16610ff08461061f565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff1661103182610828565b73ffffffffffffffffffffffffffffffffffffffff1614611087576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161107e90612548565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614156110f7576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016110ee90612588565b60405180910390fd5b611102838383611926565b61110d600082610ea5565b6001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461115d9190612859565b925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546111b491906127d2565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a461127383838361192b565b505050565b60606007604051806040016040528085815260200184815250908060018154018082558091505060019003906000526020600020906002020160009091909190915060008201518160000190805190602001906112d6929190611cc4565b5060208201518160010190805190602001906112f3929190611cc4565b5050506000600160078054905061130a9190612859565b9050336008600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507f6891983d42a48e510754f618abfbc8c414f4b10f9cf5d0f428133dbc60d5eb24818585604051611391939291906126c3565b60405180910390a16007805480602002602001604051908101604052809291908181526020016000905b8282101561151157838290600052602060002090600202016040518060400160405290816000820180546113ee90612943565b80601f016020809104026020016040519081016040528092919081815260200182805461141a90612943565b80156114675780601f1061143c57610100808354040283529160200191611467565b820191906000526020600020905b81548152906001019060200180831161144a57829003601f168201915b5050505050815260200160018201805461148090612943565b80601f01602080910402602001604051908101604052809291908181526020018280546114ac90612943565b80156114f95780601f106114ce576101008083540402835291602001916114f9565b820191906000526020600020905b8154815290600101906020018083116114dc57829003601f168201915b505050505081525050815260200190600101906113bb565b5050505091505092915050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141561158d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611584906125a8565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c318360405161167e9190612494565b60405180910390a3505050565b611696848484611011565b6116a284848484611930565b6116e1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016116d890612528565b60405180910390fd5b50505050565b606060405180602001604052806000815250905090565b60606000821415611746576040518060400160405280600181526020017f3000000000000000000000000000000000000000000000000000000000000000815250905061185a565b600082905060005b60008214611778578080611761906129a6565b915050600a826117719190612828565b915061174e565b60008167ffffffffffffffff81111561179457611793612adc565b5b6040519080825280601f01601f1916602001820160405280156117c65781602001600182028036833780820191505090505b5090505b60008514611853576001826117df9190612859565b9150600a856117ee91906129ef565b60306117fa91906127d2565b60f81b8183815181106118105761180f612aad565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600a8561184c9190612828565b94506117ca565b8093505050505b919050565b60008073ffffffffffffffffffffffffffffffffffffffff166002600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614159050919050565b6118d58383611ac7565b6118e26000848484611930565b611921576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161191890612528565b60405180910390fd5b505050565b505050565b505050565b60006119518473ffffffffffffffffffffffffffffffffffffffff16611ca1565b15611aba578373ffffffffffffffffffffffffffffffffffffffff1663150b7a0261197a610e9d565b8786866040518563ffffffff1660e01b815260040161199c9493929190612448565b602060405180830381600087803b1580156119b657600080fd5b505af19250505080156119e757506040513d601f19601f820116820180604052508101906119e491906120a0565b60015b611a6a573d8060008114611a17576040519150601f19603f3d011682016040523d82523d6000602084013e611a1c565b606091505b50600081511415611a62576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611a5990612528565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611abf565b600190505b949350505050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611b37576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611b2e90612628565b60405180910390fd5b611b408161185f565b15611b80576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611b7790612568565b60405180910390fd5b611b8c60008383611926565b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611bdc91906127d2565b92505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a4611c9d6000838361192b565b5050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b828054611cd090612943565b90600052602060002090601f016020900481019282611cf25760008555611d39565b82601f10611d0b57805160ff1916838001178555611d39565b82800160010185558215611d39579182015b82811115611d38578251825591602001919060010190611d1d565b5b509050611d469190611d4a565b5090565b5b80821115611d63576000816000905550600101611d4b565b5090565b6000611d7a611d758461272d565b612708565b905082815260208101848484011115611d9657611d95612b10565b5b611da1848285612901565b509392505050565b6000611dbc611db78461275e565b612708565b905082815260208101848484011115611dd857611dd7612b10565b5b611de3848285612901565b509392505050565b600081359050611dfa81612e9b565b92915050565b600081359050611e0f81612eb2565b92915050565b600081359050611e2481612ec9565b92915050565b600081519050611e3981612ec9565b92915050565b600082601f830112611e5457611e53612b0b565b5b8135611e64848260208601611d67565b91505092915050565b600082601f830112611e8257611e81612b0b565b5b8135611e92848260208601611da9565b91505092915050565b600081359050611eaa81612ee0565b92915050565b600060208284031215611ec657611ec5612b1a565b5b6000611ed484828501611deb565b91505092915050565b60008060408385031215611ef457611ef3612b1a565b5b6000611f0285828601611deb565b9250506020611f1385828601611deb565b9150509250929050565b600080600060608486031215611f3657611f35612b1a565b5b6000611f4486828701611deb565b9350506020611f5586828701611deb565b9250506040611f6686828701611e9b565b9150509250925092565b60008060008060808587031215611f8a57611f89612b1a565b5b6000611f9887828801611deb565b9450506020611fa987828801611deb565b9350506040611fba87828801611e9b565b925050606085013567ffffffffffffffff811115611fdb57611fda612b15565b5b611fe787828801611e3f565b91505092959194509250565b6000806040838503121561200a57612009612b1a565b5b600061201885828601611deb565b925050602061202985828601611e00565b9150509250929050565b6000806040838503121561204a57612049612b1a565b5b600061205885828601611deb565b925050602061206985828601611e9b565b9150509250929050565b60006020828403121561208957612088612b1a565b5b600061209784828501611e15565b91505092915050565b6000602082840312156120b6576120b5612b1a565b5b60006120c484828501611e2a565b91505092915050565b600080604083850312156120e4576120e3612b1a565b5b600083013567ffffffffffffffff81111561210257612101612b15565b5b61210e85828601611e6d565b925050602083013567ffffffffffffffff81111561212f5761212e612b15565b5b61213b85828601611e6d565b9150509250929050565b60006020828403121561215b5761215a612b1a565b5b600061216984828501611e9b565b91505092915050565b61217b8161288d565b82525050565b61218a8161289f565b82525050565b600061219b8261278f565b6121a581856127a5565b93506121b5818560208601612910565b6121be81612b1f565b840191505092915050565b60006121d48261279a565b6121de81856127b6565b93506121ee818560208601612910565b6121f781612b1f565b840191505092915050565b600061220d8261279a565b61221781856127c7565b9350612227818560208601612910565b80840191505092915050565b60006122406022836127b6565b915061224b82612b30565b604082019050919050565b60006122636032836127b6565b915061226e82612b7f565b604082019050919050565b60006122866025836127b6565b915061229182612bce565b604082019050919050565b60006122a9601c836127b6565b91506122b482612c1d565b602082019050919050565b60006122cc6024836127b6565b91506122d782612c46565b604082019050919050565b60006122ef6019836127b6565b91506122fa82612c95565b602082019050919050565b60006123126023836127b6565b915061231d82612cbe565b604082019050919050565b60006123356029836127b6565b915061234082612d0d565b604082019050919050565b6000612358603e836127b6565b915061236382612d5c565b604082019050919050565b600061237b6020836127b6565b915061238682612dab565b602082019050919050565b600061239e6018836127b6565b91506123a982612dd4565b602082019050919050565b60006123c16021836127b6565b91506123cc82612dfd565b604082019050919050565b60006123e4602e836127b6565b91506123ef82612e4c565b604082019050919050565b612403816128f7565b82525050565b60006124158285612202565b91506124218284612202565b91508190509392505050565b60006020820190506124426000830184612172565b92915050565b600060808201905061245d6000830187612172565b61246a6020830186612172565b61247760408301856123fa565b81810360608301526124898184612190565b905095945050505050565b60006020820190506124a96000830184612181565b92915050565b600060208201905081810360008301526124c981846121c9565b905092915050565b600060408201905081810360008301526124eb81856121c9565b905081810360208301526124ff81846121c9565b90509392505050565b6000602082019050818103600083015261252181612233565b9050919050565b6000602082019050818103600083015261254181612256565b9050919050565b6000602082019050818103600083015261256181612279565b9050919050565b600060208201905081810360008301526125818161229c565b9050919050565b600060208201905081810360008301526125a1816122bf565b9050919050565b600060208201905081810360008301526125c1816122e2565b9050919050565b600060208201905081810360008301526125e181612305565b9050919050565b6000602082019050818103600083015261260181612328565b9050919050565b600060208201905081810360008301526126218161234b565b9050919050565b600060208201905081810360008301526126418161236e565b9050919050565b6000602082019050818103600083015261266181612391565b9050919050565b60006020820190508181036000830152612681816123b4565b9050919050565b600060208201905081810360008301526126a1816123d7565b9050919050565b60006020820190506126bd60008301846123fa565b92915050565b60006060820190506126d860008301866123fa565b81810360208301526126ea81856121c9565b905081810360408301526126fe81846121c9565b9050949350505050565b6000612712612723565b905061271e8282612975565b919050565b6000604051905090565b600067ffffffffffffffff82111561274857612747612adc565b5b61275182612b1f565b9050602081019050919050565b600067ffffffffffffffff82111561277957612778612adc565b5b61278282612b1f565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b60006127dd826128f7565b91506127e8836128f7565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0382111561281d5761281c612a20565b5b828201905092915050565b6000612833826128f7565b915061283e836128f7565b92508261284e5761284d612a4f565b5b828204905092915050565b6000612864826128f7565b915061286f836128f7565b92508282101561288257612881612a20565b5b828203905092915050565b6000612898826128d7565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b8381101561292e578082015181840152602081019050612913565b8381111561293d576000848401525b50505050565b6000600282049050600182168061295b57607f821691505b6020821081141561296f5761296e612a7e565b5b50919050565b61297e82612b1f565b810181811067ffffffffffffffff8211171561299d5761299c612adc565b5b80604052505050565b60006129b1826128f7565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156129e4576129e3612a20565b5b600182019050919050565b60006129fa826128f7565b9150612a05836128f7565b925082612a1557612a14612a4f565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f6d697373696e6720495046532075726c20666f7220746865206461746120697460008201527f656d000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f6d697373696e672049504653206861736820666f72207468652064617461206960008201527f74656d0000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206e6f7220617070726f76656420666f7220616c6c0000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206e6f7220617070726f766564000000000000000000000000000000000000602082015250565b612ea48161288d565b8114612eaf57600080fd5b50565b612ebb8161289f565b8114612ec657600080fd5b50565b612ed2816128ab565b8114612edd57600080fd5b50565b612ee9816128f7565b8114612ef457600080fd5b5056fea26469706673582212208d1f58da9a845c8720e12e8eb63762a4cadb9dda8fb3fabb23f8823e751622ba64736f6c63430008070033"
