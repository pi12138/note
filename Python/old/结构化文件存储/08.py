import json

# help(json.dump)
# dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
# 	allow_nan=True, cls=None, indent=None, separators=None, default=None, 
# 	sort_keys=False, **kw)
# help(json.load)
# load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, 
# parse_constant=None, object_pairs_hook=None, **kw)

student = {
	"name":"zyp",
	"age":20,
	"address":"xinyang"
}
list1 = [1, 2, 3, 4, 5]
t1 = tuple(list1)

filename = '01.json'

# 
with open(filename, 'w') as f:
	json.dump(student, f)
	
	# json.dump(list1, f)

	# json.dump(t1, f)
	

with open(filename, 'r') as f:
	data1 = json.load(f)
	# data2 = json.load(f)
	# data3 = json.load(f)
	print(data1)