// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/*
 * This contract is used to keep a log of patients that the doctor interacts with
 */
contract PatientToken is ERC721, Ownable {
    uint256 public numberOfPatients;
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

    Patient[] private patientsRegistry;

    // events
    event ContractOwnershipChanged(bool success);

    function addNewPatient(
        address patient,
        address dataContract,
        address prescriptionContract
    ) public onlyOwner {
        numberOfPatients = numberOfPatients + 1;
        patientsRegistry.push(
            Patient(patient, dataContract, prescriptionContract)
        );
    }

    function checkIfPatientExists(address patient)
        public
        view
        onlyOwner
        returns (bool)
    {
        bool _patientExists = false;

        for (uint256 i = 0; i < patientsRegistry.length; i++) {
            if (patientsRegistry[i].patientAddress == patient) {
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
        for (uint256 i = 0; i < patientsRegistry.length; i++) {
            if (patientsRegistry[i].patientAddress == patient) {
                Patient storage _currentPatient = patientsRegistry[i];
                return (
                    _currentPatient.patientDataContract,
                    _currentPatient.patientPrescriptionContract
                );
            }
        }
    }


    //return Array of structure
    function getAllPatients() public view onlyOwner returns (address[] memory, address[] memory, address[] memory){
        address[] memory patientAddress = new address[](numberOfPatients);
        address[] memory dataContract = new address[](numberOfPatients);
        address[] memory prescriptionContract = new address[](numberOfPatients);
        for (uint256 i = 0; i < numberOfPatients; i++) {
            Patient storage _currentPatient = patientsRegistry[i];
            patientAddress[i] = _currentPatient.patientAddress;
            dataContract[i] = _currentPatient.patientDataContract;
            prescriptionContract[i] = _currentPatient.patientPrescriptionContract;
        }

        return (patientAddress, dataContract, prescriptionContract);

    }

    // transfer contract ownership
    function transferOwnership(address newOwner)
        public
        override(Ownable)
        onlyOwner
    {
        _transferOwnership(newOwner);
        emit ContractOwnershipChanged(true);
    }
}