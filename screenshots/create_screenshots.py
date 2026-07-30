from PIL import Image, ImageDraw

def create_screenshot(filename, title, subtitle, bg_color=(124, 58, 237)):
    # Create image
    img = Image.new('RGB', (800, 600), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw rounded rectangle background
    draw.rounded_rectangle([20, 20, 780, 580], radius=20, fill=(255, 255, 255))
    
    # Add title
    draw.text((400, 200), title, fill=bg_color, anchor="mm", align="center")
    
    # Add subtitle
    draw.text((400, 280), subtitle, fill=(100, 100, 100), anchor="mm", align="center")
    
    # Add phone frame
    draw.rounded_rectangle([300, 350, 500, 550], radius=20, outline=bg_color, width=3)
    
    img.save(filename)

create_screenshot('screenshot-1.png', 'PicxCraft Android', '114+ Free Image Tools')
create_screenshot('screenshot-2.png', 'Image Compression', 'Reduce image size instantly')
create_screenshot('screenshot-3.png', 'Image Resize', 'Resize for any platform')
create_screenshot('screenshot-4.png', 'Crop & Edit', 'Professional editing tools')
print("Screenshots created!")
