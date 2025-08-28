from tkinter import Tk,Frame,Label,Entry,Button,messagebox,ttk
from tkinter import * 
import tkinter
from PIL import Image,ImageTk
from mysql.connector import connect

conn = connect(
    host = 'localhost',
    user = 'root', 
    password = 'Bhavi@123',
    database = 'project'
)
cursor = conn.cursor()
fonts = ('portland', 13)
fonts1 = ('portland', 15)
fonts2 = ('portland', 20, 'bold')
f1 = ('portland',13,'bold')
fonts3 = ('portland',20)


root = Tk()


class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("HOME")
        self.page = Frame(self.root,width=800,height=600)
        self.page.place(x=0,y=0)

        self.image = Image.open('../assets/bg2.png')
        self.image = self.image.resize((600,400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.place(x=0,y=0)
        self.main_label = Label(self.page ,bg = 'white' ,fg="black", text = 'WELCOME TO KALAKSHETRA', font = fonts1)
        self.main_label.place(x=160,y=50)
        self.main_label2 = Label(self.page , text = "FOLLOW YOUR PASSION" , font = fonts1)
        self.main_label2.place(x=185,y=110)
        self.main_label_btn = Button(self.page,text='ENTER',font=fonts1,command=self.home_login)
        self.main_label_btn.place(x=260,y=200)
        
    def home_login(self):    
        self.page.destroy()
        home_obj = Main(root)



class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right =Frame(self.root,width = 600,  height = 400,bg='#f7ebf3')
        self.right.place(x = 0, y = 0 )
        self.add_book_btn = Button(self.right,text = '⬅', font = fonts1,bg='white',fg='black',width=3,command = self.back)
        self.add_book_btn.place(x = 5, y = 5)

        self.admin_logo = Image.open('../assets/tut1.png')
        self.admin_logo = self.admin_logo.resize((100, 100))
        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)
        self.admin_logo_lbl = Label(self.right, image = self.admin_logo)
        self.admin_logo_lbl.place(x = 100, y= 30)


        self.admin__login = Label(self.right,text="Tutor login",bg='#f7ebf3')
        self.admin__login.place(x=125,y=135) 

        self.admin_name = Label(self.right, text = 'USER ID', bg = '#f7ebf3', fg ='black', font = fonts,width = 10)
        self.admin_name.place(x = 50, y = 170)
        self.admin_name_entry = Entry(self.right, width = 10, font = fonts)
        self.admin_name_entry.place(x = 150, y = 170)
        self.admin_pass = Label(self.right, text = 'PASSWORD', bg = '#f7ebf3', fg ='black', font = fonts, width = 10)
        self.admin_pass.place(x = 50, y = 200)
        self.admin_pass_entry = Entry(self.right, width = 10, font = fonts,show = "•")
        self.admin_pass_entry.place(x = 150, y = 200)

        self.admin_login_btn = Button(self.right, text = 'LOGIN',bg='white', font = fonts, command = self.login_admin)
        self.admin_login_btn.place(x = 100, y = 250)
        self.admin_or = Label(self.right, text = 'or', bg = '#f7ebf3', fg ='black', font =  fonts, width = 1,height=1)
        self.admin_or.place(x = 125, y = 291)
        self.admin_login_btn = Button(self.right, text = 'REGISTER',bg='white', font = fonts, command = self.admin_register)
        self.admin_login_btn.place(x = 85, y = 320)


        self.left =Frame(self.root, width = 600, height = 400,bg='#f7ebf3')
        self.left.place(x = 250, y = 0 )
        
        
      
        self.student_logo = Image.open('../assets/ler1.png')
        self.student_logo = self.student_logo.resize((100, 100))

        self.student_logo = ImageTk.PhotoImage(self.student_logo)

        self.student_logo_lbl = Label(self.left, image = self.student_logo)
        self.student_logo_lbl.place(x = 100, y= 30)



        self.student__login = Label(self.left,text="Learner login",bg='#f7ebf3')
        self.student__login.place(x=120,y=140) 


        self.student_name = Label(self.left, text = 'USER ID', bg = '#f7ebf3', fg ='black', font = fonts,width=10)
        self.student_name.place(x = 50, y = 170)
        self.student_name_entry = Entry(self.left, width = 10, font = fonts)
        self.student_name_entry.place(x = 150, y = 170)

        self.student_pass = Label(self.left, text = 'PASSWORD', bg = '#f7ebf3', fg ='black', font = fonts, width = 10)
        self.student_pass.place(x = 50, y = 200)
        self.student_pass_entry = Entry(self.left, width = 10, font = fonts,show = "•")
        self.student_pass_entry.place(x = 150, y = 200)

        self.student_login_btn = Button(self.left, text = 'LOGIN', bg='white',font = fonts,command = self.login_student)
        self.student_login_btn.place(x = 100, y = 250)
        self.student_or = Label(self.left, text = 'or', bg = '#f7ebf3', fg ='black', font = fonts, width = 1,height=1)
        self.student_or.place(x = 125, y = 291)
        self.student_login_btn = Button(self.left, text = 'REGISTER',bg='white', font = fonts,command = self.student_register)
        self.student_login_btn.place(x = 85, y = 320)
    def back(self):
        obj = Home(root)
    def login_admin(self):
        self.user_name = self.admin_name_entry.get()
        self.user_pass = self.admin_pass_entry.get()
        cursor.execute('select * from tutors;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.user_name in self.names:
            cursor.execute(f"select password from tutors where name = '{self.user_name}'")
            self.pasw = cursor.fetchall()
            self.pasw = [password[0] for password in self.pasw]
            if self.user_pass in self.pasw:
                self.right.destroy()
                self.left.destroy()
                admin_obj=Admin(root,self.user_name)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')
    def login_student(self):
        self.user_name = self.student_name_entry.get()
        self.user_pass = self.student_pass_entry.get()
        cursor.execute('select * from student;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.user_name in self.names:
            cursor.execute(f"select password from student where name = '{self.user_name}'")
            self.pasw = cursor.fetchall()
            self.pasw = [password[0] for password in self.pasw]
            if self.user_pass in self.pasw:
                self.right.destroy()
                self.left.destroy()
                student_obj = Student(root,self.user_name)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')
    def admin_register(self):
        self.right.destroy()
        self.left.destroy()
        admin_obj1 = Admin_Register(root)

    
    def student_register(self):
        self.right.destroy()
        self.left.destroy()
        admin_obj1 = Student_Register(root)



class Admin_Register:
    def __init__(self,root):
        self.root = root
        self.root.title("REGISTER DASHBOARD")
        self.right = Frame(self.root, width = 600,height = 400,bg = '#ecf7eb')
        self.right.place(x = 0,y=0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.admin_logo = Label(self.right,text="REGISTER",fg='black',bg='#ecf7eb',font=fonts3)
        self.admin_logo.place(x=240,y=30)
        self.admin_name = Label(self.right, text = 'NAME', bg = '#ecf7eb', fg ='black', font = fonts,width = 13)
        self.admin_name.place(x = 30, y = 100)
        self.admin_name_entry = Entry(self.right, width = 35, font = fonts)
        self.admin_name_entry.place(x = 200, y = 100)
        self.admin_phone = Label(self.right, text = 'PHONE NUMBER', bg = '#ecf7eb', fg ='black', font = fonts,width = 15)
        self.admin_phone.place(x = 30, y = 135)
        self.admin_phone_entry = Entry(self.right, width = 35, font = fonts)
        self.admin_phone_entry.place(x = 200, y = 135)
        self.admin_address = Label(self.right, text = 'ADDRESS', bg = '#ecf7eb', fg ='black', font = fonts,width = 13)
        self.admin_address.place(x = 30, y = 170)
        self.admin_address_entry = Entry(self.right, width = 35, font = fonts)
        self.admin_address_entry.place(x = 200, y = 170)
        self.admin_art = Label(self.right, text = 'ART', bg = '#ecf7eb', fg ='black', font = fonts,width = 13)
        self.admin_art.place(x = 30, y = 205)
        self.admin_art_entry = Entry(self.right, width = 35, font = fonts)
        self.admin_art_entry.place(x = 200, y = 205)
        self.admin_pass1 = Label(self.right, text = 'PASSWORD', bg = '#ecf7eb', fg ='black', font = fonts, width = 13)
        self.admin_pass1.place(x = 30, y = 240)
        self.admin_pass1_entry = Entry(self.right, width = 35, font = fonts,show = "•")
        self.admin_pass1_entry.place(x = 200, y = 240)
        self.admin_pass2 = Label(self.right, text = 'RE-ENTER PASSWORD', bg = '#ecf7eb', fg ='black', font = fonts, width = 20)
        self.admin_pass2.place(x = 8, y = 275)
        self.admin_pass2_entry = Entry(self.right, width = 35, font = fonts,show = "•")
        self.admin_pass2_entry.place(x = 200, y = 275)
        self.submit_btn = Button(self.right,text = 'SUBMIT', font = fonts,bg='white',fg='black',width=20,command = self.admin_register)
        self.submit_btn.place(x = 220, y = 320)
    
    def back(self):
        obj3 = Main(root)
    def admin_register(self):
        self.a_pass = self.admin_pass1_entry.get()
        self.b_pass = self.admin_pass2_entry.get()
        self.admin_name1 = self.admin_name_entry.get()
        self.admin_phone1 = self.admin_phone_entry.get()
        self.admin_art = self.admin_art_entry.get()
        self.admin_address1 = self.admin_address_entry.get()
        cursor.execute('select * from tutors;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.admin_name1 == '':
            messagebox.showerror('INVALID','ENTER A VALID NAME')
        elif self.admin_name1 in self.names:
            messagebox.showerror('INVALID','USERNAME ALREADY EXISTS')
        elif self.admin_phone1 == '':
            messagebox.showerror('INVALID','ENTER A VALID PHONE NUMBER')
        elif self.admin_address1 == '':
            messagebox.showerror('INVALID','ENTER A VALID ADDRESS')
        elif self.admin_art == '':
            messagebox.showerror('INVALID','ENTER A VALID ART')
        elif self.a_pass == '':
            messagebox.showerror('INVALID','ENTER A VALID PASSWORD')
        elif self.b_pass == '':
            messagebox.showerror('INVALID','RE-ENTER THE PASSWORD')
        elif self.a_pass != self.b_pass:
            messagebox.showerror('INVALID','PASSWORD MISMATCH')
        elif self.a_pass == self.b_pass:
            self.query = "insert into tutors(name, password, address,phone_no,art) values(%s,%s,%s,%s,%s)"
            self.values = (self.admin_name1,self.a_pass, self.admin_address1,self.admin_phone1,self.admin_art)
            cursor.execute(self.query, self.values)
            conn.commit()
            messagebox.showinfo('Account Created',f'UserName = "{self.admin_name1}"\nPassword = "{self.a_pass}"')
            self.right.destroy()
            admin_1 = Admin(root,self.admin_name1) 
        


class Student_Register:
    def __init__(self,root):
        self.root = root
        self.root.title("REGISTER DASHBOARD")
        self.right = Frame(self.root, width = 600,height = 400,bg = '#eeebf7')
        self.right.place(x = 0,y=0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.register_log = Label(self.right,text="REGISTER",fg='black',bg='#eeebf7',font=fonts3)
        self.register_log.place(x=240,y=30)
        self.student_name = Label(self.right, text = 'NAME', bg = '#eeebf7', fg ='black', font = fonts,width = 13)
        self.student_name.place(x = 30, y = 100)
        self.student_name_entry = Entry(self.right, width = 35, font = fonts)
        self.student_name_entry.place(x = 200, y = 100)
        self.student_phone = Label(self.right, text = 'PHONE NUMBER', bg = '#eeebf7', fg ='black', font = fonts,width = 15)
        self.student_phone.place(x = 30, y = 135)
        self.student_phone_entry = Entry(self.right, width = 35, font = fonts)
        self.student_phone_entry.place(x = 200, y = 135)
        self.student_address = Label(self.right, text = 'ADDRESS', bg = '#eeebf7', fg ='black', font = fonts,width = 13)
        self.student_address.place(x = 30, y = 170)
        self.student_address_entry = Entry(self.right, width = 35, font = fonts)
        self.student_address_entry.place(x = 200, y = 170)
        self.student_pass1 = Label(self.right, text = 'PASSWORD', bg = '#eeebf7', fg ='black', font = fonts, width = 13)
        self.student_pass1.place(x = 30, y = 210)
        self.student_pass1_entry = Entry(self.right, width = 35, font = fonts,show = "•")
        self.student_pass1_entry.place(x = 200, y = 210)
        self.student_pass2 = Label(self.right, text = 'RE-ENTER PASSWORD', bg = '#eeebf7', fg ='black', font = fonts, width = 20)
        self.student_pass2.place(x = 8, y = 240)
        self.student_pass2_entry = Entry(self.right, width = 35, font = fonts,show = "•")
        self.student_pass2_entry.place(x = 200, y = 240)
        self.add_book_btn = Button(self.right,text = 'SUBMIT', font = fonts,bg='white',fg='black',width=20,command = self.student_register)
        self.add_book_btn.place(x = 220, y = 300)
  
    def back(self):
        obj4 = Main(root)
    def student_register(self):

        self.a_pass = self.student_pass1_entry.get()
        self.b_pass = self.student_pass2_entry.get()
        self.student_name1 = self.student_name_entry.get()
        self.student_phone1 = self.student_phone_entry.get()
        self.student_address1 = self.student_address_entry.get()
        cursor.execute('select * from student;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.student_name1 == '':
            messagebox.showerror('INVALID','ENTER A VALID NAME')
        elif self.student_name1 in self.names:
            messagebox.showerror('INVALID','USERNAME ALREADY EXISTS')
        elif self.student_phone1 == '':
            messagebox.showerror('INVALID','ENTER A VALID PHONE NUMBER')
        elif self.student_address1 == '':
            messagebox.showerror('INVALID','ENTER A VALID ADDRESS')
        elif self.a_pass == '':
            messagebox.showerror('INVALID','ENTER A VALID PASSWORD')
        elif self.b_pass == '':
            messagebox.showerror('INVALID','RE-ENTER THE PASSWORD')
        elif self.a_pass != self.b_pass:
            messagebox.showerror('INVALID','PASSWORD MISMATCH')
        elif self.a_pass == self.b_pass:
            self.query = "insert into student(name, password, address,phone_no) values(%s,%s,%s,%s)"
            self.values = (self.student_name1,self.a_pass, self.student_address1,self.student_phone1)
            cursor.execute(self.query, self.values)
            conn.commit()
            messagebox.showinfo('Account Created',f'UserName = "{self.student_name1}"\nPassword = "{self.a_pass}"')
            self.right.destroy()
            admin_1 = Student(root,self.student_name1) 



class Admin:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("TUTOR DASHBOARD")
        self.right = Frame(self.root, width = 600, height = 400,bg='#d3e9eb')
        self.right.place(x = 0, y = 0)
        self.logout_btn = Button(self.right,text = 'logout', font = fonts,bg='white',fg='black',width=10,command = self.logout)
        self.logout_btn.place(x = 490, y = 5)
        self.admin__login = Label(self.right,text="Welcome to Kalakshetra",bg='#d3e9eb',fg='black',font=fonts3)
        self.admin__login.place(x=160,y=60)
       
        self.edit_btn = Button(self.right,text = 'EDIT PROFILE', font = fonts,fg='black',width=20,command = self.edit)
        self.edit_btn.place(x = 200, y = 135)
        self.price_btn = Button(self.right,text = 'PRICE BOUNDARY', font = fonts,fg='black',width=20,command = self.price)
        self.price_btn.place(x = 200, y = 170)
        self.delete_btn = Button(self.right,text = 'DELETE PROFILE', font = fonts,fg='black' ,width=20,command = self.delete)
        self.delete_btn.place(x = 200, y = 205)
        self.help_btn = Button(self.right,text = 'HELP', font = fonts,fg='black',width=20,command=self.help)
        self.help_btn.place(x = 200, y = 240)
    def help(self):
        self.right.destroy()
        obj = Help_admin(root,self.user_name)
    def price(self):
        self.right.destroy()
        obj = Price_boundary(root,self.user_name)
    def edit(self):
        self.right.destroy()
        obj = Edit_admin(root,self.user_name)
    
    def delete(self):
        self.right.destroy()
        obj = Delete_Admin(root,self.user_name)
  
    def logout(self):
        obj2 =  Main(root)



class Student:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("LEARNER DASHBOARD")
        self.right = Frame(self.root, width = 600, height = 400,bg='#d3e9eb')
        self.right.place(x = 0, y = 0)
        self.logout_btn = Button(self.right,text = 'logout', font = fonts,bg='white',fg='black',width=10,command = self.back)
        self.logout_btn.place(x = 490, y = 5)

        self.admin__login = Label(self.right,text="Welcome to Kalakshetra",bg='#d3e9eb',fg='black',font=fonts3)
        self.admin__login.place(x=150,y=60)
       
        self.edit_btn = Button(self.right,text = 'EDIT PROFILE', font = fonts,fg='black',width=22,command = self.edit)
        self.edit_btn.place(x = 180, y = 135)
        self.search_btn = Button(self.right,text = 'ARTS', font = fonts,fg='black',width=22,command = self.search)
        self.search_btn.place(x = 180, y = 170)
        self.delete_btn = Button(self.right,text = 'DELETE PROFILE', font = fonts,fg='black' ,width=22,command= self.delete)
        self.delete_btn.place(x = 180, y = 205)
        self.help_btn = Button(self.right,text = 'HELP', font = fonts,fg='black',width=22,command = self.help)
        self.help_btn.place(x = 180, y = 240)
    def search(self):
        self.right.destroy()
        obj = Search_student(root,self.user_name)
    def back(self):
        obj2 = Main(root)
    def delete(self):
        self.right.destroy()
        obj = Delete_Student(root,self.user_name)
    def edit(self):
        self.right.destroy()
        obj = Edit_student(root,self.user_name)

    def help(self):
        self.right.destroy()
        obj = Help_student(root,self.user_name)



class Search_student:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("ART SEARCH")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        cursor.execute('select * from tutors;')
        self.data = cursor.fetchall()
        self.list1 = [art[4] for art in self.data]
        self.list1 = list(set(self.list1))
        self.role_var = tkinter.StringVar()
        self.role_var.set("search hear....")
        self.cmb = ttk.Combobox(self.root,textvariable=self.role_var,value= self.list1,width=30,font=fonts,height=10)
        self.cmb.place(x=150,y=100)
        self.cmbb = Button(self.right,text="search", font = fonts,bg='white',fg='black',width=10,command = self.search)
        self.cmbb.place(x=250,y=150)

    def search(self):
        self.art=self.role_var.get()
        self.n = len(self.list1)
        for x in range(self.n):
            if self.art == self.list1[x]:
                self.right.destroy()
                obj=Search_art(root,self.user_name,self.art)
                break
                
        else:
            messagebox.showinfo('Use Arrow',"Use arrow to acknowledge the existence of art")
    def back(self):
        self.right.destroy()
        obj2 = Student(root,self.user_name)



class Search_art:
    def __init__(self,root,user_name,art):
        self.root = root
        self.user_name = user_name
        self.art = art
        self.root.title(art)
        self.right = Frame(self.root,width=600,height=400,bg='#faf0f0')
        self.right.pack(fill=BOTH,expand=1)
        self.my_canvas = Canvas(self.right)
        self.my_canvas.pack(side = LEFT,fill=BOTH,expand=1)
        self.my_scrollbar = ttk.Scrollbar(self.right,orient=VERTICAL,command=self.my_canvas.yview)
        self.my_scrollbar.pack(side = RIGHT,fill=Y)
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>',lambda e : self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))
        self.second_frame = Frame(self.my_canvas,bg = '#faf0f0')
        self.my_canvas.create_window((0,0), window=self.second_frame,anchor="nw")
        cursor.execute('select * from tutors;')
        self.data = cursor.fetchall()
        self.name1 = [name[0] for name in self.data]
        self.phone1 = [phone[3] for phone in self.data]
        self.add1 = [add[2] for add in self.data]
        self.art1 = [art2[4] for art2 in self.data]
        self.m = len(self.name1)
        self.name = []
        self.add = []
        self.phone_no = []
        for i in range(self.m):
            if self.art == self.art1[i]:
                self.name.append(self.name1[i])
                self.add.append(self.add1[i])
                self.phone_no.append(self.phone1[i])
        self.n = len(self.name)
        for i in range(0,self.n-1,2):
            Label(self.second_frame,text= f" Name : {self.name[i]} \n Address : {self.add[i]} \n Phone Number : {self.phone_no[i]}",height=5,width=35,fg="black",font=fonts).grid(row=i,column=0)
            Label(self.second_frame,text= f" Name : {self.name[i+1]} \n Address : {self.add[i+1]} \n Phone Number : {self.phone_no[i+1]}",height=5,width=35,fg="black",font=fonts).grid(row=i,column=1)
        if self.n%2 != 0:
            self.i = self.n -1
            Label(self.second_frame,text= f" Name : {self.name[self.i]} \n Address : {self.add[self.i]} \n Phone Number : {self.phone_no[self.i]}",height=5,width=35,fg="black",font=fonts).grid(row=self.i,column=0)
        Button(self.second_frame,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back).place(x=5,y=5)

    def back(self):
        self.right.destroy()
        self.second_frame.destroy()
        obj2 = Search_student(root,self.user_name)




class Help_admin:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("HELP")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.admin__login = Label(self.right,text="Profile Management for Tutors:",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=40)
        self.admin__login = Label(self.right,text="• Once registered, tutors have the option to delete their profiles using ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=75)
        self.admin__login = Label(self.right,text="the delete option. ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=100)
        self.admin__login = Label(self.right,text="• Tutors have the flexibility to set price boundaries according to ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=130)
        self.admin__login = Label(self.right,text="their preferences. ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=155)
        self.admin__login = Label(self.right,text="• Additionally, they can edit their profiles using the edit option",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=185)
        self.admin__login = Label(self.right,text="if necessary.",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=215)
        
        


    def back(self):
        self.right.destroy()
        obj2 = Admin(root,self.user_name)




class Help_student:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("HELP")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.admin__login = Label(self.right,text="Profile Management for Learner:",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=40)
        self.admin__login = Label(self.right,text="• Once registered, Learners have the option to delete their profiles using ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=75)
        self.admin__login = Label(self.right,text="the delete option. ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=100)
        self.admin__login = Label(self.right,text="• Learners have the opportunity to select their preferred arts based ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=130)
        self.admin__login = Label(self.right,text="on their interests. ",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=155)
        self.admin__login = Label(self.right,text="• Additionally, they can edit their profiles using the edit option",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=185)
        self.admin__login = Label(self.right,text="if necessary.",bg='#faf0f0',fg='black',font=fonts)
        self.admin__login.place(x=5,y=215)
        

    def back(self):
        self.right.destroy()
        obj2 = Student(root,self.user_name)




class Price_boundary:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("PRICE BOUNDARY")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.admin__login = Label(self.right,text="Select Price",bg='#faf0f0',fg='black',font=fonts3)
        self.admin__login.place(x=210,y=30)
       
        self.edit_btn = Button(self.right,text = '1k - 3k', font = fonts,fg='black',width=20,command = self.one)
        self.edit_btn.place(x = 200, y = 100)
        self.viewer_btn = Button(self.right,text = '3k - 5k', font = fonts,fg='black',width=20,command = self.two)
        self.viewer_btn.place(x = 200, y = 135)
        self.price_btn = Button(self.right,text = '5k - 7k', font = fonts,fg='black',width=20,command = self.three)
        self.price_btn.place(x = 200, y = 170)
        self.delete_btn = Button(self.right,text = '7k - 9k', font = fonts,fg='black' ,width=20,command = self.four)
        self.delete_btn.place(x = 200, y = 205)
        self.help_btn = Button(self.right,text = '9k - 10k', font = fonts,fg='black',width=20,command = self.five)
        self.help_btn.place(x = 200, y = 240)

    def one(self):
        cursor.execute(f"UPDATE tutors SET price = '1k - 3k' WHERE name = '{self.user_name}';")
        conn.commit()
        self.right.destroy()
        obj1 = Admin(root,self.user_name)
    def two(self):
        cursor.execute(f"UPDATE tutors SET price = '3k - 5k' WHERE name = '{self.user_name}';")
        conn.commit()
        self.right.destroy()
        obj1 = Admin(root,self.user_name)
    def three(self):
        cursor.execute(f"UPDATE tutors SET price = '5k - 7k' WHERE name = '{self.user_name}';")
        conn.commit()
        self.right.destroy()
        obj1 = Admin(root,self.user_name)
    def four(self):
        cursor.execute(f"UPDATE tutors SET price = '7k - 9k' WHERE name = '{self.user_name}';")
        conn.commit()
        self.right.destroy()
        obj1 = Admin(root,self.user_name)
    def five(self):
        cursor.execute(f"UPDATE tutors SET price = '9k - 10k' WHERE name = '{self.user_name}';")
        conn.commit()
        self.right.destroy()
        obj1 = Admin(root,self.user_name)


    def back(self):
        obj2 = Admin(root,self.user_name)




class Delete_Admin:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        cursor.execute(f"select password from tutors where name = '{self.user_name}'")
        self.pasw = cursor.fetchall()
        self.pasw = [passw[0] for passw in self.pasw]
        self.passw = self.pasw[0]
        self.root.title("DELETE PROFILE")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.delete_name = Label(self.right, text = 'NAME', bg = '#faf0f0', fg ='black', font = fonts,width = 10)
        self.delete_name.place(x = 50, y = 120)
        self.delete_name_entry = Entry(self.right, width = 20, font = fonts)
        self.delete_name_entry.place(x = 200, y = 120)
        self.delete_pass = Label(self.right, text = 'PASSWORD', bg = '#faf0f0', fg ='black', font = fonts,width = 10)
        self.delete_pass.place(x = 50, y = 170)
        self.delete_pass_entry = Entry(self.right, width = 20, font = fonts,show= "•")
        self.delete_pass_entry.place(x = 200, y = 170)
        self.submit_btn = Button(self.right,text = 'SUBMIT', font = fonts,bg='white',fg='black',width=20,command = self.delete)
        self.submit_btn.place(x = 220, y = 300)
        
    def delete(self):
        self.delete1 = self.delete_name_entry.get()
        self.delete2 = self.delete_pass_entry.get()
        if self.delete1 == self.user_name :
            if self.delete2 == self.passw :
                cursor.execute(f"DELETE FROM tutors WHERE name = '{self.delete1}'")
                conn.commit()
                messagebox.showinfo('Account Deleted','YOUR ACCOUNT IS DELETED')
                self.right.destroy()
                admin_1 = Main(root)
            else:
                messagebox.showerror('INVALID','ENTER A VALID PASSWORD')
        else:
            messagebox.showerror('INVALID','ENTER A VALID NAME')
    def back(self):
        obj2 = Admin(root,self.user_name)



class Delete_Student:
    def __init__(self, root,user_name):
        self.root = root
        self.user_name = user_name
        cursor.execute(f"select password from student where name = '{self.user_name}'")
        self.pasw = cursor.fetchall()
        self.pasw = [passw[0] for passw in self.pasw]
        self.passw = self.pasw[0]
        self.root.title("DELETE PROFILE")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.back_btn = Button(self.right,text = '⬅', font = fonts,bg='white',fg='black',width=3,command = self.back)
        self.back_btn.place(x = 5, y = 5)
        self.delete_name = Label(self.right, text = 'NAME', bg = '#faf0f0', fg ='black', font = fonts,width = 10)
        self.delete_name.place(x = 50, y = 120)
        self.delete_name_entry = Entry(self.right, width = 20, font = fonts)
        self.delete_name_entry.place(x = 200, y = 120)
        self.delete_pass = Label(self.right, text = 'PASSWORD', bg = '#faf0f0', fg ='black', font = fonts,width = 10)
        self.delete_pass.place(x = 50, y = 170)
        self.delete_pass_entry = Entry(self.right, width = 20, font = fonts,show="•")
        self.delete_pass_entry.place(x = 200, y = 170)
        self.submit_btn = Button(self.right,text = 'SUBMIT', font = fonts,bg='white',fg='black',width=20,command = self.delete)
        self.submit_btn.place(x = 220, y = 300)
        
    def delete(self):
        self.delete1 = self.delete_name_entry.get()
        self.delete2 = self.delete_pass_entry.get()
        if self.delete1 == self.user_name :
            if self.delete2 == self.passw :
                cursor.execute(f"DELETE FROM student WHERE name = '{self.delete1}'")
                conn.commit()
                messagebox.showinfo('Account Deleted','YOUR ACCOUNT IS DELETED')
                self.right.destroy()
                admin_1 = Main(root) 
            else:
                messagebox.showerror('INVALID','ENTER A VALID PASSWORD')
        else:
            messagebox.showerror('INVALID','ENTER A VALID NAME')
    def back(self):
        obj2 = Student(root,self.user_name)
        



class Edit_student:
    def __init__(self,root,user_name):
        self.root = root
        self.user_name = user_name
        cursor.execute('select * from student;')
        self.data = cursor.fetchall()
        cursor.execute(f"select password from student where name = '{self.user_name}'")
        self.pasw = cursor.fetchall()
        self.pasw = [passw[0] for passw in self.pasw]
        self.passw = self.pasw[0]
        cursor.execute(f"select phone_no from student where name = '{self.user_name}'")
        self.phone = cursor.fetchall()
        self.phone = [phon[0] for phon in self.phone]
        self.phone_no = self.phone[0]
        cursor.execute(f"select address from student where name = '{self.user_name}'")
        self.add = cursor.fetchall()
        self.add = [addr[0] for addr in self.add]
        self.address = self.add[0]
        self.root.title("EDIT PROFILE")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.student_name = Label(self.right, text = 'NAME', bg = '#faf0f0', fg ='black', font = fonts,width = 13)
        self.student_name.place(x = 30, y = 65)
        self.student_name_entry = Entry(self.right, width = 30, font = fonts)
        self.student_name_entry.place(x = 220, y = 65)
        self.student_name_entry.insert(0,f"{self.user_name}")
        self.student_phone = Label(self.right, text = 'PHONE NUMBER', bg = '#faf0f0', fg ='black', font = fonts,width = 14)
        self.student_phone.place(x = 30, y = 100)
        self.student_phone_entry = Entry(self.right, width = 30, font = fonts)
        self.student_phone_entry.place(x = 220, y = 100)
        self.student_phone_entry.insert(0,f"{self.phone_no}")
        self.student_address = Label(self.right, text = 'ADDRESS', bg = '#faf0f0', fg ='black', font = fonts,width = 13)
        self.student_address.place(x = 30, y = 135)
        self.student_address_entry = Entry(self.right, width = 30, font = fonts)
        self.student_address_entry.place(x = 220, y = 135)
        self.student_address_entry.insert(0,f"{self.address}")
        self.student_pass1 = Label(self.right, text = 'PASSWORD', bg = '#faf0f0', fg ='black', font = fonts, width = 13)
        self.student_pass1.place(x = 30, y = 170)
        self.student_pass1_entry = Entry(self.right, width = 30, font = fonts,show = "•")
        self.student_pass1_entry.place(x = 220, y = 170)
        self.student_pass1_entry.insert(0,f"{self.passw}")
        self.student_pass2 = Label(self.right, text = 'RE-ENTER PASSWORD', bg = '#faf0f0', fg ='black', font = fonts, width = 20)
        self.student_pass2.place(x = 8, y = 210)
        self.student_pass2_entry = Entry(self.right, width = 30, font = fonts,show = "•")
        self.student_pass2_entry.place(x = 220, y = 210)
        self.student_pass2_entry.insert(0,f"{self.passw}") 
        self.save_btn = Button(self.right,text = 'SAVE', font = fonts,bg='white',fg='black',width=20,command = self.student_save)
        self.save_btn.place(x = 220, y = 265)
        self.cancle_btn = Button(self.right,text = 'CANCEL', font = fonts,bg='white',fg='black',width=20,command = self.back)
        self.cancle_btn.place(x = 220, y =320)
    def back(self):
        obj2 = Student(root,self.user_name)
    def student_save(self):
        self.a_pass = self.student_pass1_entry.get()
        self.b_pass = self.student_pass2_entry.get()
        self.student_name1 = self.student_name_entry.get()
        self.student_phone1 = self.student_phone_entry.get()
        self.student_address1 = self.student_address_entry.get()

        if self.student_name1 != self.user_name :
            messagebox.showerror('INVALID','ENTER A VALID NAME')
        elif self.student_phone1 != '':
            cursor.execute(f"UPDATE student SET phone_no = '{self.student_phone1}' WHERE name = '{self.student_name1}';")
            conn.commit()
        elif self.student_address1 != '':
            cursor.execute(f"UPDATE student SET address = '{self.student_address1}' WHERE name = '{self.student_name1}';")
            conn.commit()
        if self.a_pass != '':
            if self.b_pass != '':
                if self.a_pass == self.b_pass:
                    cursor.execute(f"UPDATE student SET password = '{self.a_pass}' WHERE name = '{self.student_name1}'")
                    conn.commit()
                else:
                    messagebox.showerror('INVALID','PASSWORD MISMATCH') 
            else:
                messagebox.showerror('INVALID','RE-ENTER THE PASSWORD')
                
        if 1==0:
            messagebox.showerror('INVALID','PASSWORD MISMATCH')
        elif (self.a_pass != '' or self.student_address1 != '' or self.student_phone1 != '' ) and (self.a_pass == self.b_pass):
            messagebox.showinfo('Account Edited','YOUR ACCOUNT IS EDITED')
            self.right.destroy()
            obj2 = Student(root,self.student_name1)


class Edit_admin:
    def __init__(self,root,user_name):
        self.root = root
        self.user_name = user_name 
        cursor.execute('select * from tutors;')
        self.data = cursor.fetchall()
        cursor.execute(f"select password from tutors where name = '{self.user_name}'")
        self.pasw = cursor.fetchall()
        self.pasw = [passw[0] for passw in self.pasw]
        self.passw = self.pasw[0]
        cursor.execute(f"select phone_no from tutors where name = '{self.user_name}'")
        self.phone = cursor.fetchall()
        self.phone = [phon[0] for phon in self.phone]
        self.phone_no = self.phone[0]
        cursor.execute(f"select address from tutors where name = '{self.user_name}'")
        self.add = cursor.fetchall()
        self.add = [addr[0] for addr in self.add]
        self.address = self.add[0]
        self.root.title("EDIT PROFILE")
        self.right = Frame(self.root, width = 600, height = 400,bg='#faf0f0')
        self.right.place(x = 0, y = 0)
        self.admin_name = Label(self.right, text = 'NAME', bg = '#faf0f0', fg ='black', font = fonts,width = 13)
        self.admin_name.place(x = 30, y = 65)
        self.admin_name_entry = Entry(self.right, width = 30, font = fonts)
        self.admin_name_entry.place(x = 220, y = 65)
        self.admin_name_entry.insert(0,f"{self.user_name}")
        self.admin_phone = Label(self.right, text = 'PHONE NUMBER', bg = '#faf0f0', fg ='black', font = fonts,width = 14)
        self.admin_phone.place(x = 30, y = 100)
        self.admin_phone_entry = Entry(self.right, width = 30, font = fonts)
        self.admin_phone_entry.place(x = 220, y = 100)
        self.admin_phone_entry.insert(0,f"{self.phone_no}")
        self.admin_address = Label(self.right, text = 'ADDRESS', bg = '#faf0f0', fg ='black', font = fonts,width = 13)
        self.admin_address.place(x = 30, y = 135)
        self.admin_address_entry = Entry(self.right, width = 30, font = fonts)
        self.admin_address_entry.place(x = 220, y = 135)
        self.admin_address_entry.insert(0,f"{self.address}")
        self.admin_pass1 = Label(self.right, text = 'PASSWORD', bg = '#faf0f0', fg ='black', font = fonts, width = 13)
        self.admin_pass1.place(x = 30, y = 170)
        self.admin_pass1_entry = Entry(self.right, width = 30, font = fonts,show = "•")
        self.admin_pass1_entry.place(x = 220, y = 170)
        self.admin_pass1_entry.insert(0,f"{self.passw}")
        self.admin_pass2 = Label(self.right, text = 'RE-ENTER PASSWORD', bg = '#faf0f0', fg ='black', font = fonts, width = 20)
        self.admin_pass2.place(x = 8, y = 210)
        self.admin_pass2_entry = Entry(self.right, width = 30, font = fonts,show = "•")
        self.admin_pass2_entry.place(x = 220, y = 210)
        self.admin_pass2_entry.insert(0,f"{self.passw}")
        self.save_btn = Button(self.right,text = 'SAVE', font = fonts,bg='white',fg='black',width=20,command = self.admin_save)
        self.save_btn.place(x = 220, y = 265)
        self.cancle_btn = Button(self.right,text = 'CANCEL', font = fonts,bg='white',fg='black',width=20,command = self.back)
        self.cancle_btn.place(x = 220, y =320)
    def back(self):
        obj2 = Admin(root,self.user_name)
    def admin_save(self):
        self.a_pass = self.admin_pass1_entry.get()
        self.b_pass = self.admin_pass2_entry.get()
        self.admin_name1 = self.admin_name_entry.get()
        self.admin_phone1 = self.admin_phone_entry.get()
        self.admin_address1 = self.admin_address_entry.get()
        if self.admin_name1 != self.user_name :
            messagebox.showerror('INVALID','ENTER A VALID NAME')
        elif self.admin_phone1 != '':
            cursor.execute(f"UPDATE tutors SET phone_no = '{self.admin_phone1}' WHERE name = '{self.admin_name1}';")
            conn.commit()
        elif self.admin_address1 != '':
            cursor.execute(f"UPDATE tutors SET address = '{self.admin_address1}' WHERE name = '{self.admin_name1}';")
            conn.commit()
        elif self.a_pass != '':
            if self.b_pass != '':
                if self.a_pass == self.b_pass:
                    cursor.execute(f"UPDATE tutors SET password = '{self.a_pass}' WHERE name = '{self.admin_name1}';")
                    conn.commit()
                else:
                    messagebox.showerror('INVALID','PASSWORD MISMATCH') 
            else:
                messagebox.showerror('INVALID','RE-ENTER THE PASSWORD')
        #elif self.a_pass == self.b_pass:
        if 1==0:
            messagebox.showerror('INVALID','PASSWORD MISMATCH')
        elif  (self.admin_phone1 != '' or self.a_pass != '' or  self.admin_address1 != ''  or self.b_pass != '' ) and (self.a_pass == self.b_pass):
            messagebox.showinfo('Account Edited','YOUR ACCOUNT IS EDITED')
            self.right.destroy()
            obj2 = Admin(root,self.user_name)



        

root.geometry('600x400+550+200')
home = Home(root)
root.mainloop()