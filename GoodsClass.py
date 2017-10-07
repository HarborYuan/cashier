class Goods(object):
    __slots__ = ('id', 'name', 'price')

    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price