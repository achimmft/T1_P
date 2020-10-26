class Employee:
    '''develops a payroll program for a company'''
    def __init__(self, emp_id, name, address, city, state, zipcode, classification=None, payment_Method=None):
        '''strings to define an employee object except for classification and paymentMethod'''    
        self.emp_id=emp_id
        self.name = name
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.classification=classification
        self.payment_Method=payment_Method
    
    def make_salaried(self, salary):
        '''sets classification to salary'''
        self.classification=Salaried(salary)
     
    def make_hourly(self, hourly_rate):
        '''sets classification to hourly'''
        self.classification=Hourly(hourly_rate)

    def make_commissioned(self, salary, commission_rate):
        '''sets classification to commissioned'''
        self.classification = Commissioned(salary)
    
    def mailed(self):
        '''employee has pay mailed to them'''
        self.pay = Mailed(self)
    
    def direct(self, route, account):
        '''empolyee direct deposits to bank'''
        self.pay=Direct(self, route, account)
    
    def issue_Pay(self):
        amount=self.classification.get_Pay()
        self.pay(amount)
        
from abc import ABC, abstractmethod
class Classification(ABC):
    '''from ABS for an abstract class determine how the employee wants to be paid'''

    @abstractmethod
    def get_Pay(self):
        pass
 
class Hourly(Classification):
    '''employee type'''
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecards = []
        
    def get_Pay(self):
        '''calculate pay for hourly employee'''
        amount = 0.0
        for timecard in self.timecards:
            amount += timecard * self.hourly_rate
        self.timecards.clear()
        return amount

    def add_Timecard(self, hours):
        '''add some hours to the timecards list'''
        self.timecards.append(hours)
            
        
class Salaried(Classification):
    '''employee type'''
    def __init__(self, salary):
        self.salary=salary
    def get_Pay(self):
        '''return pay calculation for Salary employee'''
        return self.salary/24
    
        

class Commissioned(Salaried):
    '''employee type'''
    def ___init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_Sale(self, receipt):
        '''put receipts in a list'''
        self.receipts.append(receipt)

    def get_Pay(self):
        '''custom pay method'''
        amount = super().get_Pay()
        for receipt in self.receipts:
            amount += receipt * self.commission_rate/ 100
            self.receipts.clear()
            return amount

class Payment_Method(ABC):
    '''abstract PaymentMethod class'''
    def __init__(self, employee):
        self.employee = employee
        
    @abstractmethod
    def pay(self, amount):
        pass

class Direct(Payment_Method):
    '''employee wants a directdeposit'''
    def __init__(self, employee, route, account):
        super().__init__(employee)
        self.route = route
        self.account=account
    def pay(self, amount, pay_log_file):
        with open(pay_log_file, 'a') as plog:#add file to print to. 
            print("Transferring", f"{amount:.02f}", "for", self.employee.name, "to", self.account, ": ", 
            self.route, file=plog)
    
class Mailed(Payment_Method):
    '''employee wants a mailed check'''
    def __init__(self, employee):
        super().__init__(employee)

    def pay(self, amount, pay_log_file):
        with open(pay_log_file, 'a') as plog:
            print("Mailing", f"{amount:.02f}", "to", self.employee.name, "at" ,self.employee.address, 
            self.employee.city. self.employee.state, self.employee.zipcode, file=plog)