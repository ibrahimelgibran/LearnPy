def sequentialSearch(alist, item): pos = 0
found = False
while pos < len(alist) and not found:
if alist[pos] == item: found = True
else:
pos = pos+1
return found
urutan = [23,7,32,99,4,15,11,20]