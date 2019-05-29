N = int(input())
ms = list(map(int, input().split()))

i = ms.index(max(ms))
t = ms[0]
ms[0] = ms[i]
ms[i] = t

print(*ms)

'''
N = int(input())
ms = list(map(int, input().split()))

def swap(mas, a, b):
    t = mas[a]
    mas[a] = mas[b]
    mas[b] = t

for i in range():
    



'''