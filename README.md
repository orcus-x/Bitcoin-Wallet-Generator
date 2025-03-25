# Bitcoin Wallet Generator and Balance Checker

This Python project demonstrates how to generate Bitcoin wallets using the BIP-39 and BIP-44 standards. It also checks the wallet balance using a public API.

## Requirements

- Python 3.x
- `bip_utils` library for generating Bitcoin wallets from BIP-39 mnemonic
- `requests` library to interact with the BlockCypher API

To install the required libraries, you can run:

```bash
pip install bip-utils requests
```

## How It Works

1. **Generate a 12-word BIP-39 Mnemonic**: The script generates a random 12-word mnemonic phrase using the BIP-39 standard.
2. **Generate Wallet**: From the mnemonic, a Bitcoin wallet is generated using BIP-44 derivation path (Bitcoin in this case).
3. **Check Balance**: The script checks the balance of the generated Bitcoin address via BlockCypher API. If the balance is greater than 0, the private key is displayed.

## Usage

Run the script by executing:

```bash
python main.py
```

It will generate a mnemonic, derive the wallet, and check the balance. If the balance is greater than 0, it will display the private key.

## Example Output

```text
Generated Mnemonic: "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
Wallet Address: bc1qpxw8c5zth7vq85vjqek7h5kyr3dxuqvqe5rphd
Balance: 0 BTC
Wallet has no balance.
```

## Disclaimer

- This script is for educational purposes only.
- Do not use this script with real funds unless you understand the risks.
- Keep your private keys secure. Never share them publicly.
```
