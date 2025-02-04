from PIL import Image, ImageDraw, ImageFont
import os

WATERMARK_TEXT = "山雀大王\noloiyy@163.com"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Ubuntu 默认字体
FONT_SIZE = 36
IMAGE_DIR = "images"

def add_watermark(image_path):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    # 创建水印
    watermark = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(WATERMARK_TEXT, font)
    position = (width - text_width - 20, height - text_height - 20)

    draw.text(position, WATERMARK_TEXT, font=font, fill=(255, 255, 255, 128))

    # 合并图片
    watermarked = Image.alpha_composite(img, watermark)
    watermarked.convert("RGB").save(image_path, "JPEG")

def process_images():
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            add_watermark(os.path.join(IMAGE_DIR, filename))

if __name__ == "__main__":
    process_images()
