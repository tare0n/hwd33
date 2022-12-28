from Item import Item, Phone
from MyList import MyList
from Team import Team


def test_first_task():
    """
    commented strings raise some errors
    """
    print("&&& test for first task &&&")
    print("*** print input: 'Item('phone', 18000, 5)' ***")
    print(Item('phone', 18000, 5))

#    print("print input: 'Item(18000, 'phone', 5)'")
#    print(Item(18000, 'phone', 5))

#    print("print input: 'Item('phone', '18000', 5)'")
#    print(Item('phone', '18000', 5))

#    print("print input: 'Item('phone', 18000, 5.5)'")
#    print(Item('phone', 18000, 5.5))


def test_second_task():
    print("&&& test for second task &&&")
    print("*** initialisation of phone1 with 'Phone('iPhone 10', 500, 5, 1)' ***")
    phone1 = Phone("iPhone 10", 500, 5, 1)
    print(phone1)


def test_third_task():
    print("&&& test for third task &&&")
    lst = MyList(['John', 'Snow', 'Java'])

    if not lst[2] == 'Python':
        lst[2] = 'Python'

    print(lst)
    print(len(lst))


def test_fourth_task():
    print("&&& test for fourth task &&&")
    team = Team()
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** iterating through team in for loop ***')
    for member in team:
        print(member)

    print('*** iterating through team in while loop ***')
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    test_first_task()
    test_second_task()
    test_third_task()
    test_fourth_task()
