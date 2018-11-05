from vython import *



class Contract:
	foo = public(int128())
	bar = public(uint256())

	@public
	def __init__(self, wa: int128):
		self.foo = wa

	@public
	def test(self):
		self.bar = 5

Contract.tast = public(int128(10))

transpile(Contract)