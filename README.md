

# QR Code Generator with High Error Correction and Transparent Logo

This Python script generates a customizable QR code with high error correction and an option to include a logo. The QR code and logo will have no background, making it perfect for use in designs where transparency is needed.

## Features

- Generates a QR code with **high error correction** (30% of the code can be damaged and still be scannable).
- Supports **transparent backgrounds** for both the QR code and the logo.
- Allows **custom logo placement** in the center of the QR code, ensuring the logo retains its transparency.
- Offers customizable options for **box size**, **border size**, **QR code color**, and **logo size**.

## Requirements

- Python 3.x
- Required Python packages:
  - `qrcode[pil]`
  - `Pillow`

### Installation

1. Clone the repository or download the script.
2. Install the required Python packages:

   ```bash
   pip install qrcode[pil] Pillow
   ```

## Usage

1. **Configure the settings**:
   - Update the `URL` variable in the script to the URL or data you want to encode in the QR code.
   - Set the `LOGO_PATH` variable to the path of the logo file (must be a **transparent PNG**). Set it to `None` if no logo is needed.
   - Customize the output filename, box size, border size, and other settings as needed.

2. **Run the script**:

   ```bash
   python main.py
   ```

3. The script will generate the QR code and save it to the specified output file. If a logo is included, it will be centered in the QR code with the appropriate size.

### Example Configuration

```python
URL = "https://google.com"  # The URL to encode in the QR code
LOGO_PATH = "/path/to/transparent_logo.png"  # Path to the logo image file (set to None if no logo is desired)
OUTPUT_FILENAME = "qr_code_no_bg.png"  # Output filename for the generated QR code
BOX_SIZE = 10  # Size of each box in the QR code
BORDER = 4  # Size of the border around the QR code
FILL_COLOR = "black"  # Color of the QR code
LOGO_SIZE_PERCENTAGE = 25  # Logo size as a percentage of QR code size
```

## Output

- **Transparent Background**: The QR code will be generated without a background, and the logo (if included) will retain its transparency.
- **High Error Correction**: The QR code is designed to be scannable even if part of the code is damaged, due to the high error correction setting.

## Customization

- **Box Size**: Adjust the `BOX_SIZE` parameter to control the size of each module (square) in the QR code.
- **Border**: Modify the `BORDER` parameter to control the width of the quiet zone around the QR code.
- **Logo Size**: Use `LOGO_SIZE_PERCENTAGE` to set the size of the logo as a percentage of the QR code size.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributions

Feel free to fork the project and contribute by submitting pull requests. Any suggestions for improvements are welcome!

---

This `README.md` provides the necessary details to understand, configure, and run the QR code generator.