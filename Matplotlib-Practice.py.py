import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("export_1662385061.csv") # load data

plt.plot([23,14,43,53],
         [14,23,29,41],
         color = 'purple',
         linestyle='--',
         linewidth=2,
         marker = 'd',
         markersize=10,
         label='Water')
plt.title('Playing with Plots')
plt.xlabel('time', fontsize=15, color='green')
plt.ylabel('temperature', fontsize=15, color="green")
plt.tick_params(axis='y',
                color='red',
                labelcolor='green',
                labelsize='xx-large')
#plt.legend()
#plt.show()

plt.figure(figsize=(10,5))
x = range(len(data['timestamp']))
plt.plot(x,data["Ambient Temperature"],
         color = 'pink',
         marker = 'd',
         label = "Export" )
plt.tick_params(axis='y',
                color='green',
                labelcolor= 'green')
plt.xlabel("timestamp")
plt.ylabel("Ambient Temperature")
plt.legend()
plt.show()