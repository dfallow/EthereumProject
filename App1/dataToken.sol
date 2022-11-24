// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/*
 * This contract is used to save data items as NFTs on the blockchain
 * The reference to data item on IPFS is stored in NFT token URI
 */
contract DataToken is ERC721, ERC721URIStorage, Ownable {
    uint256 private _numberOfDataTokens;

    // address is set in constructor or in changeDoctor()
    address private _doctor;

    // constructor sets contract owner to the patient who deployed it
    // it also sets _doctor to patient's current doctor (requires doctor's address)
    // contract is deployed once per patient
    constructor(address doctorAddress) ERC721("DataToken", "DTK") {
        _transferOwnership(msg.sender);
        _doctor = doctorAddress;
    }

    // events
    event Minted(address indexed minter, uint256 nftId);
    event TokenOwnershipChanged(bool success);
    event DoctorChanged(bool success);
    event ContractOwnershipChanged(bool success);

    // mint data token
    function mintDataToken(string memory ipfsDataURL)
        public
        onlyOwner
        returns (uint256)
    {
        require(
            bytes(ipfsDataURL).length > 0,
            "missing IPFS url for the data item"
        );

        // set NFT tokenID
        _numberOfDataTokens += 1;
        uint256 tokenId = _numberOfDataTokens;

        // mint
        _safeMint(msg.sender, tokenId);
        // set tokenID to link back to data item on IPFS
        _setTokenURI(tokenId, ipfsDataURL);

        emit Minted(msg.sender, tokenId);

        // return token(NFT) ID
        return tokenId;
    }

    // change ownership of data tokens passed in an array
    function transferTokenOwnership(address to, uint256[] memory tokenIdArray)
        public
        onlyOwner
    {
        for (uint256 i = 0; i < tokenIdArray.length; i++) {
            safeTransferFrom(msg.sender, to, tokenIdArray[i]);
        }

        emit TokenOwnershipChanged(true);
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

    function changeDoctor(address newDoctor) public onlyOwner {
        _doctor = newDoctor;
        emit DoctorChanged(true);
    }

    function getDoctor() public view onlyOwner returns (address) {
        return _doctor;
    }

    // _burn function is an override required by Solidity
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    // DON'T USE THIS
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    // DON'T USE THIS
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory data
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    // DON'T USE THIS
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    // DON'T USE THIS
    function transferOwnership(address newOwner)
        public
        override(Ownable)
        onlyOwner
    {
        emit ContractOwnershipChanged(false);
    }
}