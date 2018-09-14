#-------------------------------------------------------------------------------
# Name: Sofia Sikandar                                                         
# G#: G00964476                                                           
# Project 4                                                                   
# Lab Section 204                                                                   
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture slides, zybook, multiple office hour sessions.                                                                 
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or 
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
#methods: s.split(), s.join(), s.pop(), 
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60     70        80
#------------------------------------------------------------------------------
def read_coords(s):
	temparr = s.split("\n") #splits the string
	list = [] #creates empty list
	xcord = 0 #initializes variable
	ycord = 0
	arr = []
	for i in temparr: #runs through vals of temparr
		if i != '': #checks if there is a blank space
			arr.append(i) #if there is not, then 
	correct = len(arr[0]) #length of the row
	for i in range(len(arr)): #runs through the length of the list
		if correct != len(arr[i]): #if its not equal return None
			return None
	for row in arr: 
		ycord = 0
		for col in row:
			if col == 'O':
				list.append(tuple([xcord, ycord])) #returns coord as a tuple
			ycord+=1 
			if col != 'O' and col != '.':
				return None
		xcord+=1 
	return list 

def get_dimensions(s):
	temparr = s.split("\n")
	list = []
	arr = []
	for i in temparr: #runs through indices 
		if i != '': #if not blank space, add that value onto arr
			arr.append(i)
	correct = len(arr[0]) #the length of the row
	for i in range(len(arr)): #runs through length of rows
		if correct != len(arr[i]): #if the len of rows and cols is not equal
			return None 
		for j in arr[i]:
			if j != "O" and j != ".": #removes invalid chars 
				return None 
	numrows = len(arr) #length of rows
	numcols = len(arr[0]) #length of columns 
	return tuple([numrows, numcols]) #returns dimensions of grid in a tuple

def build_empty_grid(height, width):
	temparr = [] 
	arr = []
	for i in range(height): #runs through the rows
		for j in range(width): #runs through the columns
			temparr.append(False) #makes all vals False
		arr.append(temparr) #adds temparr to arr
		temparr = [] 
	return arr 

def build_grid(s):
	dim = get_dimensions(s) #implements get_dimensions func
	grd = build_empty_grid(dim[0], dim[1]) 
	coord = read_coords(s) #implements read_coords func
	for i in range(len(coord)): #runs through the length of the coord
		grd[coord[i][0]][coord[i][1]] = True 
	return grd
			
def show_grid(grid, live='O', dead='.'):
	var = ''
	for lists in grid: #runs through 2D list
		for y in lists:
			if y == True: #if true, add live str to var
				var+=live
			elif y == False: #if false, add dead str to var 
				var+=dead
		var+= "\n" #adds to the end of var
	return var

def count_living(grid):
	int = 0 
	for lists in grid:
		for y in lists:
			if y == True: #if true, add 1 to int to count living
				int+=1
	return int

def any_living(grid):
	bool = False 
	for lists in grid:
		for y in lists:
			if y == True: #returns true if any of the vals in the list are true
				bool = True 
	return bool #returns a single boolean statement
	
def on_grid(grid, r, c):
	if r < 0 or c < 0: #returns false for negative values
		return False 
	if len(grid) > r: #checks if r,c is on the grid
		if len(grid[r]) > c:
			return True #if it is, return True
	return False #if the if statements are false, the func returns false

def count_neighbors(grid, r, c):
	count = 0 
	z = len(grid) #length of the grid
	if (on_grid(grid, r, c) == True): #checks if element exists then execute for loop of possible combos of r and c 
		for x, y in ((r - 1, c), (r + 1, c), (r, c- 1), (r, c+1), (r-1, c-1), (r+1, c+1), (r+1, c-1), (r-1,c+1)):
			if ( 0 <= x < z and 0 <= y < len(grid[0])): 
				if(grid[x][y] == True): #if the cell is alive, add 1 to the count 
					count+=1
	return count
	
def next_gen(grid): 
	string_gr = show_grid(grid, live='O', dead='.')
	var = get_dimensions(string_gr)
	#building grid of the size grid
	newgr = build_empty_grid(var[0], var[1]) 
	#goes through grid
	for lists in range(len(grid)):
		for y in range(len(grid[0])):
			if grid[lists][y] == True:
			#checks if alive neighbors is equal to 2 or 3
				if count_neighbors(grid, lists, y) == 3 or count_neighbors(grid, lists, y) == 2:
					newgr[lists][y] = True
			else:
				if count_neighbors(grid, lists, y) == 3:
					newgr[lists][y] = True
	return newgr

def n_gens(grid, n=20): #returning a list full of n gens, starting with the original val 
	arr =[]
	arr.append(grid)
	for i in range(n - 1): 
		arr.append(next_gen(grid))
		grid = next_gen(grid)
	return arr

def is_still_life(grid, limit=100): #checks if the grid isn't changing with each generation
	var = n_gens(grid, limit)
	for i in range(len(var) - 1):
		if var[i] == var[i+1]:
			return True
	return False

#1 failure and 1 error
def is_cycle(grid, limit=100): #checks if grids are oscillating with each new generation
	list = n_gens(grid, limit)
	for i in range(len(list) - 1):
		for j in range(i+1, len(list)):
			if grid[i] == grid[j]: #checks if grid i is equal to grid j 
				if grid[i] != grid[i+1]:
					return True
	return False

	
	
	
