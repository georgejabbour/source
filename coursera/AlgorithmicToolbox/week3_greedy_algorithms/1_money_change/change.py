# Uses python3
import sys

def get_change(m):
    dimes=int(m/10)
    nickels = int((m%10)/5)
    pennies = int((m%10)%5)

    return dimes+nickels+pennies

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
