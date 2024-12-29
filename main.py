from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, Bip39MnemonicGenerator
import requests

# Generate a valid 12-word mnemonic from the BIP-39 word list
def generate_valid_mnemonic():
    return Bip39MnemonicGenerator().FromWordsNumber(12)

# Function to generate Bitcoin wallet from mnemonic
def generate_wallet(mnemonic):
    # Generate a seed from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    
    # Generate the wallet (using Bitcoin as the coin)
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)
    bip44_addr = bip44_acc.AddressIndex(0)
    
    # Get the address and private key
    address = bip44_addr.PublicKey().ToAddress()
    private_key = bip44_addr.PrivateKey().ToWif()
    
    return "bc" + address, private_key

# Function to check the balance of an Bitcoin address
def get_eth_balance(address):
    try:
        # Check the balance using a public API (e.g., BlockCypher)
        api_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
        response = requests.get(api_url)
        if response.status_code == 200:
            balance_info = response.json()
            balance = balance_info.get("balance", 0)  # balance is in satoshis
            return balance
        print(response)
        return 0
    except Exception as e:
        print(e)
        return 0

while True:
    # Generate a valid mnemonic
    mnemonic = generate_valid_mnemonic()
    print(f"Generated Mnemonic: {mnemonic}")

    # Generate wallet using the mnemonic
    wallet_address, wallet_private_key = generate_wallet(mnemonic)
    print(f"Wallet Address: {wallet_address}")

    # Get the Ethereum balance for the wallet
    balance = get_eth_balance(wallet_address)
    print(f"Balance: {balance} BTC")

    # If balance is greater than 0, print the private key
    if balance > 0:
        print(f"Private Key: {wallet_private_key}")
        break
    else:
        print("Wallet has no balance.")