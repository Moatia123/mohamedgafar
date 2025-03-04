import math

def tanh(x):
    return math.tanh(x)

def dot_product(z, d):
    return sum([x * y for x, y in zip(z, d)])

def neural_network(inputs, weights1, weights2, bias1, bias2):
    hidden_inputs = [dot_product(inputs, w) + bias1 for w in weights1]
    hidden_outputs = [tanh(x) for x in hidden_inputs]
    output_layer_input = dot_product(hidden_outputs, weights2) + bias2
    final_output = tanh(output_layer_input)

    return final_output

inputs = [1.0, 0.5, -0.5]
weights1 = [[0.2, -0.3, 0.4], [-0.1, 0.5, -0.2], [0.3, -0.4, 0.1], [0.2, 0.1, -0.3]]
weights2 = [0.4, -0.5, 0.3, -0.2]

pis1 = 0.4
pis2= 0.3

output = neural_network(inputs, weights1, weights2, pis1, pis2)

print("Network:", output)
