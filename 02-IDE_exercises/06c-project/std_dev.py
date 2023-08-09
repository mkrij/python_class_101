class Person:
    """
    Represents a named person with a specific age in years.
    """
    def __init__(self, name: str, age: int):
        """
        Adds a new person.
        """
        self.name = name
        self.age = age
    def get_age(self):
        """
        Returns the age of a specific person
        """
        return self.age

def std_dev(a_list:list[Person]) -> float:
    new_list = [x.age for x in a_list]
    age_sum_counter = 0
    for x in new_list:
        age_sum_counter += x
    average_age = age_sum_counter / len(new_list)
    new_list = [x - average_age for x in new_list]
    new_list = [x * x for x in new_list]
    person_total = 0
    for x in new_list:
        person_total +=1
    variance_sum = 0
    for x in new_list: 
        variance_sum += x
    variance = variance_sum / person_total
    st_dv = variance ** 0.5
    return st_dv

person1 = Person("Katie", 73)
person2 = Person("Tran", 24)
person3 = Person("Hanna", 48)
person_list = [person1, person2, person3]
print(std_dev(person_list))

