inf = open(r"C:\Users\nazar\OneDrive\Документы\PTH LABs\LAB1\sequence.txt").readlines()
n0 = 0
n1 = 0
for i in range(len(inf)):
    inf[i] = float(inf[i])
    if inf[i] < 0:
        n0 += 1
    else:
        n1 += 1
print("Количество числе < 0: ", n0)
print("Количество числе > 0: ", n1)
print()
colorA = 18
colorB = 255
a = f"{CSI}48;5;{colorA}m{' ' * 2}{RESET}"
b = f"{CSI}48;5;{colorB}m{' ' * 2}{RESET}"
print(a * n0 //2)
print(b * n1 //2)