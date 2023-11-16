import matplotlib.pyplot as plt
<<<<<<< HEAD
import matplotlib.dates as mdates
=======
>>>>>>> 18925d1ce6de395f9e637a5ef775a3866633bf9b
import pandas as pd
import numpy as np

# Practice Plot
<<<<<<< HEAD
plt.figure(figsize=(9, 4))
=======
>>>>>>> 18925d1ce6de395f9e637a5ef775a3866633bf9b
plt.plot([23,14,43,53],
         [14,23,29,41],
         color = 'purple',
         linestyle='--',
         linewidth=5,
         marker = 'o',
         markersize=12,
         label='Water')
plt.annotate('Wrong Value',
            xy=(14,23),
            xytext=(20,30), color='red',
            arrowprops=dict(facecolor='r', edgecolor='black', alpha=0.5))
plt.title('Playing with Plots')
plt.xlabel('Time', fontsize=15, color='green')
plt.ylabel('Temperature', fontsize=15, color="green")
plt.tick_params(axis='y',
                color='green',
                labelcolor='red',
                labelsize='x-large')
plt.tick_params(axis='x',
                color='green',
                labelcolor='red',
                labelsize='x-large')
<<<<<<< HEAD
plt.tight_layout()
plt.savefig("Practice-Plot.png", dpi=300)
=======
>>>>>>> 18925d1ce6de395f9e637a5ef775a3866633bf9b
plt.show()




# Working with CSV file
data = pd.read_csv("export_1662385061.csv") # Load Data

# Convert 'timestamp' to datetime
<<<<<<< HEAD
#data['timestamp'] = pd.to_datetime(data['timestamp'])
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Start a new figure
plt.figure(figsize=(9, 4))

# First y-axis for 'Exciter Field Current'
line1, = plt.plot(df['timestamp'], df['Exciter Field Current'], color='purple', linestyle='--', linewidth=1, label='Exciter Field Current')

# Second y-axis for 'Line Current'
ax2 = plt.twinx()
line2, = ax2.plot(df['timestamp'], df['Line Current'], color='green', linewidth=1,  label='Line Current')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
=======
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Start a new figure
plt.figure(figsize=(19, 5))

# First y-axis for 'Exciter Field Current'
line1, = plt.plot(data['timestamp'], data['Exciter Field Current'], color='purple', linestyle='--', linewidth=1, label='Exciter Field Current')

# Second y-axis for 'Line Current'
ax2 = plt.twinx()
line2, = ax2.plot(data['timestamp'], data['Line Current'], color='green', linewidth=1,  label='Line Current')
>>>>>>> 18925d1ce6de395f9e637a5ef775a3866633bf9b

# Set the labels for x-axis and y-axes
plt.xlabel("Time (ISO 8601)")
plt.ylabel("Exciter Field Current", color='purple')
ax2.set_ylabel("Line Current", color='green')

# Customize tick parameters
plt.tick_params(axis='y', colors='purple')
ax2.tick_params(axis='y', colors='green')

# Create legends for both lines
plt.legend([line1, line2], ["Exciter Field Current", "Line Current"], loc='upper left')

# Set limit for the y-axis
plt.ylim(40)
ax2.set_ylim()

# Add title
plt.title('Exciter Field Current and Line Current Over Time')

<<<<<<< HEAD
plt.annotate('20/04/21', xy=(0.02,1), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', color='red', fontsize=12)

# Add grid
plt.grid(True)

#plt.xticks(ticks=df['timestamp'], rotation=45)

# Save figure with high DPI for better quality 
plt.savefig("Current-Time-Plot.png", dpi = 300)

# Display the plot
plt.show()

=======
# Add grid
plt.grid(True)

# Display the plot
plt.show()
>>>>>>> 18925d1ce6de395f9e637a5ef775a3866633bf9b
