from abc import ABCMeta, abstractmethod

class ShiritoriAI(metaclass=ABCMeta):
    @abstractmethod
    def answer(self, char, vocab):
        raise NotImplementedError
