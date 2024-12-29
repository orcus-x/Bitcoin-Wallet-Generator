# Bitcoin Wallet Generator and Balance Checker

This Python project demonstrates how to generate Bitcoin wallets using the BIP-39 and BIP-44 standards. It also checks the wallet balance using a public API.

## Features

- Generates a 12-word mnemonic using the BIP-39 word list.
- Derives Bitcoin wallets using the BIP-44 standard.
- Checks the Bitcoin wallet balance using the BlockCypher API.
- Prints the private key for wallets with a non-zero balance.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.8+** installed.
2. **Dependencies** listed in the `requirements.txt` file installed (see below).
3. An active internet connection to query the balance from the BlockCypher API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bitcoin-wallet-generator.git
   cd bitcoin-wallet-generator
