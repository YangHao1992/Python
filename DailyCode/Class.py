class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course):
        print("%s is studying %s." % (self.name, course))
    
    def watchMovie(self):
        if self.age > 18:
            print("Can watch any movie.")
        else:
            print("Only can watch some movie.")

def main():
    stu = Student('Lyndon', 26)
    stu.study('math')
    stu.watchMovie()

if __name__ == '__main__':
    main()