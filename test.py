from PIL import Image
from PIL import ImageOps

image = Image.open("dataset/numbers/9/1.png")
image = ImageOps.grayscale(image)
image = image.resize((28,28))

array = []
array_2d = []

for i in range(28):
    array_2d.append([])

for i in range(28):
    for j in range(28):
        pixel = image.getpixel((j,i))
        array.append(pixel)
        array_2d[i].append(pixel)

for i in range(28):
    print(array_2d[i])

print("\n")
print(array)
print(array_2d)