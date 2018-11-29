import os
import sys

scannedFiles = []
dotunderscore = []

os.system("clear")
folder = input("Drag/Drop the folder to clean\n> ")
if folder[-1:] == " ":
	folder = folder[:-1]
os.chdir(folder)

if __name__ == "__main__":
	# Scan the files in the current work directory.
	for path, subdirs, files in os.walk("."):
		for name in files:
			filePath = os.path.join(os.getcwd(), path, name)
			scannedFiles.append(filePath)

for file in scannedFiles:
	copy = file
	try:
		while True:
			slash = copy.index("/")
			copy = copy[(slash+1):]
	except:
		file = file[len(os.getcwd()) + 1:]

		if copy[:2] == '._':
			dotunderscore.append(file)
			os.remove(file)

if len(dotunderscore) == 0:
	print("You didn't have any '._' files!")
else:
	print("Your '._' files have been removed!")
	print(dotunderscore)

if input("Press Enter to quit") == "":
	os.system("killall Terminal")