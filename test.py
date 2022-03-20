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

# network[layer][activation/weight/bias][index]
network = hidden_layers     # network = (input) -> hidden layers -> (output)
network.append(output)      # network = (input) -> hidden layers -> output

# create 2d array

for i in range(28):
    array_2d.append([])

for i in range(28):
    for j in range(28):
        pixel = image.getpixel((j,i))
        array.append(pixel)
        array_2d[i].append(pixel)

#invert grayscale value

for i in range(784):
    array[i] = array[i] - 127.5
    array[i] = -array[i]
    array[i] = int(array[i] + 127.5)
    array[i] = array[i] * (1/255)           # change value from 0 to 255, to between 0 and 1

network.insert(0,array)                     # network = input -> hidden layers -> output

network[0] = [network[0],[],[]]             # make it have the same format as other layers

def sigmoid(x):
    if x <= -40:
        x = 0
    else:
        x = float(1/(1+((math.e)**(-x))))
    return x

def sigma(array):
    x = 0
    for i in array:
        x = x + i
    return x

def calculate_network(network):
    for i in range(1,len(network)):
        x = sigma(network[i-1][0])
        for j in range(0,len(network[i][0])):
            network[i][0][j] = sigmoid((network[i][1][j] * float(x) + float(network[i][2][j])))
    output_layer = len(network) - 1
    return network[output_layer][0]

print(calculate_network(network))
