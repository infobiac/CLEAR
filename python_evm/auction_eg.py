from vython import *



class Auction:
	beneficiary = public(address())
	auctionStart = public(timestamp())
	auctionEnd = public(timestamp())

	# Current state of auction
	highestBidder = public(address())
	highestBid = public(wei_value())

	# Set to true at the end, disallows any change
	ended = public(bool())

	@public
	def __init__(_beneficiary: address, _bidding_time: timedelta):
	    self.beneficiary = _beneficiary
	    self.auctionStart = block.timestamp
	    self.auctionEnd = self.auctionStart + _bidding_time

	# Bid on the auction with the value sent
	# together with this transaction.
	# The value will only be refunded if the
	# auction is not won.
	@public
	@payable
	def bid():
	    assert block.timestamp < self.auctionEnd
	    assert msg.value > self.highestBid
	    if not self.highestBid == 0:
	        send(self.highestBidder, self.highestBid)
	    self.highestBidder = msg.sender
	    self.highestBid = msg.value


	# End the auction and send the highest bid
	# to the beneficiary.
	@public
	def endAuction():
	    assert block.timestamp >= self.auctionEnd
	    assert not self.ended
	    self.ended = True

	    send(self.beneficiary, self.highestBid)

print(transpile(Auction))