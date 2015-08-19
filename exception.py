#!env python
try:
	try:
		fh = open("not_exists_file", "r")
	except IOError, e:
		print "Error: can\'t find file or read data"
		print e
	finally:
		print "finally block"
	raise BaseException('1232')
except BaseException, e:
	print "Error raised!"
	print e

