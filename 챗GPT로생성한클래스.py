class Person:
    def __init__(self, id, phoneNumber):
        # Person 클래스의 생성자입니다. 인스턴스를 초기화하는 메서드입니다.
        self.id = id
        self.phoneNumber = phoneNumber

    def printinfo(self):
        # Person 클래스의 정보를 출력하는 메서드입니다.
        print(f"ID: {self.id}")
        print(f"전화번호: {self.phoneNumber}")


class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        # Manager 클래스의 생성자입니다. Person 클래스의 생성자를 호출하고 skill 변수를 추가로 초기화합니다.
        super().__init__(id, phoneNumber)
        self.skill = skill

    def printinfo(self):
        # Manager 클래스의 정보를 출력하는 메서드입니다. 부모 클래스(Person)의 printinfo 메서드를 호출하여 기본 정보를 출력한 후 skill 정보를 추가로 출력합니다.
        super().printinfo()
        print(f"스킬: {self.skill}")


class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, title):
        # Employee 클래스의 생성자입니다. Manager 클래스의 생성자를 호출하고 title 변수를 추가로 초기화합니다.
        super().__init__(id, phoneNumber, skill)
        self.title = title

    def printinfo(self):
        # Employee 클래스의 정보를 출력하는 메서드입니다. 부모 클래스(Manager)의 printinfo 메서드를 호출하여 기본 정보와 스킬 정보를 출력한 후 title 정보를 추가로 출력합니다.
        super().printinfo()
        print(f"직급: {self.title}")


# 샘플 코드
person = Person("1", "555-123-4567")
person.printinfo()

manager = Manager("2", "555-987-6543", "리더십")
manager.printinfo()

employee = Employee("3", "555-555-5555", "프로그래밍", "소프트웨어 엔지니어")
employee.printinfo()
