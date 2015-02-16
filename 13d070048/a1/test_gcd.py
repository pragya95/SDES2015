from gcd import gcd

def test_gcd():
	""" checks test cases for the function gcd"""
	
	assert gcd(1,3) == 1
	assert gcd(5,0) == 5
	assert gcd(32,48) == 16
	# assert gcd(100000000000055555555, 1331) == 1

	try:
		gcd(-40,-20)
	except ValueError:
		print "ValueError thrown"
	
	try:
		gcd(56,"pragya")
	except TypeError:
		print "TypeError thrown"

	try:
		gcd(5,[4,3])
	except TypeError:
		print "TypeError thrown"
	
	try:
		gcd(6,('a','b','c'))
	except TypeError:
		print "TypeError thrown"

if __name__ == '__main__':
	test_gcd()