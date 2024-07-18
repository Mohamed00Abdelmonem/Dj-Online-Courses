import matplotlib.pyplot as plt

# Data
labels = ['Related courses', 'Related units', 'Fetching context data for course', 'Course_Detail view accessed', 'Course_grid view accessed']
sizes = [20, 10, 20, 30, 20]

# Create a figure with a 1x2 grid of subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Pie Chart
axs[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
axs[0].set_title('Pie Chart')

# Bar Chart
axs[1].bar(labels, sizes)
axs[1].set_ylabel('Number of Entries')
axs[1].set_title('Bar Chart')
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlapping labels
plt.tight_layout()

# Set overall title for the figure
fig.suptitle('Distribution of Log Entries', fontsize=16, y=1.02)

plt.show()
