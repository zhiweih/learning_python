class Lunch:
    def __init__(self):
        self.employee = Employee()
        self.customer = Customer()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        self.customer.printFood()

class Customer:
    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self):
        print("I ordered:", self.food.name)

class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)

class Food:
    def __init__(self, foodName):
        self.name = foodName

if __name__ == '__main__':
    l = Lunch()
    l.order('Pizza')
    l.result()
