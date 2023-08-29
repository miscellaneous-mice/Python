#TUPLES
t = ('a','a',1)
mylist = [1,2,3]
print(type(mylist))
print(type(t)) #type is tuples
#you can do slicing and indexing and mixing of strings and integers etc...
print(t.count('a')) #counting no. of a
print(t.index('a')) #where b is located in tuples 
# t[0] = 'new' is not supported whereas lists support this assignment
# use tuples when you dont want elements dont get changed in tuples

#SETS
myset = [1,1,1,2,2,2,3,3,3] #assigning empty set
print(set(myset))  
myset.append(5) #adding elemts to SET
myset.append(6)# adding 2 to my SET
myset.append(6) #here 2 is not added again to my SET
print(set(myset))
#only unique value is accepted in SET

print('tuple unpacking')
stock_prices = [('APPL',200),('GOOG',300),('MSFT',250)]
for ticker,price in stock_prices:
    print(price + (0.1*price))




