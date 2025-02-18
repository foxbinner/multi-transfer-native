<div align="center">

# Transfer Native Token

[![Python][python-version-img]][python-version-url]
[![Web3][web3-version-img]][web3-version-url]
[![Issues][repo_issues_img]][repo_issues_url]
[![License][repo_license_img]][repo_license_url]

Easily transfer native tokens (e.g., Sepolia ETH) from <br>**single address to multiple addresses** or consolidate funds from <br>**multiple addresses into one**—all in an instant!

<p align="center">
  <img width="45%" alt="Main to Multi" src="https://i.postimg.cc/wBFpH5PF/main-to-multi.png">
  <img width="45%" alt="Multi to Main" src="https://i.postimg.cc/TPT6ZNkp/multi-to-main.png">
</p>

</div>

## 🚀 Introduction

Transferring native tokens (e.g., Sepolia ETH, Base ETH) to multiple addresses can be time-consuming when done manually with wallets (e.g., Metamask,  Rabby). My solution simplifies this with two Python scripts:

- **Single-to-Multiple Transfers** – Send native tokens from one address to multiple recipients in a single transaction.
- **Multiple-to-Single Transfers** – Consolidate tokens from multiple addresses into a single destination efficiently.

Save time, reduce complexity, and make token transfers easier! 🧙‍♂️

## 📖 User Manual

- Keep your addresses and private keys formatted and saved in ```mainwallet.txt``` and ```recipients.txt```.
- Change the following values to start with:
```
AMOUNT =
RPC_URL = 'https://ethereum-sepolia-rpc.publicnode.com'
CHAIN_ID = 11155111
TICKER = 'ETH'
EXPLORER = 'https://sepolia.etherscan.io'
GAS_LIMIT = 21000
```

## 🚩 Contribution

Found an issue or have a suggestion? Report it in [issues][repo_issues_url] or fork & submit a pull request.<br>Every contribution counts! 🎉

## 📄 License

This project is open-source and licensed under the [MIT license][repo_license_url].

<!-- Repo Links -->
[repo_url]: https://github.com/foxbinner/multi-transfer-native
[repo_license_url]: https://github.com/foxbinner/multi-transfer-native/blob/main/LICENSE
[repo_issues_url]: https://github.com/foxbinner/multi-transfer-native/issues

[repo_license_img]: https://img.shields.io/badge/license-MIT-red
[repo_issues_img]: https://img.shields.io/badge/feedback-open-green

<!-- Extras -->
[web3-version-img]: https://img.shields.io/badge/web3-7.7.0-blue
[web3-version-url]: https://pypi.org/project/web3/7.7.0
[python-version-img]: https://img.shields.io/badge/python-3.12.9-blue
[python-version-url]: https://www.python.org/downloads
