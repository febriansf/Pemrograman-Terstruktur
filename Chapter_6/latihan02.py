def starFormation1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print('')


def starFormation2(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print('')


def fullTriangle(n):
    starFormation1(n//2)
    if(n % 2 == 0):
        starFormation2(n//2)
    else:
        starFormation2(n//2+1)


starFormation1(4)
print('')
starFormation2(4)
print('')
fullTriangle(7)
