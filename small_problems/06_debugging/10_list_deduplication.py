'''
Since sets are not ordered and if the order must be preserved, a better solution may be to add the element to a new list if the new list does not contain the element. This is a way to make sure duplicates are not added to the list if the element already exists in the list.

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
'''
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num)
    
print(unique_data == [4, 2, 1, 3])

'''
Upon review, LSBot noted that my solution uses the list for two things, to store the nums and check for membership, and that a common practice is to separate the two concerns; the provided solution uses an empty set as the data structure to check for membership (which is part of a set's design), and then stores the num to a list.
'''