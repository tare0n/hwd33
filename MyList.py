class MyList(list):
    def __init__(self, _list):
        print("works magic method")
        super().__init__(_list)

    def __getitem__(self, item):
        print("works magic method")
        super().__getitem__(item)

    def __setitem__(self, key, value):
        print("works magic method")
        super().__setitem__(key, value)

    def __str__(self):
        print("works magic method")
        return str(super().__str__())

    def __len__(self):
        print("works magic method")
        return int(super().__len__())




