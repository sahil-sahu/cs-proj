# Write a program in Python that take three inputs from user i.e 1st is a source file name, 2nd target file name,
# 3rd a character and copies all the lines of a text source file onto target file except those lines which starts with char.
# In program you may need to define and call a function filter(source, target, char).
# f_name, t_name, char = "bella.txt", "ciao.txt", "ciao"
# f_name, t_name, char = input("Please enter filename:"), input(
#     "Please enter target filename: "), input("Eliminating character: ")


# def filter(f_name, t_name, char):
#     f = open(f_name)
#     data = f.readlines()
#     f.close()

#     t = open(t_name, "w")

#     for i in data:
#         if i[0] != char:
#             t.write(i)

#     t.close()


# filter(f_name, t_name, char)
# OR

# Write a program in Python that take two inputs from user i.e a file name, a word and display number of occurance of given word
# in the file. In program you may need to define and call function count(file, word) that return the occurance of given word in file.

# def count(file, word):
#     f = open(file)
#     data = " ".join(f.read().split("\n")).split(" ")
#     counter = 0
#     for i in data:
#         if word in i:
#             counter += 1
#     return counter


# print(count(f_name, char))
