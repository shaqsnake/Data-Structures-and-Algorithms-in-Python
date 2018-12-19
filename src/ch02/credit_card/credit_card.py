class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        
        The initial balance is zero.
        
        customer the name of the customer (e.g. Sean Tan)
        bank     the name of the bank (e.g. ICBC)
        acnt     the account identifier (e.g. 6200 0375 9983 1024)
        limit    credit limit (measured in RMB)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number(typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Sean Tan', 'ICBC', '6200 0375 9983 1024', 10000))
    wallet.append(CreditCard('Sean Tan', 'CMB', '6200 0375 9983 1024', 20000))
    wallet.append(CreditCard('Sean Tan', 'HKSC', '6200 0375 9983 1024', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val * 2)
        wallet[2].charge(val * 3)

    for c in range(3):
        print("Customer: %s, Bank: %s, Limit: %d\nBalance: %d" %
              (wallet[c].get_customer(), wallet[c].get_bank(),
               wallet[c].get_limit(), wallet[c].get_balance()))
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance: ", wallet[c].get_balance())
        print()