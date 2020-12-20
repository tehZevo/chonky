import hashlib
import numpy as np

def create_mapping(key, in_shape, out_shape):
    locs = []
    len_out_shape = np.prod(out_shape)

    for i in range(np.prod(in_shape)):
        k = "{},{}".format(key, i)
        h = int(hashlib.sha256(k.encode('utf-8')).hexdigest(), 16) % len_out_shape
        locs.append(h)

    return np.unravel_index(locs, out_shape)
