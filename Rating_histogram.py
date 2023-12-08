%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Drop missing values
review_data.dropna(inplace=True)

df = review_data.sort_values(by ='Rating', ascending = True)
plt.hist(df.Rating,  bins = 5, color ='Blue', rwidth=0.9, label = "Rating");
plt.legend()
