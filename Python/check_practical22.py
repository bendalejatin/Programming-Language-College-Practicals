#Name: Jatin Bendale
#Enrollment Number: 202203103510038

class student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def get_data(self):
        print("Student name:", self.name)
        print("Student branch:", self.branch)
