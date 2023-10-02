"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
        def __init__(self, name):
            self.name = name
            self.pay = 0
            self.monthly_salary = 0
            self.hourly_wage = 0
            self.commission = 0
            self.no_contracts = 0

        def get_pay(self):
            #calculates contract pay
            if (self.monthly_salary > 0):
                self.pay = self.pay + self.monthly_salary
            elif (self.hourly_wage>0 and self.hours_worked >0):
                self.pay = self.pay + (self.hourly_wage * self.hours_worked)
            #calcuales commission pay
            if (self.commission > 0 and self.no_contracts == 0):
                self.pay = self.pay + self.commission
            elif (self.commission > 0 and self.no_contracts):
                self.pay = self.pay + (self.commission * self.no_contracts)
            #returns total pay
            return self.pay

        def __str__(self):
            self.get_pay()
            payment_string = self.name
            if (self.monthly_salary > 0):
                payment_string = payment_string + ' works a monthly salary of ' + str(self.monthly_salary)
            elif (self.hourly_wage>0 and self.hours_worked >0):
                payment_string = payment_string + ' works on a contract of ' + str(self.hours_worked) + ' at ' + str(self.hourly_wage) + '/hour'
            
            if (self.commission > 0 and self.no_contracts == 0):
                payment_string = payment_string + ' and receives a bonus commission of ' + str(self.commission)
            elif (self.commission > 0 and self.no_contracts):
                payment_string = payment_string + ' and recieves a commission for ' + str(self.no_contracts) + ' contracts(s) at ' + str(self.commission) + '/contract'

            payment_string = payment_string + '. Their total pay is ' + str(self.pay) + '.'
            return payment_string

        def set_monthly_salary(self, num):
            self.monthly_salary = num
        def set_hourly_wage(self, num):
            self.hourly_wage = num
        def set_hours_worked(self, num):
            self.hours_worked = num
        def set_commission(self, num):
            self.commission = num
        def set_no_contracts(self, num):
            self.no_contracts = num

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_monthly_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_hours_worked(100)
charlie.set_hourly_wage(25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_monthly_salary(3000)
renee.set_no_contracts(4)
renee.set_commission(200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_hours_worked(150)
jan.set_hourly_wage(25)
jan.set_no_contracts(3)
jan.set_commission(220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_monthly_salary(2000)
robbie.set_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_hours_worked(120)
ariel.set_hourly_wage(30)
ariel.set_commission(600)

