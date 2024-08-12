# For loop
# syntax for i in range|list|string:
#conditon to perfrom
'''
for i in range(0,10):
    print(f"{i},--hello") '''

# range prints frpm 0-9 not 10 can bee seen in output

# range (start, stop/end(-1), step) this how range fuction works

for i in range(-1,-10,-1):
    print(f"{i}--""string","Gods save us")
# revere the sting with range fuction and for loop
string1 = "Hello world God save us all"
for i in range(-1,-(len(string1)+1),-1):
    print(string1[i],sep=" ",end='')


for i in range(0,10,2): # 2,4,5,6,8
    print(i)


for i in range(1,5):
    print(i,"hello")

list11 = list(range(4,9))
print('list11',list11)