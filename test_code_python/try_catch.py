for i in range(int(input())):
    try:
        a,b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)