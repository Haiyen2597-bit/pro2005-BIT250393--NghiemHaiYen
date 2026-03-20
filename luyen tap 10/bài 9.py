class Person:

    def __init__(self, name, age):
        if not isinstance(name, str) or not name:
            raise ValueError("Tên phải là chuỗi không rỗng")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Tuổi phải là số nguyên >= 0")
        self._name = name
        self._age = age


    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


    def set_name(self, name):
        if not name:
            raise ValueError("Tên không được rỗng")
        self._name = name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không được âm")
        self._age = age


    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"


    def greet(self):
        print(f"Xin chào, tôi là {self._name}, {self._age} tuổi")


    @classmethod
    def class_info(cls):
        print(f"Đây là class {cls.__name__}")


    @staticmethod
    def is_adult(age):
        return age >= 18


    def __eq__(self, other):
        if isinstance(other, Person):
            return self._name == other._name and self._age == other._age
        return False



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # gọi constructor cha
        if not student_id:
            raise ValueError("Mã sinh viên không được rỗng")
        self._student_id = student_id


    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        if not student_id:
            raise ValueError("Mã sinh viên không được rỗng")
        self._student_id = student_id

    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, student_id={self._student_id})"

    # Phương thức đối tượng riêng
    def study(self):
        print(f"{self._name} đang học bài...")


p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print("--- Person ---")
print(p1)                # __str__
p1.greet()               # phương thức đối tượng
Person.class_info()      # phương thức lớp
print(Person.is_adult(20))  # static method
print("p1 == p2?", p1 == p2)  # nạp chồng ==


s1 = Student("Charlie", 22, "S12345")
s2 = Student("Diana", 19, "S67890")

print("\n--- Student ---")
print(s1)                # __str__
s1.greet()               # kế thừa greet
s1.study()               # phương thức riêng
Student.class_info()     # phương thức lớp
print(Student.is_adult(17))  # static method
print("s1 == s2?", s1 == s2)


s1.set_name("Charlie Brown")
s1.set_age(23)
s1.set_student_id("S54321")
print("\nSau khi chỉnh sửa:", s1)
