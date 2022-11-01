from web3 import Web3
import web3

# access the tester accounts
w3 = Web3(Web3.EthereumTesterProvider())
# print(w3.isConnected())
# print(w3.eth.accounts)

# initialise the default_account
w3.eth.default_account = w3.eth.accounts[0]
myAcc = w3.eth.default_account
acc2 = w3.eth.accounts[1]

print(f"my account address: {myAcc}")
# 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf

# to view balance
# print(f"my balance: {w3.eth.get_balance(myAcc)}")

# transations
tx_hash = w3.eth.send_transaction({
    'from': w3.eth.accounts[1],
   'to': myAcc,
   'value': w3.toWei(3, 'ether')
})

w3.eth.get_transaction(tx_hash)
# print(f"my balance: {w3.eth.get_balance(myAcc)}")


# create a new account
newAcc = w3.eth.account.create()

# public address of newAcc
# print(newAcc.address) 
#0x0A6d8c0D1e979b5FCb17bBCdC743f2B57a18DA48

# private key
# print(newAcc.key)

# transaction simulation
print(newAcc.address)
print(myAcc)

print(f"before transaction: myAcc's balance {w3.eth.get_balance(myAcc)}")
print(f"before transaction: newAcc's balance {w3.eth.get_balance(newAcc.address)}")

tx_hash = w3.eth.send_transaction({
    'from': myAcc,
	'to': newAcc.address,
	'value': w3.toWei(3, 'ether')
})

tx = {
    'to': myAcc,
    'value': 10000000,
    'gas': 21000, 
    'gasPrice': w3.eth.get_block('pending')['baseFeePerGas'],
    'nonce': 0
}

signed = w3.eth.account.sign_transaction(tx, newAcc.key)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)

print(f"the gas price: {tx['gasPrice']}")
print(f"after transaction: myAcc's balance {w3.eth.get_balance(myAcc)}")
print(f"after transaction: newAcc's balance {w3.eth.get_balance(newAcc.address)}")







