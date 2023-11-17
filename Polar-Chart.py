import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Football.csv") # Load Data from football csv
plt.figure(figsize= (8,8))

ax = plt.subplot(111, polar=True)

# Plot
bars = ax.bar('Dribble', 'Shoot')

ax.plot(data['Name'], data['Dribble'], data['Shoot'], data['Physic'], data['Speed'], data['Defense'])

plt.title('Best Overall Football Player', fontsize=10, color='b')

#plt.stackplot('Shoot', 'Physic', 'Speed', 'Defense')


plt.show()


