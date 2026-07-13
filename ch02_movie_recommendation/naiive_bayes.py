# %% packages
import numpy as np
from collections import defaultdict

# %% define dataset
X_train = np.array(
    [
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0],
        [1, 1, 0]
    ]
)
Y_train = ["Y", "N", "Y", "Y"]
X_test = np.array([1, 1, 0])

# %% define function to get label indices
def get_label_indices(labels):
    label_indices = defaultdict(list)
    for index, label in enumerate(labels):
        label_indices[label].append(index)
    return label_indices
    
label_indices = get_label_indices(Y_train)
print(label_indices)

# %%
def get_prior(labels_indices : defaultdict[str, list]):
    prior = { label : len(indices) / sum(labels_indices.values()) for label, indices in labels_indices.items() }
    return prior

prior = get_prior(label_indices)
print(prior)

# %%