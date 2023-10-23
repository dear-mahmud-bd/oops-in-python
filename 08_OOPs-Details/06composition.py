class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        return "Engine started"
    
class Driver:
    def __init__(self) -> None:
        pass


# car "has a" engine ---> it's not inheritance
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
    def start(self):
        self.engine.start() 


"""                           **                           """
"""                    ****************                    """
"""              ****************************              """
"""       ******************************************       """
""" ****************************************************** """
"""       ******************************************       """
"""              ****************************              """
"""                    ****************                    """
"""                           **                           """

# inheritance vs composition
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores
class RAM:
    def __init__(self, size) -> None:
        self.size = size
class HDD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hard drive
class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HDD(hd_capacity)


laptop = Computer(4, 16, 1024)
print(f"Laptop with {laptop.cpu.cores} CPU cores")
print(f"Laptop with {laptop.ram.size} GB of RAM")
print(f"Laptop with {laptop.hard_disc.capacity} GB HDD capacity")
