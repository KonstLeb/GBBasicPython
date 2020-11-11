mystring = input ("Введите любой текст, разделяемый пробелами: ")
mylist = list (mystring)
mylist.append(' ')
count = 1
newstring = ''
for letter in mylist:
    newstring = newstring + letter
    if letter == ' ':
        print (count, newstring[0:10])
        newstring = ''
        count += 1
input()