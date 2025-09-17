'''
inputs: list of numbers
outputs: number (sum of sums of each leading subsequence in list)
rules:
- list always contains at least one number
- implicit: list w/ single number returns that number

data structure: list to add sum of each leading subsequence

algorithm:
- Given nums
- Get sum of sums of each leading subsequence:
    - Get sums:
        - Set sums to empty list
        - For idx in range of length of nums
            - For leading subsequence, start at 0, stop at idx + 1
            - Pass subsequence to sum function and assign to sums
    - Get total_sum:
        - Pass sums to sum function (and assign to total_sums or return as is)
- Return total_sum

code:
'''
def sum_of_sums(nums):
    subsequences = [nums[:idx + 1] 
                    for idx in range(len(nums))]
    
    return sum([sum(subsequence) 
                for subsequence in subsequences])
    
    # sums = []
    # for idx in range(len(nums)):
    #     sums.append(sum(nums[:idx + 1]))
    # return sum(sums)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True