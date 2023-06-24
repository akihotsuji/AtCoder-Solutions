import io,sys,os
os.system("Cls")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n = int(input())
li = [input() for _ in range(n)]

ans = "No"

for i in range(n):
    for j in range(n):
        if i ==j:
            continue
        s = li[i]+li[j]
        if  s == s[::-1]:
            ans = "Yes"
            break

print(ans)