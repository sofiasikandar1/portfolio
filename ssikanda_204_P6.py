#-------------------------------------------------------------------------------
# Name: Sofia Sikandar                                                                                                                 
# Project 6                                                                
# Lab Section 204                                                                   
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture slides, zybook, mostly MANY office hour sessions that I attended almost everyday                                                                
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or 
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60    70        80
#------------------------------------------------------------------------------

import random #used in scramble method 

class Tile: #class represents an individual tile 
	def __init__(self,value): 
		self.value = value 
	def __str__(self):
		if self.value == None: 
			return("<>") #value for blank tile 
		elif self.value < 10:
			return("%2d" % (self.value)) #adds a space infront of int if it is a single digit 
		else:
			return("%d" % (self.value))
	def __repr__(self): 
		if self.value == None: #if val is None, place None in Tile(value)  
			return ("Tile(None)")
		else:
			return('Tile(%d)' % self.value)	#if it isn't None, then place the value in Tile(value) 
class Direction:
	def __init__(self,value): 
		self.value = value
		if self.value != "UP" and self.value != "DOWN" and self.value != "LEFT" and self.value != "RIGHT":	
			raise TileError("invalid value for Tile") #raises a tileError if value isn't one of the given dirs. 
		else:
			self.value = value #if it is one of the values, store the val
	def __str__(self):
		return self.value #returns the value 
	def __repr__(self):
		return ("Direction('%s')" % (self.value)) #returns the direction in string formatting
	def __eq__(self, other): #checks if self.value is equal to any other value
		return self.value==other.value #returns boolean val 
		
UP = Direction("UP") #global values
DOWN = Direction("DOWN") 
LEFT = Direction("LEFT") 
RIGHT = Direction("RIGHT") 
dirs = [UP,DOWN,LEFT,RIGHT]
 
class TileError(Exception): #defines exception class 
	def __init__(self,msg):
		self.msg = msg 
	def __str__(self):
		return self.msg #returns attribute  
	def __repr__(self):
		return("""TileError('''%s''')""" % (self.msg)) #returns TileError with the message as a string
		
class Puzzle:
	def __init__(self, grid=None, height=4, width=4): #this def creates a 2D list 
		value = 0 #counter function 
		tile = Tile([value]) #calls the Tile class
		t = [] #empty list 
		if grid == None:
			for i in range(height):
				templist = [] #resets the value of temp list after going through loop
				for j in range(width):
					value = value + 1 
					tile = Tile(value) #calls the Tile class 
					if value == 16: #if its the 16th tile, return None as the value 
						tile = Tile(None)
					templist.append(tile) #creates a 1d list		
				t.insert(len(t), templist) #inserts the built list into another, 2d list hence created
			self.grid = t
		else: 
			self.grid = grid #if the grid is not equal to none, just return it 
	def __str__(self):	
		j = '' #empty list to add values onto 
		x = 0  #counter
		for row in self.grid: #runs through lists 
			for col in row: #runs through elements in the list 
				t = col 
				j += str(t) #the # in Tile(#)
				if str(t) != " 4" and str(t) != " 8" and str(t) != "12" and str(t) != "<>": 
					j+= " " 
			x+=1 
			j+='\n'
		return j 
	def __repr__(self):
		x = 0  
		if x in self.grid == "<>":
			x.replace("Tile(None)") #assigns the Tile object value to the empty tile 
		else:
			return (("Puzzle(%s)") % str(self.grid)) 
	def display(self): #prints the value of the tiles in a string 
		print(str(self))
		
	def find_opening(self):	
		for row in range(len(self.grid)): #looks through 2D grid, indexing
			for col in range(len(self.grid[row])):
				if self.grid[row][col].value == None: #if tile is blank, just return the tuple 
					return (row, col) #returns tuple
		raise TileError("no blank spot found") #if not equal to None return Tile error 
		
	def move(self, dir): #move the tile #set this tile = none 
		(row,col) = self.find_opening()
		if dir == DOWN and row != 0: #sets bounds and the direction 
			x = self.grid[row][col] #blank tile 
			j=self.grid[row-1][col] #changed value 
			self.grid[row][col] = j
			self.grid[row-1][col] = x #gives modified 
		elif dir == UP and row !=3:
			x = self.grid[row][col] #blank tile 
			j=self.grid[row+1][col] #changed value 
			self.grid[row][col] = j
			self.grid[row+1][col] = x 
		elif dir == RIGHT and col != 0:
			x = self.grid[row][col] #blank tile 
			j=self.grid[row][col-1] #changed value 
			self.grid[row][col] = j
			self.grid[row][col-1] = x #swaps tiles
		elif dir == LEFT and col != 3:
			x = self.grid[row][col] #blank tile 
			j=self.grid[row][col+1] #changed value 
			self.grid[row][col] = j
			self.grid[row][col+1] = x #swaps tiles 
		else:
			raise TileError("can't move %s" % (dir)) #raises tileError if not a valid direction 	
				
	def is_solved(self): 
		prev = 0 #previous value 
		for i in range(0,3): #uses index method 
			for j in range(0,3):
				if self.grid[i][j].value != None: #if the tile is not blank and if its less than the previous value 
					if self.grid[i][j].value < prev:
						return False
					else:
						prev+=1 #increments the previous value 
		if self.grid[3][3].value != None: #if the 16th tile is not blank return False else return True 
			return False
		return True
								
	def scramble(self, n=1000):
		for i in range(0, n): #range from 0-1000 
			next_direction = random.choice(dirs)
			try: 
				self.move(next_direction) 
			except TileError: #catches the tileError 
				print('')
			
		
		 

			
		
	
	
