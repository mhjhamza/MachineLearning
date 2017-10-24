# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# number = 0.0
# count = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"): continue
#     # print(line)
#     count += 1
#     number += float(line[line.find(':')+1:].lstrip())
#
# print(number/count)


# fname = input("Enter file name: ")
# fh = open('hamza.txt')
#
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     for word in line.split():
#         if not word in lst:
#             lst.append(word)
#
# lst.sort()
# print(lst)
# lst = lst + words
# print(lst.sort())


# fname = input("Enter file name: ")
fname = ''
if len(fname) < 1: fname = "hamza.txt"
fh = open(fname)
lst = list()
count = 0
for line in fh:
    if line.rstrip().startswith('From '):
        var = line.split()
        print(var[1])

        #        var[2]
        #        res = lst
        count += 1

print("There were", count, "lines in the file with From as the first word")

