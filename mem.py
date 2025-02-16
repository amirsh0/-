from PIL import Image, ImageDraw, ImageFont


print('Генератор мемов запущен!')

top_text = input('Введите верхний текст мема: ')
bottom_text = input('Введите нижний текст мема: ')

print(top_text, bottom_text)

print("Список картинок:")
print("1.Первый мем")
print("2.Второй мем")
print('3.Третий мем')
print('4.Четвертый мем')

image_number = int(input('Ведите номер картинки: '))

if image_number == 1:
    image_file = "15089189.png"
elif image_number == 2:
    image_file ="1628624724_preview_bec6a5031e5060a512c4da09d019825b.jpg"
elif image_number == 3:
    image_file = 'f15c282s-960.jpg'
elif image_number == 4:
    image_file = 'png-clipart-el-risitas-internet-meme-laughter-internet-forum-parody-issou-face-head.png'

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill='black')

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill='black')

image.save("new_meme.jpg")

