import numpy as np

def smoothen(xs, window):
    if window == 0:
        return xs
    else:
        return np.moveaxis(np.array([
            xs[..., t:t+window].sum(axis = len(xs.shape) - 1) / window
            for t in range(xs.shape[-1] - window+1)
        ]), 0, len(xs.shape) - 1)

def lse(xs, ys):
    return (xs - ys).dot(xs - ys)