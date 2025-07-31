import numpy as np

b = -100
m = 78.35
lr = 0.01

epochs= 100

for i in range(epochs):
    loss_slope = -2*np.sum(y-m*X.ravel()-b)
    b = b-(lr*loss_slope)

    y_pred= m*X+b