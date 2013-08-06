
class Puzzle:
	def __init__(self):
		self.objects = []
		self.constraints = {}
	
	def addObject(self, id):
		self.objects.append(id)
		
	def addConstraint(self, eater, eaten):
		self.constraints[eater] = eaten

farmer = '!'
		
def solve(puzzle):
	positions = getStartPositions(puzzle)
	
	moves = ''
	while (True):
		for object in getMovables(puzzle):
			nextMove = move(object, positions)
			if (isValid(puzzle, positions)):
				moves += nextMove
			else:
				move(object, positions)
			
			if positions == getTargetPositions(puzzle):
				return moves
				
def isValid(puzzle, positions):
	p = positions
	for threat in puzzle.constraints:
		victim = puzzle.constraints[threat]
		if p[threat] == p[victim] and not p[farmer] == p[threat]:
			return False
	return True

def move(object, positions):
	p = positions
	if object == '_':
		p[farmer] = not p[farmer]
		return '_'
		
	if p[object] == p[farmer]:
		p[object] = not p[object]
		p[farmer] = not p[farmer]
		return object
	else:
		return ''

def getTargetPositions(puzzle):
	return dict([(object, False) for object in [farmer] + puzzle.objects])

def getStartPositions(puzzle):
	return dict([(object, True) for object in [farmer] + puzzle.objects])
		
def getMovables(puzzle):
	return puzzle.objects + ['_']
	
	
if __name__ == '__main__':
	puzzle = Puzzle()
	puzzle.addObject('a')
	assert solve(puzzle) == 'a'

	puzzle = Puzzle()
	puzzle.addObject('x')
	puzzle.addObject('y')
	assert solve(puzzle) == 'x_y'

	puzzle = Puzzle()
	puzzle.addObject('c')
	puzzle.addObject('w')
	puzzle.addObject('g')
	puzzle.addConstraint('w', 'g')
	assert solve(puzzle) == 'w_cwg_w'

	puzzle = Puzzle()
	puzzle.addObject('c')
	puzzle.addObject('w')
	puzzle.addObject('g')
	puzzle.addConstraint('w', 'g')
	puzzle.addConstraint('g', 'c')
	assert solve(puzzle) == 'g_cgw_g'

	print 'OK'