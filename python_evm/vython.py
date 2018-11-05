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

# For now, prefer no type inference: only allow uint256 to interact with other valid vyper types
class uint256:
	def __init__(self, val=None):
		self.initd = True if val else False
		if val and val >= 0: self.val = val
		elif not val: pass
		else: raise TypeError
		self.public = False
		self.constant = False

	def __add__(self, other):
		if (type(other) is int128 and other.val >= 0) or type(other) is uint256:
			return self.val + other.val
		if (type(other) is int128):
			print("You're trying to add a negative signed int with an unsigned int. No bueno.")
		else:
			print("cannot add uint256 with {}".format(type(other)))
		raise TypeError

# For now, prefer no type inference: only allow int128 to interact with other valid vyper types
class int128:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

	def __add__(self, other):
		if (type(other) is uint256 and self.val >= 0) or type(other) is int128:
			return self.val + other.val
		if (type(other) is uint256):
			print("You're trying to add a negative signed int with an unsigned int. No bueno.")
		else:
			print("cannot add int128 with {}".format(type(other)))
		raise TypeError


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

class timestamp:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

class timedelta:
	def __init__(self, val=None):
		self.initd = True if val else False
		self.val = val
		self.public = False
		self.constant = False

class wei_value:
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
		if type(thing) is bool:
			# May need to fix this for initialized vals
			b = under_bool()
			b.public = True
			return b
		if thing not in __vython_pub_funcs: __vython_pub_funcs.append(thing)
	return thing


def private(thing):
	try:
		thing.public
		thing.public = False
	except AttributeError:
		if type(thing) is bool:
			# May need to fix this for initialized vals
			b = under_bool()
			return b
		if thing not in __vython_priv_funcs: __vython_priv_funcs.append(thing)
	return thing


def constant(thing):
	try:
		thing.constant
		thing.constant = True
	except AttributeError:
		if thing not in __vython_const_funcs: __vython_const_funcs.append(thing)



def payable(func):
	return func



def send(fr: address, to: address):
	pass


def transpile(cls):
	# Perform 2 loops: first to collect all static vars, then to collect funcs.
	fin = ""
	for x in inspect.getmembers(cls):
		if not callable(x[1]):
			name = type(x[1]).__name__ if type(x[1]).__name__ != "under_bool" else "bool"
			try:
				if x[1].public:
					dec = "{}: public({})".format(x[0], name)
				else:
					dec = "{}: private({})".format(x[0], name)
				if x[1].initd:
					dec = "{} = {}".format(dec, x[1].val)
				fin = "{}\n{}".format(fin, dec)

			except AttributeError:
				pass
	fin = "{}\n\n".format(fin)
	for x in inspect.getmembers(cls):
		if callable(x[1]) and (x[0][0:2]!="__" or x[0]=="__init__") and x[0] != "builtins":
			func = textwrap.dedent(inspect.getsource(x[1]))
			for st in func.splitlines():
				if st[0:3] == "def":
					fin = "{}\n{}".format(fin, st.replace("self,","").replace("self", ""))
				else:
					fin = "{}\n{}".format(fin, st)
	return fin
