class TeamIterator:
    def __init__(self, team):
        self.__juniors = team._juniorMembers
        self.__seniors = team._seniorMembers
        self.__list = list()
        for jun in self.__juniors:
            self.__list.append((jun, 'junior'))
        for sen in self.__seniors:
            self.__list.append((sen, 'senior'))
        self.__list.append(None)
        self.value = self.__list[0]

    def __next__(self):
        placing = self.__list.index(self.value)
        if placing < len(self.__list) - 1:
            out = self.value
            self.value = self.__list[placing + 1]
            return out
        else:
            raise StopIteration


class Team:
    """
    contains list of juniors and seniors, redefines __init__.
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ returns object-iterator """
        return TeamIterator(self)
