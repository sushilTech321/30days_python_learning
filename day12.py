# python iterators

list1 = ["apple","banana","cat","dog"]

# print(type(list1))
myit = iter(list1)

# print (next(myit))
# print (next(myit))
# print (next(myit))
# print (next(myit))


# Create an Iterator

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# class Dummy :
#     def __iter__(self):
#         self.a = 0
#         return self
#     def __next__(self):
#         if self.a <= 10:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#            raise StopIteration
# d = Dummy()
# e = iter(d)
# for x in e:
#   print (x)




        