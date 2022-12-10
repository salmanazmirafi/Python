# # -----------------------Chapter 05 Working with string in python----------------------------
#
# # ----single or double quotes
#
# # text = 'Hi "Salman"'
# # print(text)
#
#
# # ---multi line string
#
# text = ''' python is fun to learn
# python is one of the easy language
# it is very simple '''
#
# print(text)
#
# # ---concatenating string
#
# a = "Hello"
# b = " World"
#
# print(a + b)
#
# # -------------------------Accessing part of a string---------------------
#
# # ---indexing
#
# text = "I Love You"
# print(text[0])
# print(text[2:5])

# -------------String------------------
name = "Salman"
name2 = "Sonia"

x = name.upper()
y = name2.upper()
print(x + y)

print(len(name+name2))

name = "Salman is my future ------"
y = name.replace('------', "Name")
print(y)