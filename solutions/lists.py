# TODO: Implement a function that returns a list of numbers from 1 to n (already provided in original list)
def generate_numbers(n):
    my_list = []
    if (n>0):
        for i in range (1,n+1):
            my_list.append(i)
    return my_list

# TODO: Implement a function that takes two lists as arguments, merges them into one list, and then sorts the merged list in ascending order
def merge_and_sort_lists(list1, list2):
    my_list = list1 + list2
    my_list.sort()
    
    return my_list
    

# TODO: Implement a function that removes all duplicate values in a list and returns a list with only the unique elements in the order they appeared
def remove_duplicates(my_list):
    gay = []
    for item in my_list:
        if item not in gay:
            gay.append(item)
    return gay

# TODO: Implement a function that checks whether a list is a sublist of another list. A sublist is a sequence of consecutive elements that are part of another list
def is_sublist(list1, list2):
    flag = False
    a = len(list1)
    b = len(list2)
    for i in range(b-a+1):
        if list2[i:i+a] == list1:
            flag = True
    
    return flag

# TODO: Implement a function that rotates the elements of a list to the right by `k` places. `k` is non-negative
def rotate_list(my_list, k):
    a = len(my_list) 
    x = a-k
    mer_list = []
    a = my_list[a-k:a+1]
    b = my_list[0:x]
    mer_list = a +b
    return (mer_list)
    
