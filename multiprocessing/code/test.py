def cpuBound(x, y):
    c = 0
    while c < 5000000:
        x += 1
        y += 1
        c += 1

def ioBoundWrite():
    f = open('test.txt', 'w')
    for x in range(2000000):
        f.write('hello\n')
    f.close()

def ioBoundRead():
    f = open('test.txt')
    lines = f.readlines()
    f.close()