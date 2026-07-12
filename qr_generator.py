# simple_qr.py - One function QR generator
import qrcode
from PIL import Image, ImageDraw, ImageFont

def qr(data, filename="qr.png", size=20, with_text=False):
    """
    Generate QR code
    
    Args:
        data: Text or URL
        filename: Output file
        size: QR size
        with_text: Add text below QR
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
        
        tw = draw.textlength(data, font=font)
        draw.text(((img.width - tw) // 2, img.height + 10), data, fill="black", font=font)
        img = new_img
    
    img.save(filename)
    print(f"✅ Saved: {filename}")

# Usage
qr("https://google.com")                    # Simple
qr("Hello World!", "hello.png", 25, True)   # With text