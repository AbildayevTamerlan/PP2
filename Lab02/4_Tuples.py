# Tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",) # remember the comma
print(type(thistuple))


tuple1 = ("abc", 34, True, 40, "male")


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
   print("Yes, 'apple' is in the fruits tuple")


# Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
   print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
   print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
   print(thistuple[i])
   i = i + 1


# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)