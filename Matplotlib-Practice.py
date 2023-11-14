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
plt.annotate('Wrong Value',
            xy=(14,23),
            xytext=(20,30), color='red',
            arrowprops=dict(facecolor='r', edgecolor='black', alpha=0.5))
plt.title('Playing with Plots')
plt.xlabel('time', fontsize=15, color='green')
plt.ylabel('temperature', fontsize=15, color="green")
plt.tick_params(axis='y',
                color='red',
                labelcolor='green',
                labelsize='xx-large')
plt.legend()
plt.show()

plt.figure(figsize=(20,5))
x = range(len(data['timestamp']))
plt.ylim(21.4,22.5)
plt.plot(x,data["Ambient Temperature"],
         color = 'purple',
         marker = 'd',
         label = "Export" )
plt.tick_params(axis='y',
                color='green',
                labelcolor= 'green')
plt.xlabel("Time (ISO 8601)")
plt.ylabel("Ambient Temperature")
plt.minorticks_on()
plt.grid(which = 'minor', color='orange')
plt.grid(color='red', linewidth=2)
plt.show()