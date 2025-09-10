import qrcode
from PIL import Image
import io

def create_qr_code(data, filename=None, size=10, border=4):
    """Создает QR-код для переданных данных"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    if filename:
        img.save(filename)
        print(f"QR-код сохранен как {filename}")
    
    return img

def create_qr_with_logo(data, logo_path, filename=None):
    """Создает QR-код с логотипом в центре"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Добавляем логотип
    try:
        logo = Image.open(logo_path)
        logo = logo.resize((60, 60))
        
        # Размещаем логотип в центре
        pos = ((qr_img.size[0] - logo.size[0]) // 2,
               (qr_img.size[1] - logo.size[1]) // 2)
        qr_img.paste(logo, pos)
        
        if filename:
            qr_img.save(filename)
            print(f"QR-код с логотипом сохранен как {filename}")
        
        return qr_img
    except FileNotFoundError:
        print("Логотип не найден, создан обычный QR-код")
        return qr_img

# Пример использования
print("=== ГЕНЕРАТОР QR-КОДОВ ===")

# Простой QR-код
create_qr_code("https://www.python.org", "python_qr.png")

# QR-код с текстом
create_qr_code("Привет! Это мой QR-код", "hello_qr.png")

# QR-код с контактной информацией
contact_info = """BEGIN:VCARD
VERSION:3.0
FN:Иван Иванов
ORG:Моя Компания
TEL:+7-123-456-7890
EMAIL:ivan@example.com
URL:https://example.com
END:VCARD"""
create_qr_code(contact_info, "contact_qr.png")

print("QR-коды созданы!")
