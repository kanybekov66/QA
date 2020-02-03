with open('air.txt', 'r') as file:
    f = file.read().replace('\n', '')
f = f.replace(' ', '')
f = f.replace('.', '')
f = f.replace(',', '')
f = f.lower()

res = {}

for keys in f:
    res[keys] = res.get(keys, 0) + 1
print(res)


def key_with_max_value(res):
    v = list(res.values())
    k = list(res.keys())
    return k[v.index(max(v))]
print(key_with_max_value(res))