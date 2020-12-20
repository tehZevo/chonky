# Chonky
Creates sparse mappings between two NumPy array shapes based on a string key.

Ever wanted to map an array of shape [32] to random-looking locations within an array of shape [64, 64, 64] (I did.)?
Well that's what this does.

## Usage
```python
import numpy as np
from chonky import create_mapping

#define input, output shape, and the key to map between them
input_shape = [4]
output_shape = [4, 4]
key = "Hello world!"
#create some zeros
chunk = np.zeros(output_shape)
#create the mapping
mapping = create_mapping(key, input_shape, output_shape)
#write some ones to random-looking (but consistent) locations within the target array
chunk[mapping] = np.ones(input_shape)

print(chunk)
# [[1. 0. 1. 1.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 1. 0. 0.]]
