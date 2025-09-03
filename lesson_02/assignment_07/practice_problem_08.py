# inputs: dictionary w/ nested dictionaries
# outputs: return list 
# explicit:
    # list elements are colors of fruit, sizes of veg
    # sizes in uppercase
    # colors capitalized
# implicit: 
    # color is in list
    # size is not in list
# data structure: list(s)
# algorithm:
    # given `dict1` with nested dictionaries
    # add capitalized colors of fruit and uppercased sizes of veg to a list
        # set `lst` w/ empty list
        # for each key in `dict1`
            # if type is fruit, add colors capitalized
                # set `sublist` w/ empty list
                # for `color` in `colors`
                    # capitalize `color` and add to `sublist`
                # add `sublist` to `lst`
            # if type is vegetable, add size in uppercase to `lst`
    # return the list
# code:
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
# lst = []
# for subdict in dict1.values():
#     if subdict['type'] == 'fruit':
#         sublist = []
#         for color in subdict['colors']:
#             sublist.append(color.capitalize())
#         lst.append(sublist)
#     else:
#         lst.append(subdict['size'].upper())
# print(lst)

def color_or_size(subdict):
    if subdict['type'] == 'fruit':
        return [color.capitalize() for color in subdict['colors']]
    else:
        return subdict['size'].upper()

lst = [color_or_size(subdict) for subdict in dict1.values()]
print(lst == [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"])