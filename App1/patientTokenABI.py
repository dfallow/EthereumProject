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
				"name": "patient",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "prescriptionContract",
				"type": "address"
			}
		],
		"name": "addNewPatient",
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
				"internalType": "address",
				"name": "patient",
				"type": "address"
			}
		],
		"name": "checkIfPatientExists",
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
				"name": "patient",
				"type": "address"
			}
		],
		"name": "getPatient",
		"outputs": [
			{
				"internalType": "address",
				"name": "dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "prescriptionContract",
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
			}
		],
		"name": "mintPatientToken",
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

bytecode = "60806040526000600960006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055503480156200005357600080fd5b506040518060400160405280600c81526020017f50617469656e74546f6b656e00000000000000000000000000000000000000008152506040518060400160405280600381526020017f50544b00000000000000000000000000000000000000000000000000000000008152508160009080519060200190620000d8929190620001f9565b508060019080519060200190620000f1929190620001f9565b50505062000114620001086200012b60201b60201c565b6200013360201b60201c565b62000125336200013360201b60201c565b6200030e565b600033905090565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8280546200020790620002a9565b90600052602060002090601f0160209004810192826200022b576000855562000277565b82601f106200024657805160ff191683800117855562000277565b8280016001018555821562000277579182015b828111156200027657825182559160200191906001019062000259565b5b5090506200028691906200028a565b5090565b5b80821115620002a55760008160009055506001016200028b565b5090565b60006002820490506001821680620002c257607f821691505b60208210811415620002d957620002d8620002df565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b61335e806200031e6000396000f3fe608060405234801561001057600080fd5b506004361061012c5760003560e01c80638da5cb5b116100ad578063c87b56dd11610071578063c87b56dd14610342578063c8f0096a14610372578063e87ab7fe146103a2578063e985e9c5146103be578063f2fde38b146103ee5761012c565b80638da5cb5b1461029d57806395d89b41146102bb578063a22cb465146102d9578063b5368e20146102f5578063b88d4fde146103265761012c565b80634119330e116100f45780634119330e146101e757806342842e0e146102175780636352211e1461023357806370a0823114610263578063715018a6146102935761012c565b806301ffc9a71461013157806306fdde0314610161578063081812fc1461017f578063095ea7b3146101af57806323b872dd146101cb575b600080fd5b61014b60048036038101906101469190612542565b61040a565b6040516101589190612980565b60405180910390f35b6101696104ec565b604051610176919061299b565b60405180910390f35b610199600480360381019061019491906125e5565b61057e565b6040516101a691906128f0565b60405180910390f35b6101c960048036038101906101c49190612502565b6105c4565b005b6101e560048036038101906101e091906123ec565b6106dc565b005b61020160048036038101906101fc919061259c565b61073c565b60405161020e9190612b7d565b60405180910390f35b610231600480360381019061022c91906123ec565b610816565b005b61024d600480360381019061024891906125e5565b610836565b60405161025a91906128f0565b60405180910390f35b61027d6004803603810190610278919061232c565b6108bd565b60405161028a9190612b7d565b60405180910390f35b61029b610975565b005b6102a5610989565b6040516102b291906128f0565b60405180910390f35b6102c36109b3565b6040516102d0919061299b565b60405180910390f35b6102f360048036038101906102ee91906124c2565b610a45565b005b61030f600480360381019061030a919061232c565b610a5b565b60405161031d92919061290b565b60405180910390f35b610340600480360381019061033b919061243f565b610b84565b005b61035c600480360381019061035791906125e5565b610be6565b604051610369919061299b565b60405180910390f35b61038c6004803603810190610387919061232c565b610c00565b6040516103999190612980565b60405180910390f35b6103bc60048036038101906103b79190612399565b610cb6565b005b6103d860048036038101906103d39190612359565b610e22565b6040516103e59190612980565b60405180910390f35b6104086004803603810190610403919061232c565b610eb6565b005b60007f80ac58cd000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806104d557507f5b5e139f000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b806104e557506104e482610f02565b5b9050919050565b6060600080546104fb90612da2565b80601f016020809104026020016040519081016040528092919081815260200182805461052790612da2565b80156105745780601f1061054957610100808354040283529160200191610574565b820191906000526020600020905b81548152906001019060200180831161055757829003601f168201915b5050505050905090565b600061058982610f6c565b6004600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b60006105cf82610836565b90508073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415610640576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161063790612b1d565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1661065f610fb7565b73ffffffffffffffffffffffffffffffffffffffff16148061068e575061068d81610688610fb7565b610e22565b5b6106cd576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106c490612b3d565b60405180910390fd5b6106d78383610fbf565b505050565b6106ed6106e7610fb7565b82611078565b61072c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610723906129bd565b60405180910390fd5b61073783838361110d565b505050565b6000610746611407565b600082511161078a576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161078190612b5d565b60405180910390fd5b60016008600082825461079d9190612c62565b92505081905550600060085490506107b53382611485565b6107bf81846114a3565b3373ffffffffffffffffffffffffffffffffffffffff167f30385c845b448a36257a6a1716e6ad2e1bc2cbe333cde1e69fe849ad6511adfe826040516108059190612b7d565b60405180910390a280915050919050565b61083183838360405180602001604052806000815250610b84565b505050565b60008061084283611517565b9050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614156108b4576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108ab90612afd565b60405180910390fd5b80915050919050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141561092e576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161092590612a7d565b60405180910390fd5b600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b61097d611407565b6109876000611554565b565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b6060600180546109c290612da2565b80601f01602080910402602001604051908101604052809291908181526020018280546109ee90612da2565b8015610a3b5780601f10610a1057610100808354040283529160200191610a3b565b820191906000526020600020905b815481529060010190602001808311610a1e57829003601f168201915b5050505050905090565b610a57610a50610fb7565b838361161a565b5050565b600080610a66611407565b60005b600a80549050811015610b7d578373ffffffffffffffffffffffffffffffffffffffff16600a8281548110610aa157610aa0612edb565b5b906000526020600020906003020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610b6a576000600a8281548110610b0557610b04612edb565b5b906000526020600020906003020190508060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168160020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16935093505050610b7f565b8080610b7590612e05565b915050610a69565b505b915091565b610b95610b8f610fb7565b83611078565b610bd4576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610bcb906129bd565b60405180910390fd5b610be084848484611787565b50505050565b6060610bf0611407565b610bf9826117e3565b9050919050565b6000610c0a611407565b6000805b600a80549050811015610cac578373ffffffffffffffffffffffffffffffffffffffff16600a8281548110610c4657610c45612edb565b5b906000526020600020906003020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610c9957600191505b8080610ca490612e05565b915050610c0e565b5080915050919050565b610cbe611407565b600a60405180606001604052808573ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff16815250908060018154018082558091505060019003906000526020600020906003020160009091909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060408201518160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505050505050565b6000600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b610ebe611407565b610ec781611554565b7f05654f36e2550343773cc40980261000be3091f4642ecb17b89d3fc29d3aec816000604051610ef79190612980565b60405180910390a150565b60007f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b610f75816118f6565b610fb4576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610fab90612afd565b60405180910390fd5b50565b600033905090565b816004600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff1661103283610836565b73ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560405160405180910390a45050565b60008061108483610836565b90508073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff1614806110c657506110c58185610e22565b5b8061110457508373ffffffffffffffffffffffffffffffffffffffff166110ec8461057e565b73ffffffffffffffffffffffffffffffffffffffff16145b91505092915050565b8273ffffffffffffffffffffffffffffffffffffffff1661112d82610836565b73ffffffffffffffffffffffffffffffffffffffff1614611183576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161117a906129fd565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614156111f3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111ea90612a3d565b60405180910390fd5b6112008383836001611937565b8273ffffffffffffffffffffffffffffffffffffffff1661122082610836565b73ffffffffffffffffffffffffffffffffffffffff1614611276576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161126d906129fd565b60405180910390fd5b6004600082815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055506001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a46114028383836001611a5d565b505050565b61140f610fb7565b73ffffffffffffffffffffffffffffffffffffffff1661142d610989565b73ffffffffffffffffffffffffffffffffffffffff1614611483576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161147a90612add565b60405180910390fd5b565b61149f828260405180602001604052806000815250611a63565b5050565b6114ac826118f6565b6114eb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016114e290612a9d565b60405180910390fd5b80600660008481526020019081526020016000209080519060200190611512929190612140565b505050565b60006002600083815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6000600760009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905081600760006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a35050565b8173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415611689576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161168090612a5d565b60405180910390fd5b80600560008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c318360405161177a9190612980565b60405180910390a3505050565b61179284848461110d565b61179e84848484611abe565b6117dd576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016117d4906129dd565b60405180910390fd5b50505050565b60606117ee82610f6c565b600060066000848152602001908152602001600020805461180e90612da2565b80601f016020809104026020016040519081016040528092919081815260200182805461183a90612da2565b80156118875780601f1061185c57610100808354040283529160200191611887565b820191906000526020600020905b81548152906001019060200180831161186a57829003601f168201915b505050505090506000611898611c55565b90506000815114156118ae5781925050506118f1565b6000825111156118e35780826040516020016118cb9291906128cc565b604051602081830303815290604052925050506118f1565b6118ec84611c6c565b925050505b919050565b60008073ffffffffffffffffffffffffffffffffffffffff1661191883611517565b73ffffffffffffffffffffffffffffffffffffffff1614159050919050565b6001811115611a5757600073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16146119cb5780600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546119c39190612cb8565b925050819055505b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614611a565780600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254611a4e9190612c62565b925050819055505b5b50505050565b50505050565b611a6d8383611cd4565b611a7a6000848484611abe565b611ab9576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611ab0906129dd565b60405180910390fd5b505050565b6000611adf8473ffffffffffffffffffffffffffffffffffffffff16611ef2565b15611c48578373ffffffffffffffffffffffffffffffffffffffff1663150b7a02611b08610fb7565b8786866040518563ffffffff1660e01b8152600401611b2a9493929190612934565b602060405180830381600087803b158015611b4457600080fd5b505af1925050508015611b7557506040513d601f19601f82011682018060405250810190611b72919061256f565b60015b611bf8573d8060008114611ba5576040519150601f19603f3d011682016040523d82523d6000602084013e611baa565b606091505b50600081511415611bf0576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611be7906129dd565b60405180910390fd5b805181602001fd5b63150b7a0260e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916817bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614915050611c4d565b600190505b949350505050565b606060405180602001604052806000815250905090565b6060611c7782610f6c565b6000611c81611c55565b90506000815111611ca15760405180602001604052806000815250611ccc565b80611cab84611f15565b604051602001611cbc9291906128cc565b6040516020818303038152906040525b915050919050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415611d44576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611d3b90612abd565b60405180910390fd5b611d4d816118f6565b15611d8d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611d8490612a1d565b60405180910390fd5b611d9b600083836001611937565b611da4816118f6565b15611de4576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611ddb90612a1d565b60405180910390fd5b6001600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816002600083815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550808273ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60405160405180910390a4611eee600083836001611a5d565b5050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b606060006001611f2484611fed565b01905060008167ffffffffffffffff811115611f4357611f42612f0a565b5b6040519080825280601f01601f191660200182016040528015611f755781602001600182028036833780820191505090505b509050600082602001820190505b600115611fe2578080600190039150507f3031323334353637383961626364656600000000000000000000000000000000600a86061a8153600a8581611fcc57611fcb612e7d565b5b0494506000851415611fdd57611fe2565b611f83565b819350505050919050565b600080600090507a184f03e93ff9f4daa797ed6e38ed64bf6a1f010000000000000000831061204b577a184f03e93ff9f4daa797ed6e38ed64bf6a1f010000000000000000838161204157612040612e7d565b5b0492506040810190505b6d04ee2d6d415b85acef81000000008310612088576d04ee2d6d415b85acef8100000000838161207e5761207d612e7d565b5b0492506020810190505b662386f26fc1000083106120b757662386f26fc1000083816120ad576120ac612e7d565b5b0492506010810190505b6305f5e10083106120e0576305f5e10083816120d6576120d5612e7d565b5b0492506008810190505b61271083106121055761271083816120fb576120fa612e7d565b5b0492506004810190505b60648310612128576064838161211e5761211d612e7d565b5b0492506002810190505b600a8310612137576001810190505b80915050919050565b82805461214c90612da2565b90600052602060002090601f01602090048101928261216e57600085556121b5565b82601f1061218757805160ff19168380011785556121b5565b828001600101855582156121b5579182015b828111156121b4578251825591602001919060010190612199565b5b5090506121c291906121c6565b5090565b5b808211156121df5760008160009055506001016121c7565b5090565b60006121f66121f184612bbd565b612b98565b90508281526020810184848401111561221257612211612f3e565b5b61221d848285612d60565b509392505050565b600061223861223384612bee565b612b98565b90508281526020810184848401111561225457612253612f3e565b5b61225f848285612d60565b509392505050565b600081359050612276816132cc565b92915050565b60008135905061228b816132e3565b92915050565b6000813590506122a0816132fa565b92915050565b6000815190506122b5816132fa565b92915050565b600082601f8301126122d0576122cf612f39565b5b81356122e08482602086016121e3565b91505092915050565b600082601f8301126122fe576122fd612f39565b5b813561230e848260208601612225565b91505092915050565b60008135905061232681613311565b92915050565b60006020828403121561234257612341612f48565b5b600061235084828501612267565b91505092915050565b600080604083850312156123705761236f612f48565b5b600061237e85828601612267565b925050602061238f85828601612267565b9150509250929050565b6000806000606084860312156123b2576123b1612f48565b5b60006123c086828701612267565b93505060206123d186828701612267565b92505060406123e286828701612267565b9150509250925092565b60008060006060848603121561240557612404612f48565b5b600061241386828701612267565b935050602061242486828701612267565b925050604061243586828701612317565b9150509250925092565b6000806000806080858703121561245957612458612f48565b5b600061246787828801612267565b945050602061247887828801612267565b935050604061248987828801612317565b925050606085013567ffffffffffffffff8111156124aa576124a9612f43565b5b6124b6878288016122bb565b91505092959194509250565b600080604083850312156124d9576124d8612f48565b5b60006124e785828601612267565b92505060206124f88582860161227c565b9150509250929050565b6000806040838503121561251957612518612f48565b5b600061252785828601612267565b925050602061253885828601612317565b9150509250929050565b60006020828403121561255857612557612f48565b5b600061256684828501612291565b91505092915050565b60006020828403121561258557612584612f48565b5b6000612593848285016122a6565b91505092915050565b6000602082840312156125b2576125b1612f48565b5b600082013567ffffffffffffffff8111156125d0576125cf612f43565b5b6125dc848285016122e9565b91505092915050565b6000602082840312156125fb576125fa612f48565b5b600061260984828501612317565b91505092915050565b61261b81612cec565b82525050565b61262a81612cfe565b82525050565b600061263b82612c1f565b6126458185612c35565b9350612655818560208601612d6f565b61265e81612f4d565b840191505092915050565b600061267482612c2a565b61267e8185612c46565b935061268e818560208601612d6f565b61269781612f4d565b840191505092915050565b60006126ad82612c2a565b6126b78185612c57565b93506126c7818560208601612d6f565b80840191505092915050565b60006126e0602d83612c46565b91506126eb82612f5e565b604082019050919050565b6000612703603283612c46565b915061270e82612fad565b604082019050919050565b6000612726602583612c46565b915061273182612ffc565b604082019050919050565b6000612749601c83612c46565b91506127548261304b565b602082019050919050565b600061276c602483612c46565b915061277782613074565b604082019050919050565b600061278f601983612c46565b915061279a826130c3565b602082019050919050565b60006127b2602983612c46565b91506127bd826130ec565b604082019050919050565b60006127d5602e83612c46565b91506127e08261313b565b604082019050919050565b60006127f8602083612c46565b91506128038261318a565b602082019050919050565b600061281b602083612c46565b9150612826826131b3565b602082019050919050565b600061283e601883612c46565b9150612849826131dc565b602082019050919050565b6000612861602183612c46565b915061286c82613205565b604082019050919050565b6000612884603d83612c46565b915061288f82613254565b604082019050919050565b60006128a7601083612c46565b91506128b2826132a3565b602082019050919050565b6128c681612d56565b82525050565b60006128d882856126a2565b91506128e482846126a2565b91508190509392505050565b60006020820190506129056000830184612612565b92915050565b60006040820190506129206000830185612612565b61292d6020830184612612565b9392505050565b60006080820190506129496000830187612612565b6129566020830186612612565b61296360408301856128bd565b81810360608301526129758184612630565b905095945050505050565b60006020820190506129956000830184612621565b92915050565b600060208201905081810360008301526129b58184612669565b905092915050565b600060208201905081810360008301526129d6816126d3565b9050919050565b600060208201905081810360008301526129f6816126f6565b9050919050565b60006020820190508181036000830152612a1681612719565b9050919050565b60006020820190508181036000830152612a368161273c565b9050919050565b60006020820190508181036000830152612a568161275f565b9050919050565b60006020820190508181036000830152612a7681612782565b9050919050565b60006020820190508181036000830152612a96816127a5565b9050919050565b60006020820190508181036000830152612ab6816127c8565b9050919050565b60006020820190508181036000830152612ad6816127eb565b9050919050565b60006020820190508181036000830152612af68161280e565b9050919050565b60006020820190508181036000830152612b1681612831565b9050919050565b60006020820190508181036000830152612b3681612854565b9050919050565b60006020820190508181036000830152612b5681612877565b9050919050565b60006020820190508181036000830152612b768161289a565b9050919050565b6000602082019050612b9260008301846128bd565b92915050565b6000612ba2612bb3565b9050612bae8282612dd4565b919050565b6000604051905090565b600067ffffffffffffffff821115612bd857612bd7612f0a565b5b612be182612f4d565b9050602081019050919050565b600067ffffffffffffffff821115612c0957612c08612f0a565b5b612c1282612f4d565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600081905092915050565b6000612c6d82612d56565b9150612c7883612d56565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115612cad57612cac612e4e565b5b828201905092915050565b6000612cc382612d56565b9150612cce83612d56565b925082821015612ce157612ce0612e4e565b5b828203905092915050565b6000612cf782612d36565b9050919050565b60008115159050919050565b60007fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b83811015612d8d578082015181840152602081019050612d72565b83811115612d9c576000848401525b50505050565b60006002820490506001821680612dba57607f821691505b60208210811415612dce57612dcd612eac565b5b50919050565b612ddd82612f4d565b810181811067ffffffffffffffff82111715612dfc57612dfb612f0a565b5b80604052505050565b6000612e1082612d56565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff821415612e4357612e42612e4e565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4552433732313a2063616c6c6572206973206e6f7420746f6b656e206f776e6560008201527f72206f7220617070726f76656400000000000000000000000000000000000000602082015250565b7f4552433732313a207472616e7366657220746f206e6f6e20455243373231526560008201527f63656976657220696d706c656d656e7465720000000000000000000000000000602082015250565b7f4552433732313a207472616e736665722066726f6d20696e636f72726563742060008201527f6f776e6572000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20746f6b656e20616c7265616479206d696e74656400000000600082015250565b7f4552433732313a207472616e7366657220746f20746865207a65726f2061646460008201527f7265737300000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f766520746f2063616c6c657200000000000000600082015250565b7f4552433732313a2061646472657373207a65726f206973206e6f74206120766160008201527f6c6964206f776e65720000000000000000000000000000000000000000000000602082015250565b7f45524337323155524953746f726167653a2055524920736574206f66206e6f6e60008201527f6578697374656e7420746f6b656e000000000000000000000000000000000000602082015250565b7f4552433732313a206d696e7420746f20746865207a65726f2061646472657373600082015250565b7f4f776e61626c653a2063616c6c6572206973206e6f7420746865206f776e6572600082015250565b7f4552433732313a20696e76616c696420746f6b656e2049440000000000000000600082015250565b7f4552433732313a20617070726f76616c20746f2063757272656e74206f776e6560008201527f7200000000000000000000000000000000000000000000000000000000000000602082015250565b7f4552433732313a20617070726f76652063616c6c6572206973206e6f7420746f60008201527f6b656e206f776e6572206f7220617070726f76656420666f7220616c6c000000602082015250565b7f6d697373696e6720495046532075726c00000000000000000000000000000000600082015250565b6132d581612cec565b81146132e057600080fd5b50565b6132ec81612cfe565b81146132f757600080fd5b50565b61330381612d0a565b811461330e57600080fd5b50565b61331a81612d56565b811461332557600080fd5b5056fea2646970667358221220ca582cf77a025b41c3a81adb2739eb93306e1b0814234bb547c301a605094ae964736f6c63430008070033"