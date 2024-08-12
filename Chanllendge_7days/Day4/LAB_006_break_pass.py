# how break and pass work in loops


for i in range(0,100):
    if i == 5:
        pass
    elif i == 90:
        break


ii = 0
while ii < 10:
    print(ii)
    if ii ==5:
        ii+=1
        pass
    elif ii == 8:
        ii +=1
        break
    ii +=1

    print(ii, "end of the code")
    continue