import sys

FIRST_INT = 1

with open('/proc/meminfo', 'r') as file:
    full = file.readline().split()[1]
    full = int(full)

if __name__ == '__main__':
    size = ((full//1024 + 100) * 1024 * 1024) // sys.getsizeof(FIRST_INT)
    lis = [i for i in range(size)]