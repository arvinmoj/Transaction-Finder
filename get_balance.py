from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<API_KEY>'))

def get_balance(address):
    return w3.eth.getBalance(address)

address = Web3.toChecksumAddress('<ADDRESS>')

balance = get_balance(address)
print(f"Balance of address {address}: {w3.fromWei(balance, 'ether')} Ether")
