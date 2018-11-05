import inspect
import textwrap

class Block:
	def __init__(self):
		self.timestamp = None

block = Block()

class message:
	def __init__(self):
		self.sender = None
		self.value = None

msg = message()

__vython_pub_funcs = []
__vython_priv_funcs = []
__vython_const_funcs = []

class uint256:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

class int128:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False


class under_bool:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

class decimal:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

class address:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

# class struct:

# class mapping:



def public(thing):
	try:
		thing.public
		thing.public = True
	except AttributeError:
		if thing not in __vython_pub_funcs: __vython_pub_funcs.append(thing)
	return thing


def private(thing):
	try:
		thing.public
		thing.public = False
	except AttributeError:
		if thing not in __vython_priv_funcs: __vython_priv_funcs.append(thing)


def constant(thing):
	try:
		thing.constant
		thing.constant = True
	except AttributeError:
		if thing not in __vython_const_funcs: __vython_const_funcs.append(thing)



def payable(func):
	return func


def transpile(cls):
	# Perform 2 loops: first to collect all static vars, then to collect funcs.
	for x in inspect.getmembers(cls):
		if not callable(x[1]):
			try:
				if x[1].public:
					dec = "{}: public({})".format(x[0], type(x[1]).__name__)
				else:
					dec = "{}: private({})".format(x[0], type(x[1]).__name__)
				if x[1].initd:
					dec = "{} = {}".format(dec, x[1].val)
				print(dec)

			except AttributeError:
				pass
	print()
	for x in inspect.getmembers(cls):
		if callable(x[1]) and (x[0][0:2]!="__" or x[0]=="__init__"):
			func = textwrap.dedent(inspect.getsource(x[1]))
			for st in func.splitlines():
				if st[0:3] == "def":
					print(st.replace("self,","").replace("self", ""))
				else:
					print(st)
