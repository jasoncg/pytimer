#
# jasoncg
# 2015-02-23
#
# timer.py
#
# A simple timer supporting the Python "with" statement
#
import time


class Timer():
	"""
	Use in a "with" statement:
	with timer.Timer():
		perform_expensive_calculation()

	May also print the current progress:
	with timer.Timer() as t:
		perform_expensive_calculation_1()
		t.print_progress()
		perform_expensive_calculation_2()
	"""
	def __init__(self, name=None, silent=False):
		self.silent = silent
		if name is not None:
			if not self.silent:
				print("Start %s" % (name))
			name = name+" "
		else:
			name = ""
		self.name = name

	def __enter__(self):
		self.reset()
		return self

	def __exit__(self, type, value, traceback):
		end = time.time()
		if not self.silent:
			print("%sTook %s seconds\n" % (self.name, end-self.start))

	def reset(self):
		# Reset the start to now
		self.start = time.time()
		self.elapsed = time.time()

	def get_progress(self):
		# Get the current time elapsed since start
		return time.time() - self.start

	def print_progress(self, message=None):
		if message is None:
			message = ""
		else:
			message = message+" "
		print("%s%s%s seconds\n" % (self.name, message, self.get_progress()))

	def get_elapsed(self):
		# Get the current time elapsed since start
		newelapsed = time.time()
		e = newelapsed - self.elapsed
		self.elapsed = newelapsed

		return e

	def print_elapsed(self, message=None):
		if message is None:
			message = ""
		else:
			message = message+" "
		print("%s%s%s seconds\n" % (self.name, message, self.get_elapsed()))
