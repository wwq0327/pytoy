class A(object):
    def __init__(self):
        self.__x = None

    def _get_x(self):
        return self.__x

    def _set_x(self, value):
        self.__x = value

    def _del_x(self):
        del self.__x
    x = property(_get_x, _set_x, _del_x)

