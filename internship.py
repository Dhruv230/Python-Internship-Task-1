my_list = [1, 2, 3]
print("Initial list:", my_list)

my_list.append(4)
print("List after adding an element:", my_list)

my_list.remove(2)
print("List after removing an element:", my_list)

my_list[0] = 10
print("List after modifying an element:", my_list)

my_dict = {"a": 1, "b": 2, "c": 3}
print("\nInitial dictionary:", my_dict)

my_dict["d"] = 4
print("Dictionary after adding an element:", my_dict)

del my_dict["b"]
print("Dictionary after removing an element:", my_dict)

my_dict["a"] = 10
print("Dictionary after modifying an element:", my_dict)

my_set = {1, 2, 3}
print("\nInitial set:", my_set)

my_set.add(4)
print("Set after adding an element:", my_set)

my_set.remove(2)
print("Set after removing an element:", my_set)

print("Is 3 in the set?", 3 in my_set)
print("Is 5 in the set?", 5 in my_set)

my_set.remove(3)
my_set.add(10)
print("Set after modifying an element (remove 3, add 10):", my_set)