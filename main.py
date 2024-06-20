import sys

if __name__ == "__main__":
	if len(sys.argv)>1:
		upath = sys.argv[1]
		f = open(upath)
		print(f.read())
