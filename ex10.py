
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#solution with list comprehesion
prep = [i for i in a if i in b]   
new_list = []

for i in prep:
  if i not in new_list:
    new_list.append(i)
    
print(new_list)

# solution with set function (set()) and set intersection (&)
new_set = (set(a) & set(b))     
print(new_set)

# creating random lists
import random
random_a = [random.randint(1, 100) for i in range(random.randint(10, 20))]
random_b = [random.randint(1, 100) for i in range(random.randint(10, 20))]
print(random_a)
print(random_b)

# another option for creating random lists
import random
a = random.sample(range(100), 10)
b = random.sample(range(100), 10)
print(a)
print(b)