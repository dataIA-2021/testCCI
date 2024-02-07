import demo

def test_one():
	assert demo.fibonacci(0) == 0
	assert demo.fibonacci(1) == 1
	assert demo.fibonacci(2) == 1
	assert demo.fibonacci(10) == 55
	#assert demo.fibonacci(10) == 99
	
def test_two():
	assert demo.test1() == None
	
def test_prime():
	assert demo.est_premier(2) == True
	assert demo.est_premier(5) == True
	assert demo.est_premier(7) == True
	assert demo.est_premier(6) == False
	assert demo.est_premier(8) == False
	assert demo.est_premier(100000007) == True
