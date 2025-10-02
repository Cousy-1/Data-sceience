import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"]
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

# Bar positions
x = np.arange(len(months))
width = 0.25  # width of each bar

# Plotting
fig, ax = plt.subplots(figsize=(10,6))
bars1 = ax.bar(x - width, searches, width, label='Searches', color='dodgerblue')
bars2 = ax.bar(x, direct, width, label='Direct', color='lightcoral')
bars3 = ax.bar(x + width, social_media, width, label='Social Media', color='orange')

# Add labels, title, and legend
ax.set_ylabel('visitors\nin thousands', fontsize=12)
ax.set_title('Visitors by web traffic sources', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Annotating bar values
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.ylim(0, 110)
plt.show()
