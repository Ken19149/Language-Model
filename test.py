from PIL import Image
from PIL import ImageOps
import math

image = Image.open("test/test.png")
image = ImageOps.grayscale(image)
image = image.resize((28,28))

array = []      # input
array_2d = []

# layers = [[activations],[weights],[bias]]
# the number is random for now

layer_1 = [[0.72,0.23,0.76], [3,2,-4], [8,-6,4]]    # 3 activations
layer_2 = [[0.55,0.31], [-2,3], [7,0.2]]    # 2 activations
layer_3 = [[0.12,0.7,0.42,0.98], [2,-4,-2,1], [1,2,3,4]]    # 4 activations

hidden_layers = [layer_1,layer_2,layer_3]

output = [[0.7,0.4,0.3,0.15], [2,3,1,4], [-3,-5,6,2]] # 4 output for simplicity for now

print("hidden layer",hidden_layers)

network = hidden_layers

print("network before",network)
network.append(output)  # network[layer][activation/weight/bias][index]

print("network after",network)
print(network[0][0][1])

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
    array[i] = array[i] * (1/255)           # change value from 0 to 255, to between 0 and 1

print(array)

network.insert(0,array)

def sigmoid(x):
    x = 1/(1+((math.e)**(-x)))
    return x

sum = 0
for i in array:
    sum = sum + i

print(sum)
print(network)
