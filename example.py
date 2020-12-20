import numpy as np
import time

from chonky import create_mapping

#define input, output shape, and the key to map between them
input_shape = [4]
output_shape = [4, 4]
key = "Hello world!"

#create some zeros
chunk = np.zeros(output_shape)

t = time.time()
#create a sparse mapping between the input and output spaces
mapping = create_mapping(key, input_shape, output_shape)
print("took", time.time() - t, "seconds")

#write some ones to random-looking (but consistent) locations within the target array
chunk[mapping] = np.ones(input_shape)

print(chunk)
