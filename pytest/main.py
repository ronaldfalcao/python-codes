from src.Calculator import Calculator
from src.operations.AddOperation import AddOperation
from src.operations.SubOperation import SubOperation
from src.operations.MultOperation import MultOperation
from src.operations.DivisionOperation import DivisionOperation

if __name__ == '__main__':

	calc = Calculator(AddOperation(), SubOperation(), MultOperation(), DivisionOperation())

	operation_one = calc.add(10, 3, True)
	operation_two = calc.sub(20, 3, False)
	operation_three = calc.mult(2, 3, True)
	operation_four = calc.div(4, 2, True)

	print(operation_one)
	print(operation_two)
	print(operation_three)
	print(operation_four)
