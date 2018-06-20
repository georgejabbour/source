# Uses python3
import sys

def get_change(money):
    coins=[1,3,4]
    MinNumCoins=[0]
    for m in range(1,money+1):
    	MinNumCoins.append(m)
    	for i in range(1,len(coins)):
    		if m>=coins[i]:
    			NumCoins=MinNumCoins[m-coins[i]]+1
    			if NumCoins<MinNumCoins[m]:
    				MinNumCoins[m]=NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))