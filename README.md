# RSA File Encryption Experiment

## Overview
An RSA-based file encryption/decryption experiment using a 2048-bit RSA key pair and OAEP padding with SHA-256.

## Technologies
- Python
- `cryptography`
- RSA
- OAEP
- SHA-256
- PEM key serialization

## Skills demonstrated
- Public-key cryptography
- Key generation
- Encryption/decryption
- Secure padding concepts
- File handling

## Important limitation
RSA is not designed to encrypt arbitrarily large files directly. This project is therefore an educational experiment. A production design should use hybrid encryption: a random AES key encrypts the file, and RSA-OAEP encrypts that AES key.

## Run
```bash
python3 asymm.py
```

Use test files only until the implementation has been thoroughly reviewed.

## Portfolio note
Strong evidence of practical cryptography learning, especially because the code uses RSA-OAEP rather than raw RSA.
