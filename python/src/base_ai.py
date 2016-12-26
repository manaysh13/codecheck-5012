from abc import ABCMeta, abstractmethod


class BaseAI():
    __metaclass__ = ABCMeta
    @abstractmethod
    def answer(self, char, vocab):
        raise NotImplementedError
