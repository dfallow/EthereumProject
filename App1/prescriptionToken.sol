// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/*
 * This contract is used to save prescriptions as NFTs on the blockchain
 * The reference to prescription on IPFS is stored in NFT token URI
 */
contract PrescriptionToken is ERC721, ERC721URIStorage, Ownable {
    uint256 private _numberOfPrescriptionTokens;

    address private _patient;

    // constructor sets contract owner to the doctor who deployed it
    // it also sets _patient address
    // contract is deployed once per patient so all prescriptions are under one contract
    constructor(address patient) ERC721("PrescriptionToken", "PTK") {
        _transferOwnership(msg.sender);
        _patient = patient;
    }

    // events
    event Minted(address indexed minter, uint256 nftId);
    event TokenOwnershipChanged(bool success);
    event ContractOwnershipChanged(bool success);

    // mint prescription token
    function mintPrescriptionToken(string memory ipfsDataURL)
        public
        onlyOwner
        returns (uint256)
    {
        require(
            bytes(ipfsDataURL).length > 0,
            "missing IPFS url for the data item"
        );

        // set NFT tokenID
        _numberOfPrescriptionTokens += 1;
        uint256 tokenId = _numberOfPrescriptionTokens;

        // mint
        _safeMint(msg.sender, tokenId);
        // set tokenID to link back to prescription on IPFS
        _setTokenURI(tokenId, ipfsDataURL);

        emit Minted(msg.sender, tokenId);

        // return token(NFT) ID
        return tokenId;
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        //only doctor or the patient can see the URI
        address _doctor = owner();
        require(
            msg.sender == _patient || msg.sender == _doctor,
            "Only the doctor or the patient can see the URI"
        );
        return super.tokenURI(tokenId);
    }

    // change ownership of prescription tokens passed in an array
    function transferTokenOwnership(address to, uint256[] memory tokenIdArray)
        public
        onlyOwner
    {
        for (uint256 i = 0; i < tokenIdArray.length; i++) {
            safeTransferFrom(msg.sender, to, tokenIdArray[i]);
        }

        emit TokenOwnershipChanged(true);
    }

    // transfer contract ownership
    function transferOwnership(address newOwner)
        public
        override(Ownable)
        onlyOwner
    {
        _transferOwnership(newOwner);
        emit ContractOwnershipChanged(false);
    }

    function getPatient() public view onlyOwner returns (address) {
        return _patient;
    }


    // _burn function is an override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    // TODO: token and contract ownership transfer
}
