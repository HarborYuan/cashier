from GoodsClass import Goods
from Errors import *
from Ticket import ticket_printer
from Readme import read_me

my_goods = []

if __name__ == '__main__':
    while (True):
        try:
            x=input(read_me)
            if not x in ("1","2","3","4"):
                raise ValueError()
            x= int(x)
            if (x==1):
                try:
                    id = int(input("请输入商品编号"))
                    name = input("请输入商品名称")
                    price = float(input("请输入商品价格"))
                    new_good = Goods(id,name,price)
                    for good in my_goods:
                        if good.id==new_good.id:
                            raise RepeatError("已有此编号的商品")
                    my_goods+=[new_good]
                    print("商品添加成功")
                except RepeatError as e:
                    print (e)
                except ValueError as e:
                    print ("输入非法请重试!")
            if (x==2):
                id = int(input("请输入要删除的商品编号"))
                flag=True
                for good in my_goods:
                    if good.id==id:
                            my_goods.remove(good)
                            print ("删除成功")
                            flag=False
                            break
                if flag:
                    print("找不到该商品")
            if (x==3):
                print ("\n现在开始收银，请依次输入商品编号，输入stop停止\n")
                total = 0
                lister = []
                number = []
                x=input("请输入商品编号")
                while x!="stop":
                    try:
                        x=int(x)
                        this_good = None
                        for good in my_goods:
                            if good.id == x:
                                this_good = good
                                break
                        if this_good == None:
                            raise NoneError("不存在此商品")
                        y=int(input("请输入数量"))
                        number+=[y]
                        lister+=[this_good]
                        print("添加物品成功")
                        total += y*this_good.price
                        x=input("请输入商品编号")
                    except NoneError as e:
                        print(e)
                    except ValueError as e:
                        print("输入非法请重试")
                print("商品的总价是",total)
                x= input("是否打印小票?Y/N\n")
                if x=="Y":
                    ticket_printer(lister,number,total)
            if (x==4):
                print("欢迎下次使用")
                break
        except ValueError as e:
            print ("输入非法请重试")
