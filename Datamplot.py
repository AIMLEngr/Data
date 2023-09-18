import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# create Pandas DataFrame from csv
df = pd.read_csv('DHA.csv')

#create a list of unique bed values
bed_values = df['Bed'].unique()

# Plot multiple lines
plt.figure()

#Plot a line for each bed value
for bed_value in bed_values:
  df_filtered = df[df['Bed'] == bed_value]
  plt.plot(df_filtered['Size'], df_filtered['Price'], label=f'{bed_value}Beds')

plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Price vs. Size by Number of Beds')
plt.legend()
plt.show()