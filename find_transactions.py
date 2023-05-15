from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<API_KEY>'))

def find_transactions(address, start_block, end_block):
    transactions = []
    for block_number in range(start_block, end_block + 1):
        block = w3.eth.getBlock(block_number, full_transactions=True)
        for tx in block.transactions:
            if tx['from'] == address or tx['to'] == address:
                transactions.append(tx)
    return transactions

address = Web3.to_checksum_address('<ADDRESS>')
start_block = 10000000
end_block = 10000100

transactions = find_transactions(address, start_block, end_block)

for tx in transactions:
    print(f"Transaction hash: {Web3.toHex(tx.hash)}")
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Value: {w3.fromWei(tx['value'], 'ether')} Ether")
    print(f"Gas price: {w3.fromWei(tx['gasPrice'], 'gwei')} Gwei")
    print("\n")
