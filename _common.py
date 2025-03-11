import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

from scipy.stats import (
    norm, binom, expon, t, chi2, pareto, ttest_1samp, ttest_ind, sem, bernoulli, mannwhitneyu, uniform, gamma
)

import warnings
warnings.filterwarnings("ignore")

np.random.seed(73)

# custom color palette
sns.set_style("whitegrid")
palette = sns.color_palette("Set2")
sns.set_palette(palette)
sns.set_context("talk")