# list
# List - collectio of Items (dupicate is allowed)
my_list = [1,2,3]  # sae type of data (int)
print("print list ",my_list,'\n' ,"lenght of the list", len(my_list))\

print("my_list[0]",my_list[0],'my_list[2]',my_list[2], "my_list[11]",)
try:
    if my_list[10] == False:
        print("error")

except Exception as e:
    print("my_list[10] oout of range",e)

my_list.extend([9,8,7,'rdh',"Pramod", 3.14])
print(my_list)
my_list.remove(3)
print(my_list)
my_list.insert(2,33)
print(my_list)
print(my_list)
print(my_list[-1])
my_list.insert(-1,'luck')
print("hello how are you?? !!".replace(" ", '.'))
print(my_list)
my_list.reverse()
print(my_list)
#print('mylist to what tp do '.__reversed__())
print(my_list.pop(), my_list)
print(my_list,my_list.extend([2,2,2,3,3,3,]),"mylist", my_list, my_list.remove(2), my_list)