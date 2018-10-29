class MaxSizeList(object):
    def __init__(self, list_size):
        self.list_size = list_size
        self.list = list()

    def push(self, value):
        if len(self.list) >= self.list_size:
            self.list.pop(0)
        self.list.append(value)

    def get_list(self):
        return self.list


def main():
    pass


if __name__ == '__main__':
    main()
