# AES-256 File Encryption/Decryption Application

## Overview
The AES-256 File Encryption/Decryption Application is a Python-based GUI tool designed to securely encrypt and decrypt text files using the AES (Advanced Encryption Standard) algorithm with a 256-bit key. The application provides a user-friendly interface for selecting files, entering passwords, and saving encrypted or decrypted files.

## Features
- **Encryption and Decryption**: Securely encrypt and decrypt text files using AES-256.
- **User-friendly GUI**: Modern and intuitive interface for ease of use.
- **Password Protection**: Utilizes a password to generate a cryptographic key for encryption and decryption.
- **File Handling**: Supports the selection of input files and the specification of output files.

## Requirements
- **Python**: Version 3.6 or higher
- **Dependencies**: 
  - `tkinter` (included with Python)
  - `cryptography` library
  - `PyInstaller` (for creating the executable)

## Installation

1. **Clone or Download the Repository**:
   - Clone the repository or download the script file `encryption_tool.py`.

2. **Install Required Libraries**:
   - Open a command prompt or terminal and install the required libraries:

   ```bash
   pip install cryptography
