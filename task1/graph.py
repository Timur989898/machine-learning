import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/train.csv")

plt.xlabel('Class')
plt.ylabel('Count of passengers')
plt.title('Class/Passengers')

data.Pclass.hist(color=(0, 0, 0))

plt.show()

