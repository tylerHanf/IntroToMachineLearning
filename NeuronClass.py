import numpy as np
from numpy import random
import matplotlib.pyplot as plt

/*
    Represents a single trainable neuron
    using tanh function as 
*/
class Neuron:
    def __init__(self, weight_count):
        random.seed(1)
        self.weights = initial_weights = 2 * random.random((1,1)) - 1

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2

    def step(self, x):
        dot_product = np.dot(x, self.weights)
        return np.tanh(dot_product)

    def train(self, iterations, train_inputs, train_outputs):
        for i in range(iterations):
            output = self.step(train_inputs)
            error = train_outputs - output
            adjustment = np.dot(train_inputs.T, (error * self.tanh_derivative(output)))
            self.weights += adjustment
