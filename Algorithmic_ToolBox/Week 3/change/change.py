# Uses python3
import sys

def get_change(m):
    ans = 0
    for n in [10,5,1]:
        ans += int(m/n)
        m = m%n
    return ans

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
