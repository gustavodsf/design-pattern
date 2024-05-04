"""
Type: Creation
Intent: ensure a class has only one instance
Applicability:
  - use the singleton pattern when a class in you program should have just a single
    instance to all clients; for example, a single database object shared by different
    parts of the program
  - use the singleton when you need stricter control over global variables

"""

class SingletonMeta(type):
  """
  The Singleton class can be implemented in different ways in Python. Some
  possible methods include: base class, decorator, metaclass. We will use the
  metaclass because it is best suited for this purpose.
  """
  _instances = {}

  def __call__(cls, *args, **kwargs):
    """
    Possible changes to the value of the `__init__` argument do not affect
    the returned instance.
    """
    if cls not in cls._instances:
      instance =  super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Hello World")


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")