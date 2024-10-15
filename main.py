import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image

# Configurable settings
URL = "https://linktr.ee/itrust_finance_limited"  # The URL to encode in the QR code
LOGO_PATH = "/mnt/d/qr-code-generator/logo.png"  # Ensure the logo has a transparent background (PNG)
OUTPUT_FILENAME = "qr_code_no_bg.png"  # Output filename for the QR code
BOX_SIZE = 15  # Size of each box in the QR code
BORDER = 1  # Size of the border around the QR code
FILL_COLOR = "black"  # Color of the QR code
LOGO_SIZE_PERCENTAGE = 10  # Logo size as a percentage of QR code size

def generate_qr_code(url, logo_path=None, output_filename="qr_code_no_bg.png", box_size=10, border=4, 
                     fill_color="black", logo_size_percentage=25):
    # Create QR code instance with high error correction
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    
    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create a QR code image with a transparent background and rounded modules
    qr_image = qr.make_image(fill_color=fill_color, back_color=None,  # No background (transparent)
                             image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

    if logo_path:
        # Open and resize logo, ensuring it has transparency (no background)
        logo = Image.open(logo_path).convert("RGBA")

        # Resize the logo
        logo_size = int(qr_image.size[0] * (logo_size_percentage / 100))
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Calculate position to center the logo
        pos = ((qr_image.size[0] - logo_size) // 2, (qr_image.size[1] - logo_size) // 2)

        # Paste the logo onto the QR code, preserving transparency
        qr_image.paste(logo, pos, logo)

    # Save the final QR code with no background
    qr_image.save(output_filename)
    print(f"QR code saved as {output_filename}")

if __name__ == "__main__":
    generate_qr_code(
        url=URL,
        logo_path=LOGO_PATH,
        output_filename=OUTPUT_FILENAME,
        box_size=BOX_SIZE,
        border=BORDER,
        fill_color=FILL_COLOR,
        logo_size_percentage=LOGO_SIZE_PERCENTAGE
    )
