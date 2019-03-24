class Const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

const = Const()

const.INIT = "oneUp"

const.ONE_UP = "oneUp"
const.TWO_UP = "twoUp"
const.THREE_UP = "threeUp"
const.ONE_DOWN = "oneDown"
const.TWO_DOWN = "twoDown"
const.THREE_DOWN = "threeDown"

const.KEY_TIME = "2019-01-01"
const.KEY_PRICE = "low"
const.KEY_MAX = 6
const.KEY_MIN = 3
const.PRE_VALUE_FILE = "history.json"
const.LIST_VALUE = "list.txt"