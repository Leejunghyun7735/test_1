my_list = ["a","b","c"]
del my_list[0]
print(my_list)

my_list = ["a","b","c"]
print(my_list[::-1])


my_list = ["a","b","c","d","e","f"]
print(my_list[0:5])

my_list = ["a","b","c","d","e","f"]
print(my_list[2:])

my_list = ["a","b","c","d","e","f"]
print(my_list[3:0:-1])

my_list = ["a","b","c","d","e","f"]
print(my_list[::2])

for i in my_list: # :리스트로 출력됨
    print(i)

for i in range(100,0,-1):     # :리스트로 출력됨
    print(i)

for i in range(10,0,-3):
    print(i)



my_list = ["a","b","c","d","e","f"]
print(my_list[0,5])

my_list = ["a","b","c","d","e","f"]
for i in range(2,0):
    print(my_list[i])  

my_list = ["a","b","c","d","e","f"]
for i in range(3,0,-1):
    print(my_list[i])

my_list = ["a","b","c","d","e","f"]
for i in range(0,0,2):
    print(my_list[i])




# end
 
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in range(5):
    print(my_list[i], end=', ')

print()

for i in range(2, 6):
    print(my_list[i], end=', ')

print()

for i in [3, 2, 1]:
    print(my_list[i], end=', ')

print()

for i in [0, 2, 4]:
    print(my_list[i], end=', ')


