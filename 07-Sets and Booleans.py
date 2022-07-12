# coding: utf-8

# # Set and Booleans
# 
# There are two other object types in Python that we should quickly cover: Sets and Booleans. 
# 
# ## Sets
# 
# Sets are an unordered collection of *unique* elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works

x = set()


# We add to sets with the add() method
x.add(1)

#Show
x


# Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.
# 
# We know that a set has only unique entries. So what happens when we try to add something that is already in a set?

# Add a different element
x.add(2)

#Show
x


# Try to add the same element
x.add(1)


#Show
x


# Notice how it won't place another 1 there. That's because a set is only concerned with unique elements! We can cast a list with multiple repeat elements to a set to get the unique elements. For example:
# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]


# Cast as set to get unique values
set(list1)


# ## Booleans
# 
# Python  comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None. Let's walk through a few quick examples of Booleans (we will dive deeper into them later in this course).

# Set object to be a boolean
a = True

#Show
a


# We can also use comparison operators to create booleans. We will go over all the comparison operators later on in the course.
# Output is boolean
1 > 2


# We can use None as a placeholder for an object that we don't want to reassign yet:
# None placeholder
b = None


# Show
print(b)


# Thats it! You should now have a basic understanding of Python objects and data structure types. Next, go ahead and do the assessment test!
