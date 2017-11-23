import leancloud


class BaseModel(leancloud.Object):
    """
    # @DynamicAttrs
    """

    def __init__(self, attrs=None):
        leancloud.Object.__init__(self)
        for attr in attrs:
            setattr(self, "get_{}".format(attr), lambda name=attr: self.get(name, None))
            setattr(self, "set_{}".format(attr), lambda val, name=attr: self.set(name, val))

