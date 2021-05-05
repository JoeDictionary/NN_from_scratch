import math
import random

import numpy as np


softmax():
	pass


def sigmoid(x):
	return (1 / (1 + math.exp(-x)))
sigmoid_v = np.vectorize(sigmoid)

def relu(x):
	return np.maximum(x, 0)

input_layer = np.full(28 * 28, 1)
input_layer_w = np.full((100, 28 * 28), 1)

hidden_layer = np.full(100, 1)
hidden_layer_w = np.full((10, 100), 1)

output_layer = np.full(10, 1)

print(sigmoid_v(input_layer_w))
