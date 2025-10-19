🔐 Playfair Cipher – Encryption & Decryption

📘 Overview
The Playfair Cipher is a classic substitution cipher used for encrypting pairs of letters (digraphs).
This project implements encryption and decryption techniques for the Playfair Cipher using Python, along with a web-based interface built using HTML, CSS, and JavaScript for local hosting.

🧠 Features
✅ Encryption and decryption of text messages
✅ Key matrix generation from user-defined key
✅ Automatic handling of repeated letters and odd-length messages
✅ Visual 5×5 matrix display in browser
✅ Works offline — no internet required
✅ Supports running on local server using Python

🧩 Project Structure
Playfair-Cipher/
│
├── playfair.py              # Python script for encryption & decryption
├── playfair.html            # Web interface with HTML, CSS, JS
├── README.md                # Project documentation
└── assets/ (optional)       # Store screenshots or visuals

⚙️ How to Run the Python Program
Open a terminal and navigate to your project folder.
Run the Python file:
python playfair.py
Enter the key and message when prompted.
The encrypted and decrypted text will be displayed in the terminal.

🌐 How to Run the Web Interface
Save the file as playfair.html.
Open it directly in your browser or start a local server:
python -m http.server 8000


Visit http://localhost:8000/playfair.html
.

Enter your key and message, then click Encrypt or Decrypt.
🧮 Example
Key: MONARCHY
Plaintext: INSTRUMENTS

Output:
Encrypted Text: GATLMZCLRQXAZ
Decrypted Text: INSTRUMENTSX

🧰 Technologies Used
Python 3
HTML5 / CSS3
JavaScript (Vanilla JS)
