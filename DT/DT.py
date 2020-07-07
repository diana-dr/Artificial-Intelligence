import pprint
import numpy as np
import pandas as pd
eps = np.finfo(float).eps
from numpy import log2 as log


def import_data():
    balance_data = pd.read_csv("DECISION/balance-scale.csv", sep=',', header=None)

    # Printing the dataswet shape
    # print("Dataset Length: ", len(balance_data))
    # print("Dataset Shape: ", balance_data.shape)

    # print("Dataset:\n", balance_data.head())

    return balance_data


def find_entropy(data):
    Class = data.keys()[0]
    entropy = 0
    values = data[Class].unique()
    for value in values:
        fraction = data[Class].value_counts()[value] / len(data[Class])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_entropy_attribute(data, attribute):
    Class = data.keys()[0]
    target_variables = data[Class].unique()
    variables = data[attribute].unique()
    entropy2 = 0

    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(data[attribute][data[attribute] == variable][data[Class] == target_variable])
            den = len(data[attribute][data[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * log(fraction + eps)
        fraction2 = den / len(data)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)


def find_root(data):
    IG = []
    for key in data.keys()[1:]:
        IG.append(find_entropy(data) - find_entropy_attribute(data, key))
    return data.keys()[1:][np.argmax(IG)]


def get_subtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df, tree=None):
    Class = df.keys()[0]
    node = find_root(df)
    attValue = np.unique(df[node])

    if tree is None:
        tree = {}
        tree[node] = {}

    for value in attValue:

        subtable = get_subtable(df, node, value)
        clValue, counts = np.unique(subtable['balanced'], return_counts=True)

        if len(counts) == 1:
            tree[node][value] = clValue[0]
        else:
            tree[node][value] = buildTree(subtable)

    return tree


def predict(inst, tree):
    prediction = 0

    for nodes in tree.keys():

        value = inst[nodes]
        tree = tree[nodes][value]

        if type(tree) is dict:
            prediction = predict(inst, tree)
        else:
            prediction = tree
            break

    return prediction


def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


def main():
    data = import_data()
    df = pd.DataFrame(data.values, columns=['balanced', 'leftweight', 'leftdistance', 'rightweight', 'rightdistance'])

    train_dataset = df
    test_dataset = df[400:]
    tree = buildTree(train_dataset)

    logFile = open('tree.txt', 'w')
    pprint.pprint(tree, logFile)

    predictions = []
    for i in range(len(test_dataset)):
        row = test_dataset.iloc[i]
        prediction = predict(row, tree)
        predictions.append(prediction)

    actual = [row[0] for row in test_dataset.values]
    accuracy = accuracy_metric(actual, predictions)


main()