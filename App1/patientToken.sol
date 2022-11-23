// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/*
 * This contract is used to keep a log of patients that the doctor interacts with
 */
contract PatientToken is ERC721, ERC721URIStorage, Ownable {
    uint256 private _numberOfPatientTokens;

    // constructor sets contract owner to the doctor who deployed it
    // contract is deployed once per doctor so all doctor's patients are under one contract
    constructor() ERC721("PatientToken", "PTK") {
        _transferOwnership(msg.sender);
    }

    struct Patient {
        address patientAddress;
        address patientDataContract;
        address patientPrescriptionContract;
    }

    Patient[] private patients;

    // events
    event Minted(address indexed minter, uint256 nftId);

    // mint patient token
    function mintPatientToken(string memory ipfsDataURL)
        public
        onlyOwner
        returns (uint256)
    {
        require(
            bytes(ipfsDataURL).length > 0,
            "missing IPFS url for the data item"
        );

        // set NFT tokenID
        _numberOfPatientTokens += 1;
        uint256 tokenId = _numberOfPatientTokens;

        // mint
        _safeMint(msg.sender, tokenId);
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
        address _patient = owner();
        address _tokenOwner = ownerOf(tokenId);
        //only doctor or the patient or someone who bought the data can see the URI
        require(
            msg.sender == _patient ||
                msg.sender == _doctor ||
                msg.sender == _tokenOwner,
            "Only the owner of data (the patient/someone who bought it) or the doctor of patient can view data"
        );
        return super.tokenURI(tokenId);
    }

    // _burn function is an override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

}