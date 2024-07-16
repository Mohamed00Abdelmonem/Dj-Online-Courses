import matplotlib.pyplot as plt

# Data
labels = ['Related courses', 'Related units', 'Fetching context data for course', 'Course_Detail view accessed', 'Course_grid view accessed']
sizes = [20, 10, 20, 30, 20]

# Plot
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Log Entries')
plt.show()
