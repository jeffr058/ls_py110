def swap_name(full_name):
    swapped_name = full_name.split(' ')
    swapped_name.reverse()
    return ', '.join(swapped_name)

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True