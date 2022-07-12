"""
File Handling

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

r+ Open for reading and writing. The stream is positioned at the beginning of the file.

a+ Open for reading and appending (writing at end of file). The file is created if it does not exist. The initial file position for reading is at the beginning of the file, but output is appended to the end of the file

"""


my_file = open('test.txt')

# We can now read the file
my_file.read()

# But what happens if we try to read it again?
my_file.read()

# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:

# Seek to the start of file (index 0)
my_file.seek(0)
# Now read again
my_file.read()


# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()


# When you have finished using a file, it is always good practice to close it.
my_file.close()


# ## Writing to a File
# 
# By default, the `open()` function will only allow us to read the file. We need to pass the argument `'w'` to write over the file. For example:

# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')
# Opening a file with `'w'` or `'w+'` truncates the original, meaning that anything that was in the original file **is deleted**!
# Write to the file
my_file.write('This is a new line')

# Read the file
my_file.seek(0)
my_file.read()
my_file.close()  # always do this when you're done with a file


# ## Appending to a File
# Passing the argument `'a'` opens the file and puts the pointer at the end, so anything written is appended. Like `'w+'`, `'a+'` lets us read and write to a file. If the file does not exist, one will be created.

my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

#to read
my_file = open('test.txt','r')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')
my_file.seek(0)
print(my_file.read())


for line in open('test.txt'):
    print(line)


# Don't worry about fully understanding this yet, for loops are coming up soon. But we'll break down what we did above. We said that for every line in this text file, go ahead and print that line. It's important to note a few things here:
# 
# 1. We could have called the "line" object anything (see example below).
# 2. By not calling `.read()` on the file, the whole text file was not stored in memory.
# 3. Notice the indent on the second line for print. This whitespace is required in Python.

# Pertaining to the first point above
for asdf in open('test.txt'):
    print(asdf)

