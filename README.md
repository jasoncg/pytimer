# pytimer
A simple timer for Python supporting the with statement.  Once the when block exits the total time elasped is displayed.

# Usage
Enclose any code to be timed in a with statement:
	
	import time
	with time.Timer() as t:
		perform_calculation()
		t.print_elapsed("Time for perform_calculation()")
		perform_calculation_two()
		t.print_elapsed("Time for perform_calculation_two()")
    

Upon execution the output will be similar to the following:

	Time for perform_calculation() 4.42677 seconds
	Time for perform_calculation_two() 0.82540 seconds
	Took 5.25220 seconds
