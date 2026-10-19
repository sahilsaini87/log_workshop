# # import sys 
# # name = sys.argv[1]
# # batch = sys.argv[2]
# # cgpa = sys.argv[3]
# # print("Hello", name, "from", batch, "has a CGPA of", cgpa)
# # def greet(name, batch, cgpa):
# #     return f"Hello {name} from {batch} has a CGPA of {cgpa}"
# # for i in range(1, 5):
# #     print(greet(name, batch, cgpa))

# # with open("text.txt", "r") as f:
# #     content = f.read()
# #     print(content)
# with open("text.txt", "r") as f:
#     content = f.read()
#     print(content)
#     updated_content = content.replace("hello world how are you", "hello everyone, I am fine")
#     print(updated_content)


# import sys
# from collections import Counter
# filename = sys.argv[1]
# with open(filename) as f:
#     lines = f.readlines()
# print("Total lines:", len(lines))

# counts = Counter()
# for line in lines:
#     fields = line.split()
#     if len(fields) > 0:
#         key = fields[0]
#         counts[key] += 1
# print("Top 5:")
# for item, n in counts.most_common(5):
#     print(item, n)

import sys
from collections import Counter
filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
print("Total lines:", len(lines))

counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > 7:
        key = fields[7]
        counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)