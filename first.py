print("hello world")
numbers = [10,15,20,25,30,35,40,45]
even_list = numbers[::2]
odd_list = numbers[1::2]
print(numbers)
print(even_list)
print(odd_list)


list1 = [10,30,20,40,50]
list2 = [60,20,40,70,80]
merge_list = list1 + list2
unique_list = list(set(merge_list))
ascending_list = sorted(unique_list)
descending_list = sorted(unique_list,reverse=True)
print(list1)
print(list2)
print(merge_list)
print(unique_list)
print(ascending_list)
print(descending_list)



numbers = [45,20,50,60,30,10,40,80]
print(numbers)
numbers.append(35)
print(numbers)
numbers.insert(3,55)
print(numbers)
numbers.extend([56,57])
print(numbers)
numbers.remove(40)
print(numbers)
numbers.pop()
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(numbers.index(50))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))




numbers =[45,30,50,90,80,70,50,30,20]
unique_numbers = list(set(numbers))
sorted_numbers = sorted(unique_numbers)
largest = sorted_numbers[-1]
second_largest = sorted_numbers[-2]
smallest = sorted_numbers[0]
second_smallest = sorted_nu#mbers[1]
print(numbers#)
print(unique_#numbers)
print(sorted_numbers)
print(largest)
print(second_largest)
print(smallest)
print(second_smallest)



a=(10,20,30,40)
print(type(a))

a =(10,20,30,40)
a1 = list(a)
a1.append(50)
a1.pop()
print(tuple(a1))


a =(10,20,30,40)
new_tuples = a +(50,)
print(new_tuples)



a = (10,20,30,40)
print(a)

a = 10,20,30,40
print(a)

a = tuple([1,2,3])
print(type(a))
print(a)


a =()
print(type(a))
print(a)


a = (1,)
print(type(a))
print(a)


a = (1,2,3,4,5)
print(a[3])
print(a[-2])



a = (1,2,3,4,5)
print(a[::-1])
print(a[1:4])


a = (1,[1,2])
print(a[1][0])


a = (10,20,30,40)
print(max(a))
print(min(a))
print(len(a))
print(sorted(a))
print(type(a))
print(sum(a))



a = (45,10,89,10,30,10)
print(max(a))
print(min(a))
result = sum(a)
result = (a[::-1])
result = tuple(set(a))
my_list = [1,2,3,4]
result = tuple(my_list)
print(my_list)
print(result)

a1 = (1,2,3,4,5)
a2 = (6,7,8,9,10)
result = a1 + a2
print(result)

a = (10,20,30,40,50,60)
result = sorted(a)
print(result[-2])

s = {1, 2}
s.update([3, 4])
print(s)
s.update((5, 6), {7, 8})
print(s)
s.update("ab")
print(s)

a = (1,2,3,4,3,6,3)
print(max(a))
print(min(a))
result = sum(a)
print(result)
result = (a[::-1])
print(result)
result = tuple(set(a))
print(result)
print(100 in a)
result = sorted(set(a))
print(result[-2])













