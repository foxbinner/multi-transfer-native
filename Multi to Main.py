from web3 import Web3

# .-.. .. - - . ..-. --- -..-
#  Constants & Configuration
# .-.. .. - - . ..-. --- -..-
AMOUNT = 0 # Put 0 to send all
RPC_URL = 'https://ethereum-sepolia-rpc.publicnode.com'
CHAIN_ID = 11155111
TICKER = 'ETH'
EXPLORER = 'https://sepolia.etherscan.io'
GAS_LIMIT = 21000  # Fixed gas limit
GAS_ADD = 1  # Put 0 for minimum gas fee

AMOUNT_TO_SEND = Web3.to_wei(AMOUNT, 'ether')

# .-.. .. - - . ..-. --- -..-
#   File Configuration
# .-.. .. - - . ..-. --- -..-
# Load main wallet address
with open('mainwallet.txt', 'r') as file:
    line = file.readline().strip()
wallet_data = line.split(',')
MAIN_WALLET_ADDRESS = wallet_data[1]

# Load sender credentials
with open('test.txt', 'r') as file:
    SENDER_ADDRESSES_AND_KEYS = [line.strip().split(',') for line in file if line.strip()]

# .-.. .. - - . ..-. --- -..-
#  Web3 Initialization
# .-.. .. - - . ..-. --- -..-
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.is_connected():
    raise Exception("Failed to connect to the chain")

# Configure gas settings
current_gas_price = web3.eth.gas_price
gas_price = current_gas_price + Web3.to_wei(GAS_ADD, 'gwei')

# .-.. .. - - . ..-. --- -..-
#  Core Function
# .-.. .. - - . ..-. --- -..-
if AMOUNT == 0:
    print(f"Sending All {TICKER}:\n")
else:
    print(f"Sending {AMOUNT} {TICKER}:\n")

def send_token(sender_address, sender_private_key, nonce):
    try:
        balance = web3.eth.get_balance(sender_address)
        gas_fee = GAS_LIMIT * gas_price

        if balance < (AMOUNT * 1e18 + gas_fee):
            print(f"Skipping {sender_address} - Balance: {balance / 1e18:.8f} {TICKER} - Need: {AMOUNT + gas_fee / 1e18} {TICKER}")
            return None

        if AMOUNT == 0:
            amount_to_send = balance - gas_fee
        else:
            amount_to_send = AMOUNT_TO_SEND

        transaction = {
            "from": sender_address,
            "to": MAIN_WALLET_ADDRESS,
            "value": amount_to_send,
            "gas": GAS_LIMIT,
            "gasPrice": gas_price,
            "nonce": nonce,
            "chainId": CHAIN_ID,
        }

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, sender_private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

        # # Wait for confirmation
        # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        # fee = tx_receipt['gasUsed'] * gas_price

        print(f"{sender_address} - Amount: {amount_to_send / 1e18} {TICKER} - "
              # f"Fee: {Web3.from_wei(fee, 'ether')} {TICKER} - "
              f"{EXPLORER}/tx/0x{tx_hash.hex()}")
    except Exception as e:
        print(f"Failed {sender_address}: {str(e)}")

# .-.. .. - - . ..-. --- -..-
#  Execution Flow
# .-.. .. - - . ..-. --- -..-
try:
    for sender_data in SENDER_ADDRESSES_AND_KEYS:
        sender_address = sender_data[1]
        sender_private_key = sender_data[3]
        nonce = web3.eth.get_transaction_count(sender_address)
        send_token(sender_address, sender_private_key, nonce)

except Exception as e:
    print(f"Script error: {str(e)}")