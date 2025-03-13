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
base_size = 13
sns.set_style("whitegrid")
palette = sns.color_palette("Set2")
sns.set_palette(palette)
sns.set_context("talk")

# matplotlib settings
plt.rcParams['figure.figsize'] = (8, 3.5)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 12

# Define colors
red_pink   = "#e64173"
turquoise  = "#20B2AA"
orange     = "#FFA500"
red        = "#fb6107"
blue       = "#181485"
navy       = "#150E37FF"
green      = "#8bb174"
yellow     = "#D8BD44"
purple     = "#6A5ACD"
slate      = "#314f4f"
