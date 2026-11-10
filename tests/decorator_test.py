from datetime import datetime
from pydantic import BaseModel, PositiveInt

def register(fn):
    print("______Inside register______")

    print(fn.__name__)
    print(fn.__doc__)
    print(fn.__annotations__)

    return fn

def decorator_with(prefix):
    print("Inside decorator_with")

    def decorator(fn):
        print("Inside decorator baskdlaskjdaslkjdlaskjdlaskjd")
        print(prefix, fn.__name__)
        return fn

    print("Returning decorator")

    return decorator

@register
@decorator_with("Prefix:") # anything_at_all = decorator_with("Prefix:")(anything_at_all)
def anything_at_all(x: int) -> str:
    """Does a thing."""

    print(f"Did a thing: {x}")

    return ""

if __name__ == "__main__":
    print(0)
    anything_at_all(5)
