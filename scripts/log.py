import sys, datetime

if __name__ == "__main__":
	log = open("log.txt", "a")
	log.write(str(datetime.datetime.now()) + " " + sys.argv[1] + "\n")