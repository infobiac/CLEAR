from vython import *



class Contract:
	test = public(int128())
	toost = public(uint256())

	@public
	def __init__(self, wa: int128):
		self.test = wa

	@public
	def poop(self):
		self.toost = 5

transpile(Contract)