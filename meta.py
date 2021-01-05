import ast
import sys


def convert_str(before, after):
	with open(before, "r") as before_file:
		src = before_file.read()
	root = ast.parse(source = src,)
	print(ast.unparse(root))

def main():
	try:
		convert_str(sys.argv[1], sys.argv[2])
	except:
		convert_str("target.py", "target_after.py")

if __name__ == '__main__':
	main()