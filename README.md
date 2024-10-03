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

```markdown
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
   Open a command prompt or terminal and install the required libraries:

   ```bash
   pip install cryptography
   ```

3. **Running the Application**:
   You can run the application directly with Python:

   ```bash
   python encryption_tool.py
   ```

   Alternatively, you can create an executable using PyInstaller (see the section below).

## Usage

### Encrypting a File

1. **Open the Application**: Run the application to open the GUI.
2. **Enter Password**: Input a password in the designated field. This password will be used to derive the encryption key.
3. **Select File**: Click on the "Encrypt File" button. A file dialogue will open, allowing you to choose the text file you want to encrypt.
4. **Save Encrypted File**: After selecting the file, you will be prompted to choose a location and name for the encrypted file (default extension is `.enc`).
5. **Success Message**: Upon successful encryption, a message box will inform you that the file has been encrypted.

### Decrypting a File

1. **Open the Application**: Run the application to open the GUI.
2. **Enter Password**: Input the same password used during encryption.
3. **Select File**: Click on the "Decrypt File" button. A dialogue will open, allowing you to select the encrypted file (with the `.enc` extension).
4. **Save Decrypted File**: After selecting the file, you will be prompted to choose a location and name for the decrypted file (default extension is `.txt`).
5. **Success Message**: Upon successful decryption, a message box will inform you that the file has been decrypted.

## Technical Details

### Encryption Algorithm
- **Algorithm**: AES (Advanced Encryption Standard)
- **Key Size**: 256 bits
- **Block Size**: 128 bits
- **Mode**: CBC (Cipher Block Chaining)

### Key Derivation
The application uses PBKDF2 (Password-Based Key Derivation Function 2) with:
- **Hash Function**: SHA-256
- **Iterations**: 100,000
- **Salt**: A fixed salt (for demo purposes; in production, a random salt should be used).

### Libraries Used
- **tkinter**: For creating the graphical user interface.
- **cryptography**: For implementing encryption, decryption, and key derivation.

## Creating an Executable
To create a standalone executable of the application:

1. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

2. **Navigate to the Script Directory**:

   ```bash
   cd path\to\your\script
   ```

3. **Create the Executable**:

   ```bash
   pyinstaller --onefile --windowed "encryption_tool.py"
   ```

4. **Locate the Executable**: The executable will be found in the `dist` folder within the script directory.

## Conclusion
This application provides a secure method for encrypting and decrypting files using industry-standard AES-256 encryption. It is suitable for users who need to protect sensitive information stored in text files.

For any further assistance or questions, feel free to reach out!
```
