import collections
import inspect
import os
from collections import abc
from random import shuffle

from frenchdeck2 import FrenchDeck2
from tombola import Tombola


class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    f = Foo()
    assert f[1] == 10
    assert 20 in f
    assert 15 not in f
    assert (0, 10, 20) == tuple(i for i in f)

    l = list(range(10))
    print(f"range {' ' * 8} = {l}")
    shuffle(l)
    print(f'shuffled range = {l}')

    deck = FrenchDeck()


    def set_card(deck, position, card):
        deck._cards[position] = card


    def print_deck(deck):
        return str(deck._cards[:5])[:-1] + ', ...]'


    FrenchDeck.__setitem__ = set_card
    FrenchDeck.__repr__ = print_deck

    shuffle(deck)
    print(deck[:5])
    print(deck)


    class Struggle:
        def __len__(self):
            return 23

        def fine(self):
            return


    assert isinstance(Struggle(), abc.Sized)
    print(inspect.getmembers(Struggle, predicate=inspect.isfunction))
    print(inspect.getmembers(Struggle(), predicate=inspect.ismethod))

    deck = FrenchDeck2()
    print(deck[:5])
    shuffle(deck)
    print(deck[:5])


    class Fake(Tombola):
        def pick(self):
            return 13


    print(Fake)
    try:
        f = Fake()
        assert False
    except Exception as e:
        assert isinstance(e, TypeError)
        print(e)

    # A Virtual Subclass of Tombola
    from tombola import Tombola
    from tombolist import TomboList

    assert issubclass(TomboList, Tombola)
    t = TomboList(range(100))
    assert isinstance(t, Tombola)
    print(f"Method Resolution Order={TomboList.__mro__}")

    # subprocess.check_call("python -m doctest tombola_runner.py".split(), shell=True)
    os.system("python -m doctest tombola_runner.py")
