
def func():
	return "This is a function"


def judge1(arg):
	if callable(arg):
		return "{} is callable, {}".format(arg, arg())
	else:
		return "{} don't callable".format(arg)

def judge2(arg):
	import types

	if isinstance(arg, types.FunctionType):
		return "{} is callable, {}".format(arg, arg())
	else:
		return "{} don't callable".format(arg)


if __name__ == "__main__":

	s = "abc"

	print(judge1(func))
	print(judge2(func))
	print(judge1(s))
	print(judge2(s))