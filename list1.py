list1 = [10,30,20,40,50]
list2 = [60,70,20,80,40]
merge_list = list1 + list2
unique_list = list(set(merge_list))
ascending_list = sorted(unique_list)
descending_list = sorted(unique_list,reverse=True)
print(list1)
print(list2)
print(merge_list)
print(ascending_list)
print(descending_list)