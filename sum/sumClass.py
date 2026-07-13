#
# sumClass.py
#
class SumClass():
	def __init__(self):
		print("init end")
	
	def sumLoop(self):
		while True:
			addend1 = input("input the addend1 : ")
			if (addend1 == "end"):
				break

			addend2 = input("input the addend2 : ")
			result = self.mySum(addend1, addend2)

			self.showSum(addend1, addend2, result)

	def mySum(self, add1, add2):
		return int(add1) + int(add2)
	
	def showSum(self, add1, add2, result):
		print(str(add1) + " + " + str(add2) + " = " + str(result))