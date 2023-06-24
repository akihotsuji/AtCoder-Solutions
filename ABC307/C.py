import io,sys,os
os.system("Cls")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]

HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]

HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

Ab = []
Bb = []
Xb = []

#A,B,Xの黒の位置を管理
for i in range(HA):
    for j in range(WA):
        if A[i][j] == "#":
            Ab.append([i,j])

for i in range(HB):
    for j in range(WB):
        if B[i][j] == "#":
            Bb.append([i,j])

for i in range(HX):
    for j in range(WX):
        if X[i][j] == "#":
            Xb.append([i,j])

print(Xb)