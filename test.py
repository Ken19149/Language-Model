from PIL import Image
from PIL import ImageOps

image = Image.open("test/test.png")
image = ImageOps.grayscale(image)
image = image.resize((28,28))

array = []
array_2d = []


# create 2d array

for i in range(28):
    array_2d.append([])

for i in range(28):
    for j in range(28):
        pixel = image.getpixel((j,i))
        array.append(pixel)
        array_2d[i].append(pixel)

'''
for i in range(28):
    print(array_2d[i])
'''

'''
print("\n")
print(array)
print(array_2d)
'''

#invert grayscale value

for i in range(784):
    array[i] = array[i] - 127.5
    array[i] = -array[i]
    array[i] = int(array[i] + 127.5)

print(array)
