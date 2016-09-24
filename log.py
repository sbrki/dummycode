import time

def log(message, file="log.txt"):
	"""A barebones function that logs messages."""
	line="[{} >>> {}]\n\t{}\n\n".format(time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"),message)
	file=open(file, "a")
	file.write(line)
	file.close()
