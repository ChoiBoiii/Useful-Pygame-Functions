if True: ## INITIALISE PYGAME ##
	import pygame as py
	py.init(); py.display.set_caption('Square')
	clock = py.time.Clock()
	if False:
		while True:
			try:
				tempVar = int(input('Enter screen width (px): '))
				try:
					if tempVar >= 50:
						break
					elif tempVar < 50:
						print('  Error: Invalid input v\u0332a\u0332l\u0332u\u0332e\u0332;')
						print('    Input must be a positive intager above 50 \n')
				except NameError:
					pass
			except ValueError:
				print('  Error: Invalid input t\u0332y\u0332p\u0332e\u0332;')
				print('    Input must be a positive intager above 50 \n')
	tempVar = 1000
	X, Y = tempVar, int(tempVar *0.6)
	SCREEN = py.display.set_mode((X, Y), py.NOFRAME)
	print('Initialising Colour Chart...')

if True: ## GET COLOUR FUNCTION ##
	def get_colour(mousePos, inputColour, chartPos, chartSize):
		relClickX = mousePos[0]-chartPos[0]
		relClickY = mousePos[1]-chartPos[1]

		width, height = chartSize
		fadeFrom = int((255/height)*relClickY)
		differenceStep1 = (inputColour[0]-fadeFrom)/width
		differenceStep2 = (inputColour[1]-fadeFrom)/width
		differenceStep3 = (inputColour[2]-fadeFrom)/width
		outputColour = (fadeFrom + int(differenceStep1 *relClickX), fadeFrom + int(differenceStep2 *relClickX), fadeFrom + int(differenceStep3 *relClickX))
		return outputColour

if True: ## DRAW CHART FUNCTION(S) ##
	def colour_chart(chartSize, inputColour): ## Creates 255x255 grid, then scales results to fit specifications
		chartSurface = py.Surface((255, 255)) # Create a surface for chart
		for i in range(255): # Y
			differenceStep1 = (inputColour[0]-i)/255
			differenceStep2 = (inputColour[1]-i)/255
			differenceStep3 = (inputColour[2]-i)/255
			for j in range(255): # X
				chartSurface.set_at((j, i), # SPECIFY THE CHART SURFACE!!!
					(i +int(differenceStep1*j), i +int(differenceStep2*j), i +int(differenceStep3*j)))
		return py.transform.scale(chartSurface, chartSize)

	def colour_chart_per_pixel(chartSize, inputColour): ## Finds incraments of every pixel, rather than drawing and scaling 255x255 grid
		# Requires a surface to be created outside function, 
		# 	then have that surface specified within function
		width, height = chartSize
		shadeStep = 255/height
		for i in range(height):
			fadeFrom = int(shadeStep *i)
			differenceStep1 = (inputColour[0]-fadeFrom)/width
			differenceStep2 = (inputColour[1]-fadeFrom)/width
			differenceStep3 = (inputColour[2]-fadeFrom)/width
			for j in range(width):
				chartSurface.set_at((j, i), # SPECIFY THE CHART SURFACE!!!
					(fadeFrom + int(differenceStep1 *j), fadeFrom + int(differenceStep2 *j), fadeFrom + int(differenceStep3 *j)))




if True: #Create chart and return time taken
	clock.tick()
	## COLOUR CHART ##
	pos    = (0, 0)           # Change pos of top left
	SIZE   = (X, Y)           # Change size of window 
	inputColour = (0,50,255)  # Change RGB colour for chart
	chartSurface = colour_chart(SIZE, inputColour) # Create colour gradient
	chartSurface.convert()
	py.display.update(SCREEN.blit(chartSurface, (pos))) # Add chart to screen
	##################
	clock.tick();print(f'Time taken: {clock.get_time()}ms')

if True: #Detect clicks and return colours
	mousePos = (int(-X*0.1), int(-Y*0.1))
	while True:
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
		SCREEN.blit(chartSurface, (pos))
		py.draw.circle(SCREEN, (0,0,0), (mousePos[0], mousePos[1]), int(X*0.005), int(X*0.002))
		py.display.update() #only update part that needs to be updated?
		if py.mouse.get_pressed()[0]: # Replace with input to determine when to return colour
	## ## GET COLOUR ## ##
			mousePos = py.mouse.get_pos()
			if pos[0] < mousePos[0] < pos[0]+SIZE[0]:
				if pos[1] < mousePos[1] < pos[1]+SIZE[1]:
					outputColour = get_colour(mousePos, inputColour, pos, SIZE)
	######################
					print(f'Click Pos:       {mousePos}')
					print(f'Returned Colour: {outputColour}\n')






















