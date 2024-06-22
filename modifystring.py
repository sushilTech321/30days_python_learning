#uper case 
a = "apple"
print(a.upper())

#lower case
print(a.lower())

#remove whitespace
b = "  Hello, universe  " 
c = b.lstrip()
print(c)

# replacing string, kunai pani string lai arko string or char le replace garna replace() method ko use garinxa
b = "Mango is very taste"
print(b.replace("taste","yummy"))

#split() method, yo method le chahi kunai pani string lai 'list' maa return garxa ra jun thauma seperator rakhinxa tyaha bata teyo string chahi list item maa convert hunxa.
#e.g
b = "apple, banana"
c = b.split(',')
print(c)

#format() string, string maa integer add garna use garinxa ra jun thau maa int add garnu parne ho tyaha {} use garne talako e.g. jastai
age = 3
cls = 1
pencil = 5
txt = "I am {} years old, and i read in class {}, i have {} pencil."
print(txt.format(age,cls,pencil))

a = ["apple","ball","car","dog"]
print(isinstance(a,list))

a = ("apple","ball","car","dog")
print(isinstance(a,tuple))

a = ({"name":"apple","weight":"12kg","color:":"ping"})
print(isinstance(a,dict))

#floor division

a = 9
b = 3
print(a//b)
