class Bug:

	def __init__(self, width, length):
		self.width = width
		self.length = length

	def __repr__(self):
		return f"<Bug Width = {self.width} Length = {self.length}>"

def main():
    print(Bug(1,3))

if __name__ == '__main__':
    main()