import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')

import django
django.setup()  # Added parentheses

from testapp.models import Student
from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    d1 = randint(6, 9)  # First digit between 6 and 9
    num = str(d1)  # Start with the first digit
    for i in range(9):  # Generate the remaining 9 digits
        num += str(randint(0, 9))
    return int(num)  # Convert to integer before returning

def populate(n):
    for i in range(n):
        frollno = fake.random_int(min=1, max=999)  # Roll number
        fname = fake.name()  # Student name
        fdob = fake.date_of_birth(minimum_age=18, maximum_age=25)  # Adjust DOB range
        fmarks = fake.random_int(min=1, max=100)  # Marks
        femail = fake.email()  # Email
        fphonenumber = phonenumbergen()  # Phone number
        faddress = fake.address()  # Address
        
        # Insert into the database
        Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phonenumber=fphonenumber,
            address=faddress
        )

if __name__ == '__main__':
    n = int(input("Enter number of records: "))
    populate(n)
    print(f'{n} Records inserted successfully...')
