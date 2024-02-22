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

def avgnb(m):
    out = np.empty_like(m)
    nr, nc = m.shape[:2]
    
    for r, c in product(range(nr), range(nc)):
        val, n = 0.0, 0.0
        for i in range(max(0, r-1), min(nr, r+2)):
            for j in range(max(0, c-1), min(nc, c+2)):
                n += 1.0
                val += m[i, j]
        out[r, c] = val / n
    
    return out