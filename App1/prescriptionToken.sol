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
    uint256 public numberOfPrescriptionTokens;

    // constructor sets contract owner to the doctor who deployed it
    // contract is deployed once per doctor for all their patients
    constructor() ERC721("PrescriptionToken", "PTK") {
        _transferOwnership(msg.sender);
    }

    // events
    event Minted(address indexed minter, address patient, uint256 tokenId);
    event TokenOwnershipChanged(bool success);
    event ContractOwnershipChanged(bool success);
    event DataSaved(bool success);

    struct PrescriptionItem {
        address patientAddress;
        uint256 prescriptionTokenId;
        string prescriptionIpfsURL;
    }

    PrescriptionItem[] private prescriptionItems;

    // mint prescription token
    function mintPrescriptionToken(string memory prescriptionIpfsURL, address patientAddress)
        public
        onlyOwner
        returns (uint256)
    {
        require(
            bytes(prescriptionIpfsURL).length > 0,
            "missing IPFS url for the data item"
        );

        // set NFT tokenID
        numberOfPrescriptionTokens += 1;
        uint256 tokenId = numberOfPrescriptionTokens;

        // mint
        _safeMint(patientAddress, tokenId);
        // set tokenID to link back to prescription on IPFS
        _setTokenURI(tokenId, prescriptionIpfsURL);

        emit Minted(msg.sender, patientAddress, tokenId);

        _addData(patientAddress, tokenId, prescriptionIpfsURL);

        // return token(NFT) ID
        return tokenId;
    }

     function _addData(address patientAddress, uint256 tokenId, string memory prescriptionIpfsURL) private onlyOwner {
        prescriptionItems.push(PrescriptionItem(patientAddress, tokenId, prescriptionIpfsURL));
        emit DataSaved(true);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        //only doctor or the patient can see the URI
        address _doctor = owner();
        address _tokenOwner = ownerOf(tokenId);
        require(
            msg.sender == _doctor || msg.sender == _tokenOwner,
            "Only the doctor or the patient(token owner) can see the URI"
        );
        return super.tokenURI(tokenId);
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

    function getPrescriptionByTokenId(uint256 prescriptionTokenId) public view onlyOwner returns (PrescriptionItem memory) { 
        require(
            _exists(prescriptionTokenId),
            "URI query for nonexistent token"
        );
        for (uint256 i = 0; i < prescriptionItems.length; i++) {
            if (prescriptionItems[i].prescriptionTokenId == prescriptionTokenId) {
                PrescriptionItem storage _prescriptionItem = prescriptionItems[i];
                return _prescriptionItem;
            }
        }
    }

    function getPrescriptionsByPatient(address patientAddress) public view onlyOwner returns (PrescriptionItem[] memory) {
        PrescriptionItem[] memory _items = new PrescriptionItem[](prescriptionItems.length);

        for (uint256 i = 0; i < prescriptionItems.length; i++) {
            if (prescriptionItems[i].patientAddress == patientAddress) {
                PrescriptionItem memory _prescriptionItem = prescriptionItems[i];
                _items[i] = _prescriptionItem;
            }
        }

        return _items;
    } 

    // _burn function is an override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

}
