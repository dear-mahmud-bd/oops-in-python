from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from users import Chef, Customer, Server, Manager
from order import Order


def main():
    ########################################## Create a menu...  ##########################################
    menu = Menu()
    # add 'pizza' to the menu...
    pizza_1 = Pizza('Masala Pizza', 789, 'large', ['masala', 'moyda', 'piyaj'])
    pizza_2 = Pizza('Mangshow Pizza', 999, 'large', ['masala', 'mangshow', 'tel'])
    pizza_3 = Pizza('Sadharon Pizza', 499, 'medium', ['masala', 'tel', 'piyaj'])
    menu.add_menu_item('pizza', pizza_1)
    menu.add_menu_item('pizza', pizza_2)
    menu.add_menu_item('pizza', pizza_3)
    # add 'burger' to the menu...
    burger_1 = Burger('Chicken Burger', 150, 'Chicken', ['bread', 'chicken', 'sos'])
    burger_2 = Burger('Boneless Burger', 240, 'beef', ['beef', 'chili', 'naga flever'])
    menu.add_menu_item('burger', burger_1)
    menu.add_menu_item('burger', burger_2)
    # add 'drinks' to the menu...
    coke = Drinks('CocaCola', 50, True)
    tea = Drinks('Cha Gorom', 15, False)
    coffee = Drinks('Mocha Coffee', 100, False)
    menu.add_menu_item('drinks', coke)
    menu.add_menu_item('drinks', tea)
    menu.add_menu_item('drinks', coffee)

    # menu.show_menu()

    ########################################## Create a restaurant  ##########################################
    restaurant = Restaurant('SosurBari Restaurant', 1000, menu)
    # add 'manager' employee to the Restaurant...
    manager = Manager('Abul Khayer', 658, 'abul@khayer.manager', 'abdullahpur', 990, 'Jan 1, 2020', 'core')
    restaurant.add_employee('manager', manager)
    # add 'chef' employee to the Restaurant...
    chef_1 = Chef('Aker Baburchi', 369, 'chupa@rustom.baburchi', 'rustomNagar', 1200, 'Feb 1, 2020', 'Chef', 'sob kisu')
    chef_2 = Chef('Deshi Baburchi', 369, 'baburchi@chef.deshi', 'babaNagar', 800, 'Mar 1, 2020', 'Chef', 'sob kisu')
    restaurant.add_employee('chef', chef_1)
    restaurant.add_employee('chef', chef_2)
    # add 'server' employee to the Restaurant...
    server = Server('Server Mama', 458, 'nai@jai.com', 'restaurant', 200, 'March 1, 2020', 'server')
    restaurant.add_employee('server', server)

    # restaurant.show_employees()

    ########################################## 'customer_1' placing an order...  ##########################################
    customer_1 = Customer('Sakib Khan', 6, 'king@khan.com', "banani", 100000)
    order_1 = Order(customer_1, [burger_2, coke, tea, pizza_1, coke, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    # 'customer_1' paying for 'order_1'
    restaurant.receive_payment(order_1, 4000, customer_1)
    print('revenue and balance after first customer', restaurant.revenue, restaurant.balance)
    ########################################## 'customer_2' placing an order...  ##########################################
    customer_2 = Customer('Sakib Khan', 6, 'king@khan.com', "banani", 100000)
    order_2 = Order(customer_2, [burger_2, coke, pizza_2, coffee, burger_1])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    # 'customer_2' paying for 'order_2'
    restaurant.receive_payment(order_2, 4000, customer_2)
    print('revenue and balance after secound customer', restaurant.revenue, restaurant.balance)
    ########################################## 'rich_kid' placing an order...  ##########################################
    rich_kid = Customer('Rich Kid', 6, 'rich@kid.com', "gulshan", 500000)
    bisal_order = Order(rich_kid, [pizza_1, pizza_2, pizza_3, coffee, burger_2, burger_2, tea, coke, coffee])
    rich_kid.pay_for_order(bisal_order)
    restaurant.add_order(bisal_order)
    # 'rich_kid' paying for 'bisal_order'
    restaurant.receive_payment(bisal_order, 4000, rich_kid)
    print('revenue and balance after rich_kid customer', restaurant.revenue, restaurant.balance)
    ########################################## 'boroLok' placing an order...  ##########################################
    boroLok = Customer('Boro Lok', 6, 'boro@lok.com', "london", 100000)
    boro_Order = Order(boroLok, [pizza_1, pizza_2, pizza_2, burger_1, burger_2, tea, coke, coffee])
    boroLok.pay_for_order(boro_Order)
    restaurant.add_order(boro_Order)
    # 'boroLok' paying for 'boro_Order'
    restaurant.receive_payment(boro_Order, 4000, boroLok)
    print('revenue and balance after boroLok customer', restaurant.revenue, restaurant.balance)

    ########################################## Revinew, Expense, Balance ##########################################
    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print(f'after Rent Revinew: {restaurant.revenue}, Expense:{restaurant.expense}, Balance:{restaurant.balance}')
    # pay salary
    restaurant.pay_salary(chef_1)
    print(f'after Salary Revinew: {restaurant.revenue}, Expense:{restaurant.expense}, Balance:{restaurant.balance}')



# calling the main method...
if __name__ == "__main__":
    main()