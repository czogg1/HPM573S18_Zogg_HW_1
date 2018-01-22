
#Problem 4: Lists and Mutability (Weight 2). Create a list, named yours, to store my favorite schools:
#‘Yale’, ‘MIT’, and ‘Berkeley’; and create a list, named mine, to store 3 of your favorite schools whatever
#they are. Use the + operator to create a new list, named ours1, to represent our favorite schools:
#   ours1 = mine + yours

yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Yale', 'Harvard', 'Johns Hopkins']
ours1 = mine+yours

print(ours1)

#Now, create another list, name ours2, to again represent our favorite schools but this time use:
#   ours2 = []
#   ours2.append(mine)
#   ours2.append(yours)

ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours2)

#Answer these questions:
#1. Print ours1 and ours2. Describe how ours1 and ours2 differ from each other.

# The second set of commands calls for an empty list. It then appends the list 'mine' as an element in the list
#   and the list 'yours' as a second element in the list, resulting in a list of lists.
#   The first command concatenates the two lists, resulting in a new list with the original elements of both list
#   'mine' and list 'yours'.

#2. Change the second element of yours to something else and again print ours1 and ours2.
#Explain why changing yours would changes ours2 but not ours1.

mine[1] = 'Stanford'
print(mine)

print(ours1)
print(ours2)

# List 'ours1' was created as a new list based on the original concatenated elements of 'mine' and 'yours'.
#   Subsequently invoking 'ours1' does not call back to the current state of 'mine' or 'yours'. List 'ours2',
#   in contrast, is a list consisting of the current elements of list 'mine', list 'yours'. Any changes to its
#   elements will be reflected when it is invoked.

