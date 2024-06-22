import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()
# plt.show()

# Scatter Plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Pulse')
plt.savefig('plot.png')
