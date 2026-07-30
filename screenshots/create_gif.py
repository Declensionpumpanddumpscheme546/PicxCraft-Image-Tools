from PIL import Image, ImageDraw, ImageFont

def create_frame(title, color):
    img = Image.new('RGB', (400, 300), color=color)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([10, 10, 390, 290], radius=15, fill=(255, 255, 255))
    draw.text((200, 150), title, fill=color, anchor="mm", align="center")
    return img

frames = []
colors = [(124, 58, 237), (59, 130, 246), (16, 185, 129), (245, 158, 11)]
titles = ['Compress', 'Resize', 'Crop', 'Convert']

for i in range(8):
    frame = create_frame(titles[i % 4], colors[i % 4])
    frames.append(frame)

frames[0].save('preview.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)
print("GIF created!")
