# continue Statement
# continue statemenet skis the current iteration of a loop and
# move to the next iteration.


for number in range(10):
    if number % 2 == 0:
        continue
    print(number)


for number in range(10):
    if number % 2 == 0:
        pass
    print(number)
# |i | Condition | o/p
# |0 | 0%2 == 0 -True | continue - Skip No o/p
# |1 | 0%2 == 0 -False| o/p -> print 1
# |2 | 0%2 == 0 -True| o/p -> skip
# |3 | 0%2 == 0 -False| o/p -> print 3
# |4 | 0%2 == 0 -True| o/p -> skip
# |5 | 0%2 == 0 -False| o/p -> print 5 ......

