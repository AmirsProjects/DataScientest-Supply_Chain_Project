%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_sorted = review_data.sort_values(by ='Rating', ascending = True)
plt.hist(df_sorted.Rating,  bins = 5, color ='Blue', rwidth=0.9, label = "Rating");
plt.legend()
