def gcd(a,b):
	""" Returns the Greatest Common Divisor of the
		two integers passed as arguments"""

	if a < 0 or b < 0:
		raise ValueError('argument cannot be negative')

	if type(a)!= int or type(b)!= int:
	# if type(a) not in [int, long] or type(b) not in [int, long]:
		raise TypeError('enter an integer or long type only')

	if b == 0:
		return a
	return gcd(b, a%b)