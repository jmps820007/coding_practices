def find_max(a_list):
    if a_list == []:
        return 0
    else:
        return max(a_list)


print(find_max([1, 2, 3]))
print(find_max([1, -1, -5]))
print(find_max([]))