from credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees.
    """

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        
        The initial balance is zero.
        
        customer the name of the customer (e.g. Sean Tan)
        bank     the name of the bank (e.g. ICBC)
        acnt     the account identifier (e.g. 6200 0375 9983 1024)
        limit    credit limit (measured in RMB)
        apr      annual precentage rate (e.g. 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return Ture if charge was processed.
        Return False and assess 5 yuan if charge id denied.
        """
        success = super().charge(price)
        if not success:                                                                                                                                                                                                                                                                           
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance.
        """
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == "__main__":
    pcc = PredatoryCreditCard('Sean Tan', 'ICBC', '6200 1234 5521 1563', 800, 0.0825)
    
    for val in range(100, 500, 100):
        pcc.charge(val)
        print("Customer: %s, Bank: %s, Limit: %d, Balance: %d" % (pcc.get_customer(), pcc.get_bank(), pcc.get_limit(), pcc.get_balance()))

    print("After monthly check...")
    pcc.process_month()
    print("Customer: %s, Bank: %s, Limit: %d, Balance: %d" % (pcc.get_customer(), pcc.get_bank(), pcc.get_limit(), pcc.get_balance()))