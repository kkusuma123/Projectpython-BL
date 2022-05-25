import sqlite3
import os
os.system("cls")
choice = 0 
data=sqlite3.connect("epp.db")
c = data.cursor()
pro={}
pro1={}
pro_1=["a"]
pro_2=["a"]
pro_3=[]


#หัวตกแต่ง
print('='*100)
ttxx = ("ร้านหนังสือ")
y = ttxx.center(100)
print(y)
print('='*100)

print('='*100)
txt = ("BooK KA BooK")
x = txt.center(100)
print(x)
print('='*100)


address=""
name=""
name2=""
tele=""
def Datauser(): #singin
    global address ,name,name2
    print ("\n")
    txt = ("Signin")
    x = txt.center(100)
    print(x)
    
    User = input('\t\tUsername   : ')
    # password = input('')
    for i in range(100):
        password=input("\t\tPassword  :  ")
        if len(password) >=8:
            break
        print("ใส่คบ8")
    
    name = input('\t\tชื่อ  : ')
    name2 = input('\t\tนามสกุล  : ')
    address = input('\t\tที่อยู่  : ')

    def tel():
        global tele
        r = []
        tele = input("\t\tเบอร์ :")
        for i in range(len(r)):
                if tel == r[i]:
                    print("กรอบให้ครบ")
                    tel()
        if tele.isdigit() == False :
            print('กรุณาป้อนเฉพาะตัวเลขและป้อนให้ครบ 10 ตัว')
            tel()
        elif len(tele) != 10 :
            print('กรุณาป้อนป้อนตัวเลขให้ครบ 10 ตัว ')
            tel()
        
    tel()
            
    pp=(User,password,name,name2,address,tele)
    data=sqlite3.connect("epp.db")
    c=data.cursor()
    c.execute("INSERT INTO Datauser(User,password,name,name2,address,tele) VALUES (?,?,?,?,?,?)",pp )
    data.commit()
    c.close()
    import os ######
    os.system("cls") ##
    login() ######

def Big(): 
    print ("\n กรุณาเลือกทำรายการที่ต้องการ \n") ######
    log = input("1. Signin \t2. Login \n\n\n")#####
    if log == '1':
        Datauser()
    elif log == '2':
        login()

def login(): #LoginID
    global address,name,name2,tele
    
    print('='*100)
    txt = ("Login")
    x = txt.center(100)
    print(x)
    print('='*100)
    
    user_1=str(input("\n\n\n\t\t\tusername :"))
    pass_1=str(input("\n\n\t\t\tpassword :"))
    p=0
    cursor= data.execute('SELECT * FROM Datauser')
    for i in cursor:
        if user_1==i[0]and pass_1==i[1]:
            # q=i[2]S
            p=1
            address=i[4]
            name=i[2]
            name2=i[3]
            tele=i[5]
    if p==0:
        print("\n\tusername หรือ password ไม่ถูกต้อง ลองใหม่อีกครั้ง ")
        login()
    # print(user_1,pass_1)
    print("\n\nยินดีตอนรับเข้าสู่ร้านหนังสือ")
    print("\n\nยินดีตอนรับเข้าสู่ร้านหนังสือ")
    print("\n\nยินดีตอนรับเข้าสู่ร้านหนังสือ\n\n")

    import os
    os.system("cls")######
 
def Big(): 
    print ("\n")
    txt = ("\n กรุณาเลือกทำรายการที่ต้องการ \n")####
    x = txt.center(100)
    print(x)
    
    log = input("\t1. Signin \n\n\t2. Login \n\n\n==>  ")####
    if log == '1':
        Datauser()
    elif log == '2':
        login()
    elif log !='1'and log !='2':
        Big()


       
def menu(): #เมนู
    global choice 
    print('='*100)
    txt = ("กดหมายเลขเพื่อทำรายการ ====>")
    x = txt.center(100)
    print(x)
    print('='*100)
    print('\n 1. เเสดงประเภทหนังสือทั้งหมดของเรา\n 2.หยิบสินค้าเข้าตะกร้า\n 3.หยิบสินค้าออก\n 4. แสดงรายจำนวนและราคาของสินค้าที่หยิบ \n 5. ชำระค่าสินค้า เเละ ปิดโปรแกรม\n') 
    choice = input("\nกรุณาเลือกทำรายการ :  ")


