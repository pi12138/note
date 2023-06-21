# 多个异常情况
# 在进行异常处理时，如果存在多个异常，会处理一个excpet后，便不执行其他except

try:
	num = int(input("please a number:"))
	rst = 100 / num
	printf(rst)					# 

except ZeroDivisionError as e:
	print("input error")
	print(e)

except NameError as e:
	print('Name error')
	print(e)
	print(type(e))
	
# 所有异常都继承自Exception
# 如果写上下面这句话，任何异常属性都可以拦截
# 而且下面这句话一定是最后一个except
except Exception as e:
	print("不清楚那出错了")
	print(e)

print("异常处理") 
