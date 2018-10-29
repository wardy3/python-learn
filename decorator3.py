
class Name(object):
    def __init__(self, first_name, last_name):
        print(f"in Name __init__ {self} {first_name} {last_name}")
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def how_many_names(name_str: str) -> int:
        """How many names this bloke have?
        """
        print(f"counting names in {name_str}")
        return len(name_str.split(' '))


class Student(Name):
    @classmethod
    def from_string(cls, name_str: str):
        print(f"in from_string cls {cls} name {name_str}")
        # first_name, last_name = map(str, name_str.split(' '))
        first_name, last_name = name_str.split(' ')
        print(f"first {first_name} last {last_name}")
        student = cls(first_name, last_name)
        return student


scott = Student.from_string('Scott Robinson')
print(scott)
bill = Student('Bill', 'Posters')
print(bill)

print(Student.how_many_names('Bill'))
print(Student.how_many_names('Bill Posters'))
print(Student.how_many_names('Bill Scott Heron'))
y = Student.how_many_names('l k')
print(f"y {y}")

# name = 'michael wardman'
# first, last = name.split(' ')
# print(f"name {name}\tfirst {first} last {last}")
