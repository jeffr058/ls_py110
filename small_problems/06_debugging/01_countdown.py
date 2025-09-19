'''
I predict this will print 10 ten times and then print LAUNCH!

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')


For the loop to count down successfully, counter needs to be reassigned with the decreased value in each iteration.
'''
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')
