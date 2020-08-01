from types import FunctionType
from abc import ABC, abstractmethod


class Middleware(ABC):
  __name__ = "Middleware"

  def __init__(self):
    self.__next = None

  def add_next(self, func: FunctionType):
    self.__next = func
    return self

  @abstractmethod
  def _exec(self, next_function, *args, **kwargs):
    pass

  def __call__(self, *args, **kwargs):
    return self._exec(self.__next, *args, **kwargs)


class _FunctionMiddleware(Middleware):
  def __init__(self, current: FunctionType):
    super().__init__()
    self.__current = current

  def _exec(self, next_function, *args, **kwargs):
    return self.__current(next_function, *args, **kwargs)
