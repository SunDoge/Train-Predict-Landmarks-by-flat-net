import pickle
from collections import defaultdict

with open('data/train_dict.pkl', 'rb') as f:
    data = pickle.load(f)

"""
20180525.1727702684-9607-1_6.jpg
"""

new_data = defaultdict(list)

for key, value in data.items():
    for v in value:
        p1, p2, p3 = v.split('-')

        idx, ext = p3.split('.')

        head = idx[:1]
        tail = idx[1:]

        tail = int(tail)

        new_v = f'{p1}-{p2}-{head}_{tail}.{ext}'

        new_data[key].append(new_v)

with open('data/train_dict_fix.pkl', 'wb') as f:
    pickle.dump(new_data, f)
