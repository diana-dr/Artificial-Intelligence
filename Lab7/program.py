import numpy as np

def read_data(filename):
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    y = []
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            data = line.split(' ')
            x1.append(float(data[0]))
            x2.append(float(data[1]))
            x3.append(float(data[2]))
            x4.append(float(data[3]))
            x5.append(float(data[4]))
            y.append(float(data[5]))

    return x1, x2, x3, x4, x5, y


def cost_function(X, Y, B):
    m = len(Y)
    J = np.sum((X.dot(B) - Y) ** 2)/(2 * m)
    return J


def gradient_descent(X, Y, B, alpha, iterations):
    cost_history = [0] * iterations
    m = len(Y)

    for iteration in range(iterations):
        h = X.dot(B)
        loss = h - Y
        gradient = X.T.dot(loss) / m
        B = B - alpha * gradient
        cost = cost_function(X, Y, B)
        cost_history[iteration] = cost

    return B, cost_history


def rmse(Y, Y_pred):
    rmse = np.sqrt(sum((Y - Y_pred) ** 2) / len(Y))
    return rmse


def r2_score(Y, Y_pred):
    mean_y = np.mean(Y)
    ss_tot = sum((Y - mean_y) ** 2)
    ss_res = sum((Y - Y_pred) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


def Main():

    x1, x2, x3, x4, x5, y = read_data("data.txt")
    m = len(x1)
    x0 = np.ones(m)
    X = np.array([x0, x1, x2, x3, x4, x5]).T
    B = np.array([0, 0, 0, 0, 0, 0])
    Y = np.array(y)
    alpha = 0.0001

    newB, cost_history = gradient_descent(X, Y, B, alpha, 100000)
    print(cost_history[-1])

    Y_pred = X.dot(newB)

    print(rmse(Y, Y_pred))
    print(r2_score(Y, Y_pred))
