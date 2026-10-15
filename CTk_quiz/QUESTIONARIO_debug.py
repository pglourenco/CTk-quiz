l = [0, 1, 2, 3]
l_copy = []

for i in range(len(l)):
    if not l[i] > 1:
        l_copy.append(l[i])

print(l_copy)