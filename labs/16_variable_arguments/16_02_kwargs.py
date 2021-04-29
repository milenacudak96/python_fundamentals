'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def fun(**kwargs):
    for i,k in kwargs.items():
        print(i,k)

fun(kot='mia',dog='hau')



def lowercase(func):
  """A decorator that avoids digital screaming."""
  def wrapper(text):
    initial_result = func(text)
    new_result = initial_result.lower()
    return new_result
  return wrapper

@lowercase
def say_something(text):
  return text

print(say_something("HEI WHAT'S UP?"))


def outer_func():
    msg = "Do you understand my scope??"

    def inner_func():
        print(msg)

    return inner_func

message = outer_func()
message()

def my_func(msg):
    def inner_func():
        print(msg)
    return inner_func

message = "Now we have an argument!"
woohoo = my_func(message)
woohoo()



def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func


@decorator_func
def dec():
    print("inside dec")

dec()
