
# import numpy
import numpy as np

# create default dictionary, which is a dictionary with a default value using lambda and np.zeros
default_dict = {lambda: np.zeros(3)}

# now, add a key to the dictionary
default_dict[1] = np.ones(3)


