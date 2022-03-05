from collections import Counter

colors = ['blue', 'blue', 'blue', 'red', 'red']
counter = Counter(colors)
counter['yellow'] += 1
# Counter({'blue': 3, 'red': 2, 'yellow': 1})
counter.most_common()[0]
# ('blue', 3)