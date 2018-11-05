import parser
import sys
import symbol
import token
import vyper_types
import inspect
import astor
# print(pa ser.st2list(parser.expr("print hi")))

class test_contract:
	testaaaa = 1
	def __init__(self):
		self.a=1
	def test1(self):
		print("hi")
	def inc(self):
		self.a+=1


msg = message()

class Contract:
	def __init__(self, obj):
		self.class_def = inspect.getsource(obj)
		self.obj = obj()
		self.funcs = {}
		for x in inspect.getmembers(obj):
			# Currently don't allow redefining __
			if callable(x[1]) and x[0][0:2]!="__":
				self.funcs[x[1].__name__] = x[1]
				print(inspect.getsource(x[1]))

	def getvars(self):
		return vars(self.obj)

	def __getattr__(self, name):
		def method(*args):
			# self.funcs[name](*args)
			getattr(self.obj, name)(*args)
		return method


def main():
	if len(sys.argv) != 2:
		print("Usage is: transpile [filename.py]")
		return

	t1 = test_contract()
	t1.poo = "poo"
	filename = sys.argv[1]
	file = None
	c = Contract(test_contract)
	print(c.test1())
	# print(token.tok_name)
	with open(filename) as f:
		file = f.read()

	c.inc()
	c.getvars()



if __name__== "__main__":
    main()