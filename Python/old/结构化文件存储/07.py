import json

# 此时student是一个dict，而不是json格式
student = {
	"name":"zyp",
	"age":20,
	"address":"信阳"
}
list1 = [1, 2, 3, 4, 5]
t1 = tuple(list1)

print("student type:", type(student))
# print(type(t1))
# 将python数据类型转换为json格式
# help(json.dumps)
stu_json = json.dumps(student)
l1_json = json.dumps(list1)
t1_json = json.dumps(t1)
print("stu_json type:", type(stu_json), stu_json)
print("l1_json type:", type(l1_json), l1_json)
print("t1_json type:", type(t1_json), t1_json)

# 将json格式转化为python数据类型
stu_py = json.loads(stu_json)
l1_py = json.loads(l1_json)
t1_py = json.loads(t1_json)
print("stu_py type:", type(stu_py), stu_py)
print("l1_py type:", type(l1_py), l1_py)
print("t1_py type:", type(t1_py), t1_py)