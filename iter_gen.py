from pprint import pprint, pformat


class MyIterator:

    def __init__(self, letters):
        """
        Constructor
        """
        print("in __init__", pformat(self), pformat(letters))
        self.letters = letters
        self.position = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        print("in __iter__", pformat(self))
        return self

    def __next__(self):
        """
        Returns the next letter in the sequence or
        raises StopIteration
        """
        print("in __next__", pformat(self), vars(self))
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter


if __name__ == '__main__':
    i = MyIterator('abcd')
    for item in i:
        print(item)
