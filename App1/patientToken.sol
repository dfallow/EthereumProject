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
    address private NULL = 0x0000000000000000000000000000000000000000;

    // constructor sets contract owner to the doctor who deployed it
    // contract is deployed once per doctor so all doctor's patients are under one contract
    constructor() ERC721("PatientToken", "PTK") {
        _transferOwnership(msg.sender);
    }

    struct Patient {
        address patientAddress; // account address
        address patientDataContract; // patient's data contract address on the blockchain
        address patientPrescriptionContract; // patient's prescription contract address on the blockchain
    }

    Patient[] private patients;

    // events
    event Minted(address indexed minter, uint256 nftId);
    event ContractOwnershipChanged(bool success);

    function addNewPatient(
        address patient,
        address dataContract,
        address prescriptionContract
    ) public onlyOwner {
        patients.push(Patient(patient, dataContract, prescriptionContract));
    }

    function checkIfPatientExists(address patient)
        public
        view
        onlyOwner
        returns (bool)
    {
        bool _patientExists = false;

        for (uint256 i = 0; i < patients.length; i++) {
            if (patients[i].patientAddress == patient) {
                _patientExists = true;
            }
        }
        return _patientExists;
    }

    function getPatient(address patient)
        public
        view
        onlyOwner
        returns (address dataContract, address prescriptionContract)
    {
        for (uint256 i = 0; i < patients.length; i++) {
            if (patients[i].patientAddress == patient) {
                Patient storage _currentPatient = patients[i];
                return (
                    _currentPatient.patientDataContract,
                    _currentPatient.patientPrescriptionContract
                );
            }
        }
    }

    // TODO: check if minting is needed at all (if we don't store any ipfs data related to a patient, then we don't need this)
    // mint patient token
    function mintPatientToken(string memory ipfsDataURL)
        public
        onlyOwner
        returns (uint256)
    {
        require(bytes(ipfsDataURL).length > 0, "missing IPFS url");

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
        onlyOwner
        returns (string memory)
    {
        return super.tokenURI(tokenId);
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

    // _burn function is an override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }
}
