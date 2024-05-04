"""
Type: Creation
Intent: ensure a class has only one instance
Applicability:
  - use the singleton pattern when a class in you program should have just a single
    instance to all clients; for example, a single database object shared by different
    parts of the program
  - use the singleton when you need stricter control over global variables

"""

from threading import Lock, Thread
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class SingletonMeta(type):
  """
  This is a thread-safe implementation of Singleton.
  """
  _instances  = {}
  _lock: Lock = Lock()
  """
  We now have a lock object that will be used to synchronize threads during
  first access to the Singleton.
  """

  def __call__(cls, *args, **kwargs):
    if cls in cls._instances:
      return cls._instances[cls]
    with cls._lock:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
      return cls._instances[cls]
    # with cls._lock:
    #  if cls not in cls._instances:
    #    instance = super().__call__(*args, **kwargs)
    #    cls._instances[cls] = instance
    # return cls._instances[cls]

    
    return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
      print('Hello World')


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)



@timeit
def run() -> None:
  print("If you see the same value, then singleton was reused (yay!)\n"
        "If you see different values, "
        "then 2 singletons were created (booo!!)\n\n"
        "RESULT:\n")

  process1 = Thread(target=test_singleton, args=("AAA",))
  process2 = Thread(target=test_singleton, args=("BAA",))
  process3 = Thread(target=test_singleton, args=("BBA",))
  process4 = Thread(target=test_singleton, args=("BBB",))
  process5 = Thread(target=test_singleton, args=("CBB",))
  process6 = Thread(target=test_singleton, args=("CCB",))
  process1.start()
  process2.start()
  process3.start()
  process4.start()
  process5.start()
  process6.start()



if __name__ == "__main__":
  # The client code.
  run()
