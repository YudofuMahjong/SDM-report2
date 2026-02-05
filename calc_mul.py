#!/usr/bin/python3
import re

def calc(A,B):
        ai=str(A)
        bi=str(B)
        
        # 整数のみを許可する正規表現 (小数点は含めない)
        p = re.compile('^\d+$')
        
        # 両方の入力が数値形式であるかチェック
        if p.match(ai) and p.match(bi):
                a=int(ai)
                b=int(bi)
                
                # 仕様通りの範囲チェック (1〜999)
                # 大小関係(a<b)の条件は削除
                if 1 <= a <= 999 and 1 <= b <= 999:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()