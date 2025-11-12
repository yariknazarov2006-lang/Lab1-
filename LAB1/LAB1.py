# ВАРИАНТ 1
import time

ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"

# ФЛАГ ФРАНЦИИ
def draw_flag(lng = 36, hgt = 9):
    COLOR_1 = 18
    COLOR_2 = 255
    COLOR_3 = 160
    for i in range(hgt):
        a = f"{CSI}48;5;{COLOR_1}m{' ' * (lng//3)}{RESET}"
        b = f"{CSI}48;5;{COLOR_2}m{' ' * (lng//3)}{RESET}"
        c = f"{CSI}48;5;{COLOR_3}m{' ' * (lng//3)}{RESET}"
        print(a+b+c)


# ПАТТЕРН ШАШКИ
def draw_pattern(height=9, length = 36):
    COLOR_A = 255
    COLOR_B = 0
    a = f"{CSI}48;5;{COLOR_A}m{' ' * 2}{RESET}"
    b = f"{CSI}48;5;{COLOR_B}m{' ' * 2}{RESET}"
    for i in range(height):
        if i % 2 == 0:
            s1 = ""
            for j in range(length):
                if j % 2 == 0:
                    s1 += a
                else:
                    s1 += b
            print(s1)
        else:
            s1 = ""
            for j in range(length):
                if j % 2 == 0:
                    s1 += b
                else:
                    s1 += a
            print(s1)

# ФУНКЦИЯ y=x^2
def draw_fucion(x = 16, y = 16):
    COLOR_A = 18
    COLOR_B = 255
    a = f"{CSI}48;5;{COLOR_A}m{' ' *2}{RESET}"
    b = f"{CSI}48;5;{COLOR_B}m{' ' *2}{RESET}"
    ind = 10**1000
    for i in range(y, -1, -1):
        s1 = ""
        for j in range(x):
            if i == j**2:
                ind = j
                s1 += a
            else:
                if j == ind:
                    s1 += a
                else:
                    s1 += b
        print(s1)


# ДИАГРАММА "Количество чисел меньше и больше 0"
def draw_diag():
    inf = open(r"LAB1\sequence.txt").readlines()
    n0 = 0
    n1 = 0
    for i in range(len(inf)):
        inf[i] = float(inf[i])
        if inf[i] < 0:
            n0 += 1
        else:
            n1 += 1
    COLOR_A = 18
    COLOR_B = 160
    a = f"{CSI}48;5;{COLOR_A}m{' '}{RESET}"
    b = f"{CSI}48;5;{COLOR_B}m{' '}{RESET}"
    print("Количество числел < 0: ", n0)
    print(a * (n0//2))
    print("Количество числел > 0: ", n1)
    print(b * (n1//2))
    inf.close()




if __name__ == '__main__':
    draw_flag()
    draw_pattern()
    draw_fucion()
    draw_diag()