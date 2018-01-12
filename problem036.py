# Copyright 2018 Keval Khara kevalk@bu.edu

def is_db_palindrome(n):
	s = str(n)
	if s != s[ : : -1]:
		return False
	t = bin(n)[2 : ]       # Since bin(10) = 0b1010, we leave out the first 2 characters
	if t != t[ : : -1]:
		return False
	return True

ans = sum(i for i in range(1000000) if is_db_palindrome(i))
print(ans)
