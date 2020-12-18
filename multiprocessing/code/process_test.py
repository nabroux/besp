from multiprocessing import Process
import os

def deadloop():
    i = 0
    while True:
        i += 1

def main():
    print('start')
    for _ in range(os.cpu_count()):
        t = Process(target=deadloop)
        t.start()

if __name__ == '__main__':
    main()