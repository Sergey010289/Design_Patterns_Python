__author__ = 'sergey'


class PizzaFactory:
    def __init__(self, pizzaType):
        print "I'm pizza Factory"
        self.pizzaType = pizzaType

    def createPizza(self):
        targetPizza = self.pizzaType
        return globals()[targetPizza]()
        #print self.pizza

    #add method bake and cut in PizzaFactory
    #bake, cut

class AbstractPizza:
    pizza = ""

    def get_pizza(self):
        return self.pizza


class SanFranciscoPizza(AbstractPizza):
    pizza = 'thin crust, lots of cheese, sauce, ham'


class ChicagoPizza(AbstractPizza):
    pizza = 'thin dough, a little cheese, gravy, sausage'


if __name__ == '__main__':
    pizza1 = PizzaFactory('ChicagoPizza')
    print pizza1.createPizza()
    pizza2 = PizzaFactory('SanFranciscoPizza')
    print pizza2.createPizza()