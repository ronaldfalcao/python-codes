from .AddOperation import AddOperation
from faker import Faker


fake = Faker()


def test_soma():
	add_operation = AddOperation()
	number_1 = fake.random_number()
	number_2 = fake.random_number()
	result = add_operation.soma(number_1, number_2)
	assert result == number_1 + number_2
