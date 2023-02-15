# def starts_with_A(s):
#     return s[0] == "A"
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(starts_with_A, fruit)
#
# print(list(map_object))

#
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))



animal=["Cat","Dog","Horse","Panther","Tiger"]
anim=map(lambda ani:ani[1]=="a",animal)
print(list(anim))