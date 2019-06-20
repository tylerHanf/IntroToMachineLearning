import matplotlib.pyplot as plt
import numpy as np
from numpy import random as random

class Graph:
    STANDARD_FONT = "Helvetica"
    def __init__(self, numSubPlots, pauseTime):
        self.figure = plt.figure()
        self.numPlots = numSubPlots
        self.pauseTime = pauseTime

    def plot(self, plotNum: int, data, title: str, color: str, *args):
        self.figure.add_subplot(self.numPlots, 1, plotNum)
        if args:
            plt.plot(args, data, color)
        else:
            plt.plot(data, color)
        plt.title(title)
        plt.tight_layout()

    def pause(self):
        plt.pause(self.pauseTime)

    def addFigText(self, x, y, text: str):
        return plt.figtext(x, y, text, fontname=Graph.STANDARD_FONT, fontsize="medium")

class Neuron:
    def __init__(self, weight_count, function):
        random.seed(1)
        self.weights = initial_weights = 2 * random.random((1, weight_count)) - 1
        self.graph = Graph(5, 0.5) 
        self.function = function

    def tanh_derivative(self, x):
        deriv = 1 - np.tanh(x) ** 2
        return deriv

    def step(self, x):
        dot_product = np.dot(x, self.weights)
        tan = np.tanh(dot_product)
        return tan

    def train(self, iterations, train_inputs, train_outputs):
        for i in range(iterations):
            output = self.step(train_inputs)
            error = train_outputs - output
            adjustment = np.dot(train_inputs.T, (error * self.tanh_derivative(output)))
            self.weights += adjustment
            self.plotTrainGraphs(i, output, train_outputs, error, adjustment, iterations)
    
    def plotTrainGraphs(self, stepNum, output, train_outputs, error, adjustment, iterations):
            step = self.graph.addFigText(0.5, 0.2, "Training Step #: " + str(stepNum))
            tFunction = self.graph.addFigText(0.7, 0.2, "Target Function: " + self.function)
            cFunction = self.graph.addFigText(0.1, 0.2, "Current Function: " + str(self.weights[0][0]) + "*x")

            self.graph.plot(1, output, "Output", "b")
            self.graph.plot(1, train_outputs, "Output", "y")
            self.graph.plot(3, adjustment, "Adjustment", "g.", [i for i in range(stepNum+1)])
            self.graph.plot(2, error, "Error", "r")
            self.graph.pause()
            tFunction.remove()
            cFunction.remove()
            step.remove()

def func(x):
    return 2*x

x = [i/100 for i in range(200)]
y = [func(i/100) for i in range(200)]

neuron = Neuron(1, "2*x")

x = np.asarray([x])/100
y = np.asarray([y])/100

x = x.T
y = y.T

neuron.train(100, x, y)

constant = neuron.weights[0][0]


