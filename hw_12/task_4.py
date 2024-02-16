def remove_element(lst, target):
    count_removed = lst.count(target)
    lst[:] = [num for num in lst if num != target]
    return count_removed


list_ = [1, 2, 3, 4, 5, 2, 6, 2, 7]
target_number = 2
removed_count = remove_element(list_, target_number)
print("count of removed numbers:", removed_count)
print("New list:", list_)