def shop_1(): 
    cursor = data.execute('SELECT * FROM Allmybook')
    import os
    html = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\indexสมบูรณ์.html"
    os.system(html)
    for i in cursor:
        print(" ชื่อ ",i[1]) 
        print("    ชนิด     ",i[2]) 
        print("    ราคา    ",i[3],"\n\n")
            
    

def shop_2():
    cursor= data.execute('SELECT * FROM Allmybook')
    for i in cursor:
        print(i[0],"ชื่อ",i[1] )
        print("\t\t\t\t\t\t\t\t\t\tราคา",i[3])
        pro_1.append(i[1])
        pro_2.append(i[3])
        pro[i[1]] = i[3]
        
    print("\n\n")
    print('='*100)
    txt = ("กด 123 เพื่อหยุดหยิบสินค้า")
    x = txt.center(100)
    print(x)
    print('='*100)

    for i in range(1000):
        x=int(input("หมายเลขสิ่งค้าที่ต้องการ\n"))
        if x ==123:
            break
        pro1[pro_1[x]] = pro_2[x]
        pro_3.append(pro_1[x])
        cursor= data.execute('SELECT * FROM stock ')
        for i in cursor:
            if pro_1[x]==i[0]:
                stock=i[1]-1
        c=data.cursor()
        q_q=(stock,pro_1[x])
        c.execute("UPDATE stock SET quantity = ? WHERE namebook = ?",q_q)
        data.commit()
        c.close()
    import os
    os.system("cls")    

def shop_3():
    print("\n\n")
    print('='*100)
    txt = ("กด 12345 เพื่อหยุดการนำสินค้าออก ")
    x = txt.center(100)
    print(x)
    print('='*100)
    
    for i in range(1000):
        i=0
        for q in pro_3:
            i+=1
            print(i,'\t',q)
            
        print("\n\nกด 12345 เพื่อหยุดการนำสินค้าออก ")
        x=int(input("\nหมายเลขสิ่งค้าที่ต้องการเอาออก   "))
        
        if x == 12345:
            break
        cursor= data.execute('SELECT * FROM stock ')
        for i in cursor:
            if pro_3[x-1]==i[0]:
                stock=i[1]+1
        c=data.cursor()
        q_q=(stock,pro_1[x])
        c.execute("UPDATE stock SET quantity = ? WHERE namebook = ?",q_q)
        data.commit()
        c.close()
        pro_3.pop(x-1)


def shop_4():
    global address,name,name2,tele
    print("\n\n")
    print('='*100)
    txt = ("รายการสินค้าทั้งหมดที่ทำรายการ")
    x = txt.center(100)
    print(x)
    print('='*100)
    www=0
    for i in pro_3:
        print(" ชื่อ ",i)  
        print("    ราคา   ",pro1[i],"\n\n")
        www+=int(pro1[i])
    print("ราคารวม   ",www,"บาท\n")
    
    print('='*100)
    txt = ("ข้อมูลที่อยู่ผู้สั่งซื้อ")
    x = txt.center(100)
    print(x)
    print('='*100)
    print("\nชื่อ  ",name, "   ",name2)
    print("\nที่อยู่\n         ",address)
    print("\nเบอร์โทรศัพท์\n         ",tele)
    


def shop_5():
    global address,name
    import os
    html = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\pay.html"
    os.system(html)
    
    
    back = str(input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : '))
    if back == 'n':
        print('\nWelcome back\n')
        menu ()
    else:
        print('\nTHANK YOU\n')
        2
        x_1=" "
        for i in pro_3:
            x_1+=i+ "\n"
        data=sqlite3.connect("epp.db")
        c=data.cursor()
        c.execute(f'''INSERT INTO OrderAll (user,order_1,location) VALUES ("{name}","{x_1}","{address}")''' )
        data.commit()
        c.close()
        exit()
Big()

while True: 
    menu ()
    if choice == '1': 
        shop_1()
    elif choice == '2': 
        shop_2()
    elif choice == '3': 
        shop_3()    
    elif choice == '4': 
        shop_4() 
    elif choice == '5': 
        shop_5() 
        break