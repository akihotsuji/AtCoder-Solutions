import io,sys,os
os.system("Cls")
with open("HandInput.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

N = int(input())
S = input()

#提出する文字列
T = ""
#Tの中で最後の(のインデックス
stack = []

for i in range(N):
    c = S[i]
    #cが(だったら、Tに追加して、Tの中でのインデックスをstackに追加（長さ-1がインデックスになる）
    if c == "(":
        T += c
        stack.append(len(T)-1)
    #ｃが）で
    elif c ==")":
        #stackが空＝それまでに(が登場してなかったら、Ｔに追加
        if len(stack) == 0:
            T += c
        #stackに要素があったら、Tをstackの最後の添え字以降を削除
        else:
            T = T[:stack[-1]]
            stack.pop(-1)
    #ただの文字の時は、Ｔに追加
    else:
        T += c

print(T)
