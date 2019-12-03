import numpy as np

x = np.array([0.0, 1.0, 1.0, 2.0])
y = np.array([0.0, 1.0, 2.0, 1.0])


def gradient_descent(x, y):
    w0 = np.random.rand()
    w1 = np.random.rand()
    w2 = np.random.rand()

    iterations = 1000
    learning_rate = 0.001

    for i in range(iterations):
        y_predicted = w2 * (x ** 2) + w1 * x + w0
        grad2 = -2 * sum((x**2)*(y-y_predicted)) 
        grad1 = -2 * sum(x*(y-y_predicted))
        grad0 = -2 * sum(y-y_predicted)

        w2 = w2 - learning_rate * grad2
        w1 = w1 - learning_rate * grad1
        w0 = w0 - learning_rate * grad0

        print(w0, w1, w2)

gradient_descent(x, y)


