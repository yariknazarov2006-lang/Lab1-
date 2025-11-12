import time

ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"


def draw_loading():
    print("Loading...")
    for i in range(100):
        time.sleep(0.2)
        print(f"{CSI}1G{i + 1}%", end="", flush=True)


def show_progress(num_tasks, width=30):
    for task in range(1, num_tasks+1):
        for filled in range(width):
            bar = f"{'#' * filled}{'-' * (width - filled - 1)}"
            print(f"{CSI}1G{task}/{num_tasks} {bar}", 
                   end="",
                   flush=True)
            time.sleep(0.1)




def draw_romb(x = 20, y = 20):
    colorA = 18
    colorB = 255
    a = f"{CSI}48;5;{colorA}m{' ' * 2}{RESET}"
    b = f"{CSI}48;5;{colorB}m{' ' * 2}{RESET}"
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
      
        
inf = open("C:\Users\nazar\OneDrive\Документы\PTH LABs\LAB1\sequence.txt").readlines()
print(inf[1])

if __name__ == '__main__':
    #draw_loading()
    #show_progress(3)
    #draw_romb()