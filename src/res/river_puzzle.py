
class Puzzle:
	def __init__(self):
		self.objects = []
		self.constraints = {}
	
	def addObject(self, id):
		self.objects.append(id)
		
	def addConstraint(self, eater, eaten):
		self.constraints[eater] = eaten

		
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
	for threat in puzzle.constraints:
		victim = puzzle.constraints[threat]
		if positions[threat] == positions[victim] and not positions['f'] == positions[threat]:
			return False
	return True

def getTargetPositions(puzzle):
	start = {'f': False}
	for object in puzzle.objects:
		start[object] = False
	return start

def getStartPositions(puzzle):
	start = {'f': True}
	for object in puzzle.objects:
		start[object] = True
	return start

def move(object, positions):
	if object == '_':
		positions['f'] = not positions['f']
		return '_'
		
	if positions[object] == positions['f']:
		positions[object] = not positions[object]
		positions['f'] = not positions['f']
		return object
	else:
		return ''
		
def getMovables(puzzle):
	movables = []
	for object in puzzle.objects:
		movables.append(object)
	movables.append('_')
	return movables
	
	
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