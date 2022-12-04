from library import deployContracts, variables, contractInteraction, getContracts

from library import contractDetailsMachine as machine_cd
from library import contractDetailsMachineData as data_cd
from library import contractDetailsPatientToken as patient_cd
from library import contractDetailsPrescription as prescription_cd


def get_all_contract_address_on_block():
    
    
    contract_addresses = getContracts.get_contracts("machine", machine_cd)
    
    #print("\n\nADDRESSES", contract_addresses)
    
    #getContracts.check_contracts(contract_addresses)
    
    return



get_all_contract_address_on_block()