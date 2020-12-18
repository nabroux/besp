from threading import Thread
import os

print(os.cpu_count(), '核')

def deadloop():
    i = 0
    while True:
        i += 1

def main():
    print('start')
    for _ in range(os.cpu_count()):
        t = Thread(target=deadloop)
        t.start()

if __name__ == '__main__':
    main()