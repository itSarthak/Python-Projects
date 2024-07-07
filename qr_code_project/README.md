# QR Code Generator

## Project Overview

This project is a simple Python application to generate QR codes using the `qrcode` and `pillow` libraries.

## Features

- Generate QR codes from any text or URL
- Save the generated QR code as an image file

## Technologies Used

- Python 3.x
- qrcode library
- pillow library

## Project Structure

qr_code_project/
├── qr_code.py
└── README.md


## How to Use

1. Clone this repository and open it in VS Code:

    ```sh
    git clone https://github.com/itSarthak/Python-Projects/
    cd qr_code_project
    code .
    ```

2. Install the required libraries by running the following command in the terminal:

    ```sh
    pip install qrcode pillow
    ```

3. Open `main.py` and enter the URL you want to generate a QR code for and the file name to save it as.

    Example code snippet:

    ```python
    import qrcode

    # Input the data for the QR code
    data = input("Enter the URL or text to generate QR code: ")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Input the file name to save the QR code
    file_name = input("Enter the file name to save the QR code (e.g., 'qrcode.png'): ")
    img.save(file_name)
    ```

4. Run your script using the command:

    ```sh
    python qr_code.py
    ```

5. Follow the prompts to enter the URL or text to generate the QR code and the file name to save it as. A file with the specified name will be generated in your project directory containing the QR code for the provided data.

## Learning Points

- Understanding how to use external libraries in Python
- Learning to generate and save QR codes as image files
- Basics of image processing with the `pillow` library

