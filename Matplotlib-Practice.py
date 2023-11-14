import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Practice Plot
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



#Working with CSV file

data = pd.read_csv("export_1662385061.csv") # Load Data

# Convert 'timestamp' to datetime if it's not already
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Start a new figure
plt.figure(figsize=(20, 5))

# First y-axis for 'Exciter Field Current'
line1, = plt.plot(data['timestamp'], data['Exciter Field Current'], color='purple', linestyle='--', linewidth=2, marker='d', markersize=10, label='Exciter Field Current')

# Second y-axis for 'Line Current'
ax2 = plt.twinx()
line2, = ax2.plot(data['timestamp'], data['Line Current'], color='green', linewidth=2, marker='o', markersize=10, label='Line Current')

# Set the labels for x-axis and y-axes
plt.xlabel("Time (ISO 8601)")
plt.ylabel("Exciter Field Current", color='purple')
ax2.set_ylabel("Line Current", color='green')

# Customize tick parameters
plt.tick_params(axis='y', colors='purple')
ax2.tick_params(axis='y', colors='green')

# Create legends for both lines
plt.legend([line1, line2], ["Exciter Field Current", "Line Current"], loc='upper left')

# Add title
plt.title('Exciter Field Current and Line Current Over Time')

# Add grid
plt.grid(True)

# Display the plot
plt.show()