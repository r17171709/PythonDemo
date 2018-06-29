class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.teachers = list()
        self.students = list()

    def enroll(self, stu_obj):
        print("为%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, teacher_obj):
        print("雇佣了%s教授%s" % (teacher_obj.name, teacher_obj.course))
        self.teachers.append(teacher_obj)


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""
        ---- info of Teacher: %s ----
        Age:%s
        Sex:%s
        Salaty:%s
        Course:%s
        """ % (self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print("""
        ---- info of Student: %s ----
        Age:%s
        Sex:%s
        StuId:%s
        Grade:%s
        """ % (self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tuition for $%s" % (self.name, amount))


school = School("IT班", "位置地址")
t1 = Teacher("老师1", 30, "m", "16000", "Android")
t2 = Teacher("老师2", 28, "f", "16000", "Medical")
s1 = Student("学生1", 3, "f", "1", "Android")
s2 = Student("学生2", 3, "f", "2", "Medical")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
for teacher in school.teachers:
    teacher.teach()
for student in school.students:
    student.pay_tuition(15000)
