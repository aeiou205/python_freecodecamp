### Sorting list of tuples
# We can take advantage of the ability to sort a list of tuples to
# get a sorted version of a dictionary

#First we sort the dictionary by the key using the items () method
#and sorted() function

d = {'a':10, 'b':1, 'c':221}
print(d.items())
print(sorted(d.items()))
