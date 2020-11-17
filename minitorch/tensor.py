
import numpy as np
# import cupy as cp

from minitorch.dtype import float32

class NDArray(object):
    def __init__(self, *shape):
        super().__init__()
        self.data = np.empty(*shape)

    def __repr__(self):
        return self.data.__repr__()

    def __str__(self):
        return self.data.__str__()

class Tensor(object):
    def __init__(self):
        super().__init__()
        self.data = None
        self.grad = None

    def __repr__(self):
        return self.data.__repr__()

    def __str__(self):
        return self.data.__str__()


def zeros(*shape, dtype=float32):
    ret = Tensor()
    ret.data = NDArray(shape)
    return ret

def tensor(data):
    pass

