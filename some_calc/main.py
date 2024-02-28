def MoProbs(money, problems):
    dx = 0
    dy = 0
    if money > problems:
        for i in range((money - problems)):
            problems += 1
            dx += 1
        print(f'{dx} opps entered the chat.')
    elif money < problems:
        for i in range((problems - money)):
            money += 1
            dy += 1
        print(f'Get some more money foo, ${dy} added to account.')
    return

if __name__ in '__main__':
    x = int(input('How much money you pull?\n'))
    y = int(input('How many opps you got?\n'))
    print(MoProbs(x, y))