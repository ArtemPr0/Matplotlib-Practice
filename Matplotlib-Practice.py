import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Practice Plot
plt.figure(figsize=(9, 4))
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
plt.tight_layout()
plt.savefig("Practice-Plot.png", dpi=300)
plt.show()




# Working with CSV file
data = pd.read_csv("export_1662385061.csv") # Load Data

# Convert 'timestamp' to datetime
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

plt.annotate('20/04/21', xy=(0.02,1), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', color='red', fontsize=12)

# Add grid
plt.grid(True)

#plt.xticks(ticks=df['timestamp'], rotation=45)

# Save figure with high DPI for better quality 
plt.savefig("Current-Time-Plot.png", dpi = 300)

# Display the plot
plt.show()

