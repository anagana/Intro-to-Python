a1 = ["Cookies", "Chocolate", 8, True, -3, -5, "Chocolate", 8,False, 8]
b1 = [8,True,10,14,"Chocolate", "Milk", "Jelly",True, False, True]
set_a = set(a1)
set_b= set(b1)
union_ab = set_a.union(set_b)
intersection_ab = set_a.intersection(set_b)
print(union_ab)
union_ab.update({"kit-kat", "oreo"})
#union_ab.add("Kit-Kat")
#union_ab.add("Oreo")
print(union_ab)
new_set= union_ab | intersection_ab
print(intersection_ab)
print(new_set)
if "Chocolate" in new_set:
    print("Yes")
new_set.remove("oreo")
print(new_set)
