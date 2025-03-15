def remove_duplicates(lst):
    if not lst:
        return "The list is empty."
    
    unique_items = []
    for i in lst:
        if i not in unique_items:
            unique_items.append(i)
    
    if len(unique_items) == len(lst):
        return "The list has no repetitive items."
    
    return unique_items

result = remove_duplicates([1,1,2,2,3,3,4,4,5,5,6,7,])
print(result)