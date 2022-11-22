// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DataToken is ERC721, ERC721URIStorage, Ownable {
    uint256 private _numberOfDataTokens;

    //set in constructor or in changeDoctor()
    address private _doctor;

    constructor(address doctorAddress) ERC721("DataToken", "DTK") {
        //set contract ownership to doctor
        _transferOwnership(msg.sender);
        //set patient to be the owner of tokens (needed for ownership functions)
        _doctor = doctorAddress;
    }

    // events
    event Minted(address indexed minter, uint256 nftId);
    event TokenOwnershipChanged(bool success);
    event DoctorChanged(bool success);
    event ContractOwnershipChanged(bool success);

    //mint data token and save data to dataItems array
    function mintDataToken(string memory ipfsDataURL)
        public
        onlyOwner
        returns (uint256)
    {
        require(
            bytes(ipfsDataURL).length > 0,
            "missing IPFS url for the data item"
        );

        //set NFT tokenID
        _numberOfDataTokens += 1;
        uint256 tokenId = _numberOfDataTokens;

        //mint
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, ipfsDataURL);
        emit Minted(msg.sender, tokenId);

        //return token(NFT) ID
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
        address _tokenOwner = _ownerOf(tokenId);
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

    //functions bellow need to be overriden so the contract works as intended
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory data
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public override(ERC721) {
        emit TokenOwnershipChanged(false);
    }

    function transferOwnership(address newOwner)
        public
        override(Ownable)
        onlyOwner
    {
        emit ContractOwnershipChanged(false);
    }
}
