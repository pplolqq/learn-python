# p1
def encslat(temp):#封装
    import time
    def els():
     begin = time.perf_counter()
     temp()
     end = time.perf_counter()
     print(begin)
     print(end)
     print(end-begin)
    return els
@encslat
def func():
    pass
p={"3":4,"4":4,"5":4,"6":4,"7":4,"8":4,"9":4,"A10":4,"J":4,"Q":4,"_K":4,"c1":4,"c2":4,"joker1-small":1,"joker2-big":1}
pl=[]
for i in p:
   pl.append(i)
pl.sort()
# print(pl)
import random
a=[]
b=[]
c=[]
d=[]
t=0
play=[1,2,3]
while len(d)!=3:
    rdo =random.randint(0,14)
    r_num=pl[rdo]
    if p[r_num]==0:
       continue
    p[r_num]-=1
    d.append(r_num)
for i in [a,b,c]:    
    while len(i)!=17:
        rdo =random.randint(0,14)
        r_num=pl[rdo]
        if p[r_num]==0:
           continue
        p[r_num]-=1
        i.append(r_num)
        # print(pl)
    i.sort()
    i=i[::-1]
    i=str(i).replace("A10","10")
    i=i.replace("_K","K")
    i=i.replace("c1","1")
    i=i.replace("c2","2")
    # print(pl)
    # print(f"玩家{play[t]}的牌是:")
    t+=1
    print(i)
# print("三张置顶牌为：")
d.sort()
d=d[::-1]
d=str(d).replace("A10","10")
d=d.replace("_K","K")
d=d.replace("c1","1")
d=d.replace("c2","2")
# print(d)
# print(p)
lll=[a,b,c]
for i in range(1,4):
    with open (f"player{i}.txt","w",encoding="utf-8") as f:
        f.write(f"玩家{play[i]}的牌是:\n")
        f.write(str(lll[i-1]))
with open ("other_player.txt","w",encoding="utf-8") as f:
   f.write(d)