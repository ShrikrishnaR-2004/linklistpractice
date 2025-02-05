# Take a array and remove duplicates and add into new array but wihtout append you have to add and
# don't use set function'

arr = [int(x) for x in input().split()]
seen = []
a = [i for i in arr if i not in seen and seen.append(i) is None]
print(a)