s = set()

s.add(1)

s.add(2)

print("Set 1 : {}".format(s))

s.add(2)

print("Set 2 : {}".format(s))

s.clear()

print("Set 3 : {}".format(s))

s = {1, 2, 3}

sc = s.copy()

s.add(4)

print("Set 4 : {}".format(sc))

print("Set 5 : {}".format(s))

print("Set 6 : {}".format(s.difference(sc)))

# print("Set 6 : {}".format(sc.difference(s)))

set1 = {1, 2, 3}

set2 = {1, 4, 5}

set1.difference_update(set2)

print("Set 7 : {}".format(set1))

s.discard(2)

print("Set 8 : {}".format(s))

s1 = {1 ,2 ,3}
s2 = {1, 2, 4}
s3 = {5}

print("Set 9 : {}".format(s1.intersection(s2)))

s1.intersection_update(s2)

print("Set 10 : {}".format(s1))

print("Set 11 : {}".format(s1.isdisjoint(s2)))

print("Set 12 : {}".format(s1.isdisjoint(s3)))

print("Set 13 : {}".format(s1.issubset(s2)))

print("Set 14 : {}".format(s2.issuperset(s1)))

print("Set 15 : {}".format(s1.symmetric_difference(s2)))

print("Set 16 : {}".format(s2.symmetric_difference(s1)))

print("Set 17 : {}".format(s1.union(s2)))

s1.update(s2)

print("Set 18 : {}".format(s1))