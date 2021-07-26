import string
import random
import csv
import re
choice=0
m=0
n=0
class Exam(object):
    def __init__(self):
        self.sname=0
        self.scollege=0
        self.sroll=0
        self.s_section=0
        self.Register()

    def portal(self):
        print("=" * 80)
        print(" ")
        print(" " * 30, "Welcome")
        print(" " * 20, "G H Raisoni University Portal")
        print(" ")
        print("=" * 80)
        print("", "1:Student", "2:Staff", sep=" " * 20)
        print("="*80)
        choice = int(input("Enter Where to Login:"))
        if choice == 1:
            print("Register Yourself On Raisoni Portal")
            print("="*30)
            print("You Choose login as A Student")
            self.Register()
        elif choice == 2:
            print("You Choose Login as Staff")
            print("=" * 30)

            self.Register()
    def Register(self):
        try:
            print("="*20)
            f = open("studentdata.csv", "w", newline="")
            a = csv.writer(f)  # here it will return csv writer object
            a.writerow(["username","Password"])
            print("Login first is Mandatory")
            username=input("Enter username=")
            self.u=username
            password=input("Enter Password=")
            self.p = password
            valids = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{4,10}$"
            pattern = re.compile(valids)
            matchers = re.search(pattern, password)
            if matchers:
                print("thank You")
            else:
                print('Password should have at least one of the symbols $@#')
                print('Password should have at least one lowercase letter')
                print('Password should have at least one uppercase letter')
                print('Password should have at least one numeral')
                exit()
            a.writerow([username,password])
            print("Registration Successfull!")
            print("="*20)
            print("Enter yes/No:")
            logs=input("Do you want to login?")
            if logs=="yes":
                self.login()
            else:
                print("Thank You")
                exit()
        except (ValueError,TypeError):
            print("Enter Valid Input Please Run the Code Again")


    def login(self):
        try:
            x=input("Username:")
            y=input("Password:")
            if x==self.u and y==self.p:
                print("Login successfully")
                self.getdata()
            else:
                print("Invalid username/password")
                exit()
        except (ValueError,TypeError):
            print("Enter Valid Input Please Run the Code Again")
            exit()

    def getdata(self):
        print("="*30)
        self.sname=input("Enter Your Full name=")
        self.scollege=input("Enter College Name=")
        self.sroll=int(input("Enter Roll_no="))
        self.s_section=input("Enter Section=")
        print("="*30)
        print("Choose Your Branch")
        print("1 = Computer Science Engg")
        print("2 = Mechanical Engg")
        print("3 = Civil Engg")
        print("4 = Architecture Dept")
        choice=int(input("Enter Your choice"))
        if choice==1:
            self.CSE()
        elif choice==2:
            self.CSE()
        elif choice==3:
            self.CSE()
        elif choice==4:
            self.CSE()
    def CSE(self):
        print("="*30)
        print("Choose Your Semester")
        print("1=First Semester")
        print("2=Second Semester")
        print("=" * 30)
        choice=int(input("Enter Your Choice="))
        if choice==1 or choice==2:
            put=input("Do you want to print marksheet yes/no:")
            if put=="yes":
                try:
                    S = 6  # number of characters in the string.
                    # call random.choices() string module to find the string in Uppercase + numeric data.
                    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
                    a = (str(ran))
                    print("-" * 15)
                    print("|", " " * 2, a, " " * 2, "|")
                    print("-" * 15)
                    capt = input("Enter Captcha=")
                    if capt == a:
                        self.calculate_marks()
                    elif capt:
                        print("Try again ")
                except (TypeError):
                    print("Enter Valid Input")

class Calculate(object):
    def calculate_marks(self):
        try:
            self.mydict = {}
            self.sub = int(input("How many subjects you have:"))
            self.i = 1
            while self.i <= self.sub:
                self.s1 = input("Enter Your subject:")
                self.m1 = int(input("Enter your marks:"))
                self.i = self.i + 1
                self.mydict[self.s1] = self.m1
                self.ram=self.mydict
            self.obtain = sum(self.mydict.values())
            self.rahim=self.sub*100
            self.percent = self.obtain / self.rahim * 100
        except (ValueError,TypeError):
            print("enter valid input")

class Assesment(Exam,Calculate):
    def __init__(self):
        Exam.__init__(self)
        Calculate.__init__(self)
        print(self.ram)
        print("─"*80)
        print(" "*20,"College Name:",self.scollege)
        print("─"*80)
        print(" "*20,"Student Name:",self.sname)
        print(" " * 20,"Section:",self.s_section)
        print(" " * 20,"Roll No:",self.sroll)
        print("─"*80)
        print("Subjects","Total","Obtained",sep=" "*20)
        for m,n in self.ram.items():
            self.length=int(len(m))
            print(m," "*(30-self.length),"100"," "*20,n)
            print(" ")
        print("─"*80)
        for j, l in self.ram.items():
            if l <= 40:
                print("Failed in ", j)
        for n in self.ram.values():
            if n>40:
                self.result = "pass"
            else:
                self.result = "Fail"
                break
        print("Total:",self.rahim," "*15,"Result:",self.result)
        print("Obtained Marks:",self.obtain)
        print("Percentage:",self.percent)
        print("─"*80)

obj=Assesment()














