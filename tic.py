arr = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def show(arr):
    for x in arr:
        for y in x:
            if y == -1:
                print("a", end="  ")
            else:
                print(y, end="  ")
        print("\n")
    return


def update(x, y, player):
    arr[y-1][x-1] = player


#input(1, 2, 1)


def check():
    flag = -1
    for x in range(3):
        if arr[x][0] == arr[x][1] == arr[x][2]:
            if arr[x][0] >= 0:
                return arr[x][0]
    for x in range(3):
        if arr[0][x] == arr[1][x] == arr[2][x]:
            if arr[0][x] >= 0:
                return arr[0][x]
    if arr[0][0] == arr[1][1] == arr[2][2]:
        if arr[0][0] >= 0:
            return arr[0][x]

    if arr[2][0] == arr[1][1] == arr[0][2]:
        if arr[0][x] >= 0:
            return arr[0][x]

    return -1


winner = -1

show(arr)
turns = 0
while (winner == -1 and turns < 9):
    player = turns % 2
    print("turn of player no:", player)
    print("enter value of x")
    x = int(input())
    print("enter value of y")
    y = int(input())
    update(x, y, player)
    winner = check()
    turns += 1
    show(arr)

print("winner is", winner)
