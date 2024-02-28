madlib = ''
no_mo = ['Done', 'done', 'd']

while madlib not in no_mo:
    madlib = str(input())
    if madlib in no_mo:
        break
    else:
        print(madlib[-1::-1])



