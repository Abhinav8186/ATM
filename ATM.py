class Atm(object):
    def __init__(self, user, atmCardNo, pin):
        self.user = user
        self.atmCardNo = atmCardNo
        self.pin = pin

    def cashWithdrawl(self):
        print("Cash is being withdrawed by you!.")
    def balanceEnquiry(self):
        print("Your Balance is: ₹1,00,00,00,000")
        print("We hope it's not a काला धन.")
        
a = Atm("FutureFlash™","1542 6545 9944 8281","5850")
b = Atm("LostHickory360™","1854 3344 2881 4343","2579")
print(b.balanceEnquiry())
print(b.cashWithdrawl())
