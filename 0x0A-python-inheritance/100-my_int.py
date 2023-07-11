#!/usr/bin/python3
""" Module """


class MyInt(int):
    """
    class MyInt that inherits from int.
    """
    def __eq__(self, other):
        """ invert == by != """
        return self.value != other

    def __ne__(self, other):
        """ invert != by == """
        return self.value == other
