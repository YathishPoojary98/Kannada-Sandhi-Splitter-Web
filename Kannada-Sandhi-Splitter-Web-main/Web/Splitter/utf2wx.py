from wxconv import WXC
import sys
#print(data)

con = WXC(order='utf2wx',lang='kan')
def convert(input):
	res = con.convert(input)
	res = res.replace('_','')
	return res


