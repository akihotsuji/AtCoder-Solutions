import io,sys,os
os.system("Cls")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n = int(input())
a = list(map(int,input().split()))

sums =[]

for i in range(0, len(a), 7):
    sums.append(sum(a[i:i + 7]))

print(*sums)