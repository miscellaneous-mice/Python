import tensorflow as tf
import numpy as np
print(tf.__version__)

np_array = np.random.randint(2, size=12)
np_arr = np_array > 0
tensor_bin = tf.constant(np_arr, shape=(3,2,2))
a = tf.constant([False])
print(tf.math.logical_or(tensor_bin, a))