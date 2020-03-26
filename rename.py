# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
def main(): 
	i = 1
	
	directory = str(input("Directory (finish directory path with /): "))
	firstWord = str(input("First Word: "))
	extension = str(input("Extension: "))
	if (directory[-1] != "/"):
		directory += "/"
	
	for filename in os.listdir(directory): 
		dst =firstWord + str(i) + extension
		src = directory+ filename 
		dst = directory+ dst 
		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst)
		i+=1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 

