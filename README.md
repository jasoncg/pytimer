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
    
