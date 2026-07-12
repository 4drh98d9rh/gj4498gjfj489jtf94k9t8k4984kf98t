# qr_generator.py - Local QR Code Generator for MX-UI
import qrcode
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from typing import Optional

def generate_qr_base64(data: str, size: int = 300, with_text: bool = False, text: Optional[str] = None) -> str:
    """
    Generate QR code as Base64 string for HTML embedding
    
    Args:
        data: Data to encode in QR code
        size: Desired image size in pixels
        with_text: Whether to display text below QR
        text: Custom text to display (uses data if None)
    
    Returns:
        str: Base64 encoded PNG image
    """
    # Calculate box size based on desired image size
    box_size = max(4, size // 30)
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Add text if requested
    if with_text:
        img = img.convert('RGB')
        display_text = text or data
        
        # Truncate long text
        if len(display_text) > 50:
            display_text = display_text[:47] + "..."
        
        # Create new image with space for text
        padding_bottom = 40
        new_img = Image.new('RGB', (img.width, img.height + padding_bottom), 'white')
        new_img.paste(img, (0, 0, img.width, img.height))
        
        draw = ImageDraw.Draw(new_img)
        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        # Center text
        bbox = draw.textbbox((0, 0), display_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (img.width - text_width) // 2
        text_y = img.height + 10
        
        draw.text((text_x, text_y), display_text, fill="black", font=font)
        img = new_img
    
    # Convert to Base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    return f"data:image/png;base64,{img_base64}"

def generate_qr_file(data: str, filename: str = "qr.png", size: int = 20, with_text: bool = False) -> str:
    """
    Generate QR code and save to file
    
    Args:
        data: Data to encode
        filename: Output filename
        size: QR box size
        with_text: Whether to add text below QR
    
    Returns:
        str: Path to saved file
    """
    qr = qrcode.QRCode(version=1, box_size=size, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    if with_text:
        img = img.convert('RGB')
        new_img = Image.new('RGB', (img.width, img.height + 60), 'white')
        new_img.paste(img, (0, 0, img.width, img.height))
        
        draw = ImageDraw.Draw(new_img)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), data, font=font)
        text_width = bbox[2] - bbox[0]
        draw.text(((img.width - text_width) // 2, img.height + 10), data, fill="black", font=font)
        img = new_img
    
    img.save(filename)
    return filename

# Simple function for quick usage
def qr(data, filename="qr.png", size=20, with_text=False):
    """Quick QR generation function"""
    return generate_qr_file(data, filename, size, with_text)