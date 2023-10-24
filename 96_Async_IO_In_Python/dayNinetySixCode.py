import time
def function1():
  time.sleep(3)
  print("Function 1")
def function2():
  time.sleep(3)
  print("Function 2")
def function3():
  time.sleep(3)
  print("Function 3")
  function1()
  function2()