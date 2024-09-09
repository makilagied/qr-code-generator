import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image
import sys

def generate_qr_code_with_logo(url, logo_path, output_filename="qr_code_with_logo.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image with rounded modules
    qr_image = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

    # Open the logo image
    logo = Image.open(logo_path)

    # Calculate the size of the logo (e.g., 1/4 of the QR code size)
    logo_size = qr_image.size[0] // 4

    # Resize the logo
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to paste the logo (center)
    pos = ((qr_image.size[0] - logo_size) // 2, (qr_image.size[1] - logo_size) // 2)

    # Paste the logo
    qr_image.paste(logo, pos, logo)

    # Save the final image
    qr_image.save(output_filename)
    print(f"QR code with logo saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        logo_path = sys.argv[2]
        generate_qr_code_with_logo(url, logo_path)
    else:
        print("Please provide a URL and logo file path as command-line arguments.")
        print("Usage: python script_name.py <url> <logo_path>")