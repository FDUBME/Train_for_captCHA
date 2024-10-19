from PIL import Image, ImageDraw, ImageFont
import random
import  os


# import torch
#
# print(torch.cuda.is_available())

background_paths = []

Chinese_list = []

def generate_image_with_Chinese():
    # 随机选择一个背景图
    background_image_path = random.choice(background_paths)
    background_image = Image.open(background_image_path)

    # 创建绘图对象
    draw = ImageDraw.Draw(background_image)

    # 图像大小
    image_width, image_height = background_image.size

    # 随机选取几个汉字
    num_hanzi = random.randint(1, 5)  # 每张图随机放1到5个汉字
    selected_hanzi = random.sample(hanzi_list, num_hanzi)

    for hanzi in selected_hanzi:
        # 随机字体大小和颜色
        font_size = random.randint(30, 60)
        font = ImageFont.truetype(font_path, font_size)
        font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # 随机位置
        x_position = random.randint(0, image_width - font_size)
        y_position = random.randint(0, image_height - font_size)

        # 在图片上绘制汉字
        draw.text((x_position, y_position), hanzi, font=font, fill=font_color)

    # 保存生成的图像
    output_image_path = f'/mnt/data/generated_hanzi_image_{random.randint(1000, 9999)}.png'
    background_image.save(output_image_path)
    print(f'生成图像并保存在: {output_image_path}')


if __name__ == '__main__':

    # 生成多张图像
    for _ in range(5):
        generate_image_with_Chinese()