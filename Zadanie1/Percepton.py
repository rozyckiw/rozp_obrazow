import numpy as np
import datetime
from random import shuffle

class Percepton:


    #eg. hidden_layers = [2,3,4] - 3 warstwy po 2, 3 i 4 neurony

    def __init__(self, inputLen, outputLen, hidden_layers, ifBias = False,
                 batch_size = 0):


        if(type(inputLen) is list):

            self.input      = 1

            for inputL in inputLen:

                self.input *= inputL

        else: self.input = inputLen

        self.output     = outputLen
        self.ifBias     = ifBias
        self.network    = self.generateNetwork(hidden_layers)
        self.propabilities = []
        self.batchSize = batch_size
        self.iterations = 0
        self.classes = {"linen": 0, "salt": 1, "straw": 2, "wood": 3}


    def runEpochs(self, xDataset, yDataset, learnigRate, noEpochs, epsilon):

        for epoch in range(noEpochs):

            lastOutput = [node['output'] for node in self.network[-1]]
            for (x, yLabel) in zip(xDataset, yDataset):

                y = self.classes[yLabel]
                # Forward-pass training example into network (updates node output)
                if(x.ndim > 1): x = np.reshape(x, (-1, 1))

                self.feedforward(x)
                # Create target output
                y_target = np.zeros(self.output, dtype=np.int)
                y_target[y] = 1
                # Backward-pass error into network (updates node delta)
                self._backward_pass(y_target)
                # Update network weights (using updated node delta and node output)
                self._update_weights(x, l_rate=learnigRate)

            self.iterations = epoch + 1

            if(epsilon > 0 and any(lastOutput)):

                if(self.ifEpsilonReached(self.getError(lastOutput), epsilon)):

                    return

            if(epoch % 50 == 0):

                print("[{0}] Epoch {1} running..".format(datetime.datetime.now(), epoch))


    #
    # Train network
    #
    def train(self, X_train, y_train, l_rate=0.5, n_epochs=1000, epsilon=0):

        idxs = np.arange(len(X_train))
        shuffle(idxs)
        X_train = X_train[idxs]
        y_train = y_train[idxs]

        if(self.batchSize == 0):

            self.runEpochs(X_train, y_train, l_rate, n_epochs, epsilon)

        else:

            noGroups = int(np.ceil(len(X_train) / self.batchSize))
            xBatches = self.chunker_list(X_train, noGroups)
            yBatches = self.chunker_list(y_train, noGroups)
            ident = 0

            for x, y in zip(xBatches, yBatches):

                x = np.array(x)
                y = np.array(y)
                self.runEpochs(x, y, l_rate, n_epochs, epsilon)
                ident += 1

                print("[{0}] Batch {1}/{2} running..".format(datetime.datetime.now(), ident, noGroups))


    #
    # Predict most probable class labels for a data set X
    #
    def predict(self, X):

        y_predict = []
        for i, x in enumerate(X):

            x = np.array(x)
            if(x.ndim > 1): x = np.reshape(x, (-1, 1))
            output = self.feedforward(x)  # output class probabilities
            self.propabilities.append(max(output))

            for key, val in self.classes.iteritems():

                if(val == np.argmax(output)):

                    y_predict.append(key)

        return y_predict


    def generateNetwork(self, hidden_layers):

        def buildLayer(input, output, ifBias):

            layer = list()
            if(ifBias): input += 1

            for idx_out in range(output):

                weights = list()

                for idx_in in range(input):

                    weights.append(np.random.rand() * 2 - 1)

                layer.append({"weights": weights,
                              "output": None,
                              "delta": None})

            return layer

        allLayers = []

        if(len(hidden_layers) == 0):

            allLayers.append(buildLayer(self.input, self.output, self.ifBias))

        else:

            allLayers.append(buildLayer(self.input, hidden_layers[0], self.ifBias))

            for i in range(1, len(hidden_layers)):

                allLayers.append(buildLayer(hidden_layers[i - 1], hidden_layers[i], self.ifBias))

            allLayers.append(buildLayer(hidden_layers[-1], self.output, self.ifBias))

        return allLayers


    def getError(self, lastOutput):

        errors = [abs(lastOutput[j] - node['output']) for j, node in enumerate(self.network[-1])]
        return errors


    #
    # Forward-pass input -> output and save to network node values
    # This updates: node['output']
    #
    def feedforward(self, x):

        # Weighted sum of inputs with no bias term for our activation
        def activate(weights, inputs, ifBias):

            if(ifBias):

                inputs = list(inputs)
                inputs.append(np.array([1]))
                inputs = np.array(inputs)

            inputs = inputs.ravel()
            return inputs.dot(weights)


        input = x
        for i, layer in enumerate(self.network):

            output = []

            for node in layer:
                # Compute activation and apply transfer to it
                # activation = activate(node['weights'], node['bias'], input)
                activation = activate(node['weights'], input, self.ifBias)

                if(i == len(self.network) - 1): node['output'] = activation
                else: node['output'] = self.sigmoid(activation)

                output.append(node['output'])

            input = np.array(output)

            if(i == len(self.network) - 1):

                input = self.softmax(input)
                for j in range(len(layer)):

                    layer[j]['output'] = input[j]

        return input


    def _backward_pass(self, target):

        # Perform backward-pass through network to update node deltas
        n_layers = len(self.network)

        for i in reversed(range(n_layers)):

            layer = self.network[i]

            # Compute errors either:
            # - explicit target output difference on last layer
            # - weights sum of deltas from frontward layers
            errors = list()

            if i == n_layers - 1:

                # Last layer: errors = target output difference
                for j, node in enumerate(layer):

                    error = target[j] - node['output']
                    errors.append(error)

            else:

                # Previous layers: error = weights sum of frontward node deltas
                for j, node in enumerate(layer):

                    error = 0.0
                    for node in self.network[i + 1]:

                        error += node['weights'][j] * node['delta']

                    errors.append(error)

            # Update delta using our errors
            # The weight update will be:
            # dW = learning_rate * errors * transfer' * input
            #    = learning_rate * delta * input
            for j, node in enumerate(layer):

                node['delta'] = errors[j] * self.sigmoid_derivative(node['output'])


    def _update_weights(self, x, l_rate=0.3):

        # Update weights forward layer by layer
        for i_layer, layer in enumerate(self.network):

            # Choose previous layer output to update current layer weights
            if i_layer == 0:

                inputs = x

            else:

                inputs = np.zeros(len(self.network[i_layer - 1]))

                for i_node, node in enumerate(self.network[i_layer - 1]):

                    inputs[i_node] = node['output']

            # Update weights using delta rule for single layer neural network
            # The weight update will be:
            # dW = learning_rate * errors * transfer' * input
            #    = learning_rate * delta * input
            for node in layer:

                for j, input in enumerate(inputs):

                    dW = l_rate * node['delta'] * input
                    node['weights'][j] += dW


    def ifEpsilonReached(self, errors, epsilon):

        if(not any(delta > epsilon for delta in errors)):
            return True
        return False


    def chunker_list(self, seq, size):
        return list((seq[i::size] for i in range(size)))
		
	
    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))
		
	
    def sigmoid_derivative(self, x):
        return x * (1.0 - x)


    def softmax(self, A):

        expA = np.exp(A)
        return expA / expA.sum()