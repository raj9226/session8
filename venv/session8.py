"""
 Student
 name
 phone
 email
 password
 isCollegeTraining
 collegeName
 rollNum


class student:
    pass


s1=student()
s2=student()
s1.name="John"
s1.phone="+92....333"
s1.email="zoo@example.com"
s1.password="pass123"
s1.isCollegeataraining=True
s1.collegeName="ABC International"
s1.rollNum=24
"""
"""
print(s1.__dict__)

s2.fullName = "Fionna"
s2.phn = "+91 8888 77777"
s2.email = "fionna@example.cm"
s2.passphrase = "pass123"
s2.isCollegeTraining = True
s2.collegeName = "ABC International"
s2.rollnum = 24

print(s2.__dict__)
"""
#challenge=No standarisation
#solution= constructor
#self is a refereence variable which will hold the hashcode of current object
#__init__ is a known as constructor
#constructo is property of class
class student:
    def __init__(self,name,phone,email,password,isCollegeTraininig,collegeNmae,rollnum):
        print(">>self is:",self)
        self.fullName=name
        self.phone=phone
        self.email=email
        self.password=password
        self.isCollegeTraining=isCollegeTraininig
        self.collegeName=collegeNmae
        self.rollNum=rollnum
        #over-writing:::A new constructor will be created and old will be deleted
    """def __init__(self,name,phone):
        self.name=name
        self.phone=phone"""
    def showStudentDetail(self):
        print("=============================")
        print("detail of ",self.fullName)
        print("phone:\t",self.phone)
        print("Roll:",self.rollNum)

s1=student("John","+9233....444","zoo@example.com","pass123",True,"Gne","24")
print("s1 is:",s1)
s2=student("FIONNA","+9233....344","zoooo@example.com","pass1234",True,"international","34")
print("s2 is:",s2)
s1.age=22
s1.vehicleNum="PB10AB1234"

s1.fullName="John watson"
s2.fullName="Fionna Flynn"

#del s1.age
#del s2.phone
#print(s1.__dict__)
#print(s2.__dict__)
student.showStudentDetail(s1)
student.showStudentDetail(s2)
print()

print(s1.__dict__)
print(student.__dict__)
