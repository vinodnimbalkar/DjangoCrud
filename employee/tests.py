from django.test import TestCase

# Create your tests here.
from employee.models import Employee


class EmployeeTestCase(TestCase):
    '''This is Employee Test Case'''
    def setUp(self):
        Employee.objects.create(
            eid="1", ename="Vinod", eemail="abc@gmail.com", econtact="0123456789"
        )
        Employee.objects.create(
            eid="2", ename="Vinay", eemail="xyz@gmail.com", econtact="9876543210"
        )

    def test_employee(self):
        """Employee detail correctly identified"""
        vinod = Employee.objects.get(eid="1")
        vinay = Employee.objects.get(eid="2")
