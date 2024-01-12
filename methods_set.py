my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.remove(2)  # {1, 3}

my_set = {1, 2, 3}
my_set.discard(2)  # {1, 3}

my_set = {1, 2, 3}
popped_element = my_set.pop()  # popped_element може бути 1, 2, або 3

my_set = {1, 2, 3}
my_set.clear()  # set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)  # {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)  # {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1.issubset(set2)  # True

set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1.issuperset(set2)  # True

set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1.issuperset(set2)  # True

