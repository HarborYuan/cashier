def ticket_printer(lister,number,total):
    f=open("ticket.txt","w")
    f.write("本次购物清单如下：\n")
    f.write("商品编号\t商品名称\t价格\t数量\t小计\n")
    for (good,num) in zip(lister,number):
        f.write(str(good.id)+"\t\t"+good.name+"\t\t"+str(good.price)+"\t"+str(num)+"\t"+str(num*good.price)+"\n")
    f.write("总价： "+str(total))
    f.close()
