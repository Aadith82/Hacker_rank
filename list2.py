if __name__ == '__main__':
    N = int(input())
    result=[]
for _ in range(N):
    row = input().split(' ')
    if row[0]=='insert':
        result.insert(int(row[1]), int(row[2]))
    elif row[0] == 'print':
        print(result)
    elif row[0] == 'remove':
        result.remove(int(row[1]))
    elif row[0] == 'append':
        result.append(int(row[1]))
    elif row[0] == 'sort':
        result.sort()
    elif row[0] == 'pop':
        result.pop()
    elif row[0] == 'reverse':
        result.reverse()
    elif row[0] == 'print':
        print(result)
        
