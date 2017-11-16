#
# File: model.py
# Author: Madhu Mohan Nelemane <mmnelemane@suse.com>
#--------------------
# Model Description
#--------------------
# This is the Deep Learning model prepared using a updated training set.
# The immediate training set is a mapping of Bug Ids vs Submit Requests.
# This tells us the list of SRs that were used to resolve a particular BUG Id.
# From this information, we would like to derive more input variables including:
#    1. The title of the bug
#    2. The packages mentioned in the bug title
#    3. The packages mentioned in the bug description
#    4. The packages fixed in the Submit Request
#    5. If possible the type of bug (e.g: boot, kernel panic, segfaults, functional errors etc)
#    6. (TODO): other inputs if that helps better prediction. 
# The classifier uses these as inputs and records the corresponding outputs to
# arrive at a suitable model.
# This model can later be used to predict the most probable package that should be fixed for
# a particular bug. The only input needed for this operation would be the bug ID.
# The initial training set needs to be thoroughly developed and enhanced to incorporate 
# the examples with the above input parameters apart from just the bug ID.
#

import numpy as np

# Initialize w's b's etc as required
def initialize():
    pass

# Generate Training data based on BUG ID and SR number
def training_generator():
    pass

# Place holder for forward/backward propagation functions
def propagation(w, b, X):
    pass

# This is only a sample code and implements a sigmoid function. 
# The correct activation function needs to be identified.
# May be replaced with ReLU OR Leaky ReLU activation functions
def activation_function(w, b, X):
    z = np.dot(W.T, X) + b
    c = 1/(1 + np.exp(-z))
    return c

# The prediction function
def prediction(w, b, X):
    """
    Predicts the possible bug packages using the learned parameters
    Uses Logistic Regression or other suitable methods.
    """
    pass

def optimization(w,b,in_array, out_array, n_iter, l_rate, print_cost):
    """
    Optimizes the values of w and b by running a gradient descent algorithm
    """
    pass

def model(in_train, out_train, in_test, out_test, n_iter, l_rate, print_cost):
    """
    Builds the model 
    """
    pass

