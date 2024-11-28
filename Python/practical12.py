#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#class University
class University:
    def __init__(self,name,year_of_estd,city):
        self.name = name
        self.year_of_estd = year_of_estd
        self.city = city
    
    def display(self):
        print("Name:",self.name)
        print("Year of Establishment:",self.year_of_estd)
        print("City:",self.city)
        
#class professor
class professor(University):
    def __init__(self,name,year_of_estd,city,designation, highest_qualification, area_of_research, year_of_joining, year_of_experience, name_of_institute):
        super().__init__(name,year_of_estd,city)
        self.designation = designation
        self.highest_qualification = highest_qualification
        self.area_of_research = area_of_research
        self.year_of_joining = year_of_joining
        self.year_of_experience = year_of_experience
        self.name_of_institute = name_of_institute
    
    def display(self):
        super().display()
        print("Designation:",self.designation)
        print("Highest Qualification:",self.highest_qualification)
        print("Area of Research:",self.area_of_research)
        print("Year of Joining:",self.year_of_joining)
        print("Year of Experience:",self.year_of_experience)
        print("Name of Institute:",self.name_of_institute)

#class lab_assistant        
class lab_assistant(University):
    designation = "Lab Assistant"
    def __init__(self, name, year_of_estd, city,highest_qualification, additiobnal_skills, year_of_joining, name_of_institue):
        super().__init__(name, year_of_estd, city)
        self.highest_qualification = highest_qualification
        self.additiobnal_skills = additiobnal_skills
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institue

    def display(self):
        super().display()
        print("Designation:",self.designation)
        print("Highest Qualification:",self.highest_qualification)
        print("Additiobnal Skills:",self.additiobnal_skills)
        print("Year of Joining:",self.year_of_joining)
        print("Name of Institute:",self.name_of_institute)

#class office_assistant
class office_assistant(University):
    designation = "Office Assistant"
    def __init__(self, name, year_of_estd, city,highest_qualification, year_of_joining,name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.highest_qualification = highest_qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute

    def display(self):
        super().display()
        print("Designation:",self.designation)
        print("Highest Qualification:",self.highest_qualification)
        print("Year of Joining:",self.year_of_joining)
        print("Name of Institute:",self.name_of_institute)

#class peon
class peon(University):
    job_role = "Office peon"
    def __init__(self, name, year_of_estd, city,qualification,year_of_joining,name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.qualification = qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute

    def display(self):
        super().display()
        print("Designation:",self.job_role)
        print("Qualification:",self.qualification)
        print("Year of Joining:",self.year_of_joining)
        print("Name of Institute:",self.name_of_institute)

#display of university detais 
print("###University Details###")
uni= University("Uka Tarsadia University",2011,"Surat")
uni.display()

#display of professor information
print("\n###Professor Details###")
prof= professor("Suresh","2011","Surat","xyz","PhD","programming",2014, 9,"abc")
prof.display()

#display of lab assistant information
print("\n###Lab Assistant Details###")
lab= lab_assistant("Ramesh","2011","Surat","Post Graduate","Web Developing",2020,"abc")
lab.display()

#display of office assistant information
print("\n###Office Assistant Details###")
office= office_assistant("Shyam","2011","Surat","Post Graduate",2017,"abc")
office.display()

#display of peon information
print("\n###Peon Details###")
peo= peon("Ram","2011","Surat","Graduate",2016,"abc")
peo.display()   