from web3 import Web3

# .-.. .. - - . ..-. --- -..-
#  Constants & Configuration
# .-.. .. - - . ..-. --- -..-
AMOUNT = 0.001 # Sending amount each wallet
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
# Read main wallet credentials
with open('mainwallet.txt', 'r') as file:
    line = file.readline().strip()
wallet_data = line.split(',')
MAIN_WALLET_ADDRESS = wallet_data[1]
MAIN_WALLET_PRIVATE_KEY = wallet_data[3]

# Read recipient addresses
with open('test.txt', 'r') as file:
    RECIPIENT_ADDRESSES = [line.split(',')[1] for line in file if line.strip()]

# .-.. .. - - . ..-. --- -..-
#  Web3 Initialization
# .-.. .. - - . ..-. --- -..-
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.is_connected():
    raise Exception("Failed to connect to the chain")

# Configure gas settings
current_gas_price = web3.eth.gas_price
gas_price = current_gas_price + Web3.to_wei(GAS_ADD, 'gwei')

# Initialize main wallet
main_wallet = web3.eth.account.from_key(MAIN_WALLET_PRIVATE_KEY)

# .-.. .. - - . ..-. --- -..-
#  Core Functions
# .-.. .. - - . ..-. --- -..-
def send_token(recipient_address, amount_to_send, nonce):
    try:
        transaction = {
            "from": MAIN_WALLET_ADDRESS,
            "to": recipient_address,
            "value": amount_to_send,
            "gas": GAS_LIMIT,
            "gasPrice": gas_price,
            "nonce": nonce,
            "chainId": CHAIN_ID,
        }

        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, MAIN_WALLET_PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

        # # Wait for confirmation
        # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        # fee = tx_receipt['gasUsed'] * gas_price

        print(f"{recipient_address} - Amount: {AMOUNT} {TICKER} - "
              # f"Fee: {Web3.from_wei(fee, 'ether')} {TICKER} - "
              f"{EXPLORER}/tx/0x{tx_hash.hex()}")
    except Exception as e:
        print(f"Transaction failed to {recipient_address}: {str(e)}")

def check_balance():
    try:
        balance = web3.eth.get_balance(MAIN_WALLET_ADDRESS)
        return Web3.from_wei(balance, 'ether')
    except Exception as e:
        raise Exception(f"Failed to check balance: {str(e)}")

# .-.. .. - - . ..-. --- -..-
#  Execution Flow
# .-.. .. - - . ..-. --- -..-
try:
    # Initial checks
    balance = check_balance()
    print(f"Current {TICKER} balance: {balance}\n")

    # Calculate required funds
    total_gas_cost = gas_price * GAS_LIMIT * len(RECIPIENT_ADDRESSES)
    total_needed = (AMOUNT_TO_SEND * len(RECIPIENT_ADDRESSES)) + total_gas_cost

    if web3.eth.get_balance(MAIN_WALLET_ADDRESS) < total_needed:
        raise Exception(f"[Insufficient balance. Need {total_needed / 1e18} to proccess.]")

    # Transaction processing sequentially
    nonce = web3.eth.get_transaction_count(MAIN_WALLET_ADDRESS)

    for idx, recipient in enumerate(RECIPIENT_ADDRESSES):
        send_token(recipient, AMOUNT_TO_SEND, nonce + idx)

except Exception as e:
    print(f"Script error: {str(e)}")
