# Python program to illustrate the concept
# of threading
import threading
import os

def task1():
	print("Thread-1 starting")
	for i in range(100):
		print(i)
	print("Thread-1 completed")
def task2():
	print("Thread-2 starting")
	for i in range(200,301):
		print(i)
	print("Thread-2 completed")
if __name__ == "__main__":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	# startit1.start()
	t2.start()ng threads
	

	# wait until all threads finish
	t1.join()
	t2.join()
