numbers = [1, 2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]

# access by index
print(numbers[2]) # 3

# get index num
print(numbers.index(5)) # 4

# change value
numbers[1] = 0
print(numbers) # [1, 0, 3, 4, 5]

# length
print(len(numbers)) # 5

# add item in last
numbers.append(6)
print(numbers) # [1, 0, 3, 4, 5, 6]

# remove a item
numbers.remove(0)
print(numbers) # [1, 3, 4, 5, 6]

# min number of list
print(min(numbers)) # 1

# max number of list
print(max(numbers)) # 6

# item exist in list
print(3 in numbers) # True

# not exist in list
print(9 not in numbers) # True

# concat list
print(numbers + [8,9]) # [1, 3, 4, 5, 6, 8, 9]

# remove last item
numbers.pop()
print(numbers) # [1, 3, 4, 5]

# add item using index
numbers.insert(1, 2) # [1, 2, 3, 4, 5]
print(numbers)

# sort list
numbers2 = [1, 5, 0, 9, 5]
numbers2.sort() 
print(numbers2) # [0, 1, 5, 5, 9]
numbers2.sort(reverse= True) 
print(numbers2) # [9, 5, 5, 1, 0]

# reverse list
numbers2.reverse()
print(numbers2) # [0, 1, 5, 5, 9]
