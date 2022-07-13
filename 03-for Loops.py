# coding: utf-8

# # for Loops
# 
# A <code>for</code> loop acts as an iterator in Python; it goes through items that are in a *sequence* or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.
# 
# We've already seen the <code>for</code> statement a little bit in past lectures but now let's formalize our understanding.
# 
# Here's the general format for a <code>for</code> loop in Python:
# 
#     for item in object:
#         statements to do stuff
#     

# The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use <code>if</code> statements to perform checks.
# 
# Let's go ahead and work through several example of <code>for</code> loops using a variety of data object types. We'll start simple and build more complexity later on.
# 
# ## Example 1
# Iterating through a list

# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)


# Great! Hopefully this makes sense. Now let's add an <code>if</code> statement to check for even numbers. We'll first introduce a new concept here--the modulo.
# ### Modulo
# The modulo allows us to get the remainder in a division and uses the % symbol. For example:

17 % 5


# This makes sense since 17 divided by 5 is 3 remainder 2. Let's see a few more quick examples:
# 3 Remainder 1
10 % 3


# 2 Remainder 4
18 % 7

# 2 no remainder
4 % 2


# Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!
# 
# Back to the <code>for</code> loops!
# 
# ## Example 2
# Let's print only the even numbers from that list!

for num in list1:
    if num % 2 == 0:
        print(num)


# We could have also put an <code>else</code> statement in there:
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')


# ## Example 3
# Another common idea during a <code>for</code> loop is keeping some sort of running tally during multiple loops. For example, let's create a <code>for</code> loop that sums up the list:
# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum = list_sum + num

print(list_sum)


# Great! Read over the above cell and make sure you understand fully what is going on. Also we could have implemented a <code>+=</code> to perform the addition towards the sum. For example:

# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num

print(list_sum)


# ## Example 4
# We've used <code>for</code> loops with lists, how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.
for letter in 'This is a string.':
    print(letter)


# ## Example 5
# Let's now look at how a <code>for</code> loop can be used with a tuple:
tup = (1,2,3,4,5)

for t in tup:
    print(t)


# ## Example 6
# Tuples have a special quality when it comes to <code>for</code> loops. If you are iterating through a sequence that contains tuples, the item can actually be the tuple itself, this is an example of *tuple unpacking*. During the <code>for</code> loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)


# Now with unpacking!
for (t1,t2) in list2:
    print(t1)


# Cool! With tuples in a sequence we can access the items inside of them through unpacking! The reason this is important is because many objects will deliver their iterables through tuples. Let's start exploring iterating through Dictionaries to explore this further!

# ## Example 7
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)


# Notice how this produces only the keys. So how can we get the values? Or both the keys and the values? 
# 
# We're going to introduce three new Dictionary methods: **.keys()**, **.values()** and **.items()**
# 
# In Python each of these methods return a *dictionary view object*. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view. Let's see it in action:
# Create a dictionary view object
d.items()


# Since the .items() method supports iteration, we can perform *dictionary unpacking* to separate keys and values just as we did in the previous examples.
# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 


# If you want to obtain a true list of keys, values, or key/value tuples, you can *cast* the view as a list:
list(d.keys())


# Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():

sorted(d.values())


# ## Conclusion
# 
# We've learned how to use for loops to iterate through tuples, lists, strings, and dictionaries. It will be an important tool for us, so make sure you know it well and understood the above examples.
# 
# [More resources](http://www.tutorialspoint.com/python/python_for_loop.htm)
