"""
Python 3.8

Created on Mon Mar 30 2020

@author: Isaak Choi
"""
#if event.type == py.VIDEORESIZE:
#    # There's some code to add back window content here.
#    surface = py.display.set_mode((event.w, event.h),
#                                      py.RESIZABLE)

X, Y        = (1000, 600)  # Size of window
pos         = (0, 0)       # Pos of chart
SIZE        = (X, Y)       # Size of chart 
inputColour = (255,0,255)  # RGB colour of chart



## FUNCTIONS ##
if True: ## DRAW CHART FUNCTION(S) ##
	#-> Fastest by far
	def colour_chart(chartSize, inputColour): ## Creates 127x127 grid, then scales results to fit specifications 
		chartSurface = py.Surface((127, 127)) # Create a surface for chart
		for i in range(127): # Y
			differenceStep1 = (inputColour[0]-i*2)/255
			differenceStep2 = (inputColour[1]-i*2)/255
			differenceStep3 = (inputColour[2]-i*2)/255
			for j in range(127): # X
				chartSurface.set_at((j, i), 
					(i*2 +int(differenceStep1*j*2), i*2 +int(differenceStep2*j*2), i*2 +int(differenceStep3*j*2)))
		return py.transform.scale(chartSurface, chartSize)

	#-> Slightly slower, not worth it unless super high precision is needed
	def colour_chart_255(chartSize, inputColour): ## Creates 255x255 grid, then scales results to fit specifications 
		chartSurface = py.Surface((255, 255)) # Create a surface for chart
		for i in range(255): # Y
			differenceStep1 = (inputColour[0]-i)/255
			differenceStep2 = (inputColour[1]-i)/255
			differenceStep3 = (inputColour[2]-i)/255
			for j in range(255): # X
				chartSurface.set_at((j, i), 
					(i +int(differenceStep1*j), i +int(differenceStep2*j), i +int(differenceStep3*j)))
		return py.transform.scale(chartSurface, chartSize)

	#-> By far the slowest, not worth it in general,
	def colour_chart_per_pixel(chartSize, inputColour): ## Finds incraments of every pixel, rather than drawing and scaling 255x255 grid
		# Requires a surface to be created outside function, then have that surface specified within function
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




## RUN FUNCTIONS ##
if True: 
	## INITIALISE PYGAME ##
	if True: 
		import pygame as py
		py.init(); py.display.set_caption('Color Chart')
		clock = py.time.Clock()
		SCREEN = py.display.set_mode((X, Y), py.NOFRAME | py.RESIZABLE)

	## USE OF FUNCTIONS ##
	if True:
		chartSizeRatio = (X/SIZE[0], Y/SIZE[1])
		font = py.font.Font(None, int(X*0.05))
		mousePos = (int(-X*0.1), int(-Y*0.1))
		frameNum = 1
		totalTime = 0
		with open('frame_times (ms).txt', 'a') as file:
			file.write('\nFrame Num | Time (ms) -----------------------------------------------------\n')
		with open('retrieved_colours (ms).txt', 'a') as file:
			file.write('\nColour (R, G, B) | Click Pos | Frame Num ----------------------------------------------\n')
		chartSurface = colour_chart(SIZE, inputColour) # Create colour gradient
		while True:
			keys = py.key.get_pressed()
			if keys[py.K_ESCAPE]:
				with open('frame_times (ms).txt', 'a') as file:
					file.write(f'========== Average Frame Time: {totalTime/frameNum} (ms)\n')
				py.quit()
			for event in py.event.get():
				if event.type == py.QUIT:
					with open('frame_times (ms).txt', 'a') as file:
						file.write(f'========== Average Frame Time: {totalTime/frameNum} (ms)\n')
					py.quit()
				if event.type == py.VIDEORESIZE:
					X = event.w
					Y = event.h
					SCREEN = py.display.set_mode((X, Y),
						py.NOFRAME | py.RESIZABLE)
					SIZE = (int(X/chartSizeRatio[0]), int(Y/chartSizeRatio[1]))
					font = py.font.Font(None, int(X*0.05))
					SCREEN.fill((0,0,0))
					#print(f'Window Size: {(X, Y)}px')
					#print(f'Chart Size: {SIZE}px\n')
			SCREEN.blit(chartSurface, (pos))
			if py.mouse.get_pressed()[0]: # Replace with input to determine when to return colour
				mousePos = py.mouse.get_pos()
				if pos[0] < mousePos[0] < pos[0]+SIZE[0]:
					if pos[1] < mousePos[1] < pos[1]+SIZE[1]:
						outputColour = get_colour(mousePos, inputColour, pos, SIZE)

						with open('retrieved_colours (ms).txt', 'a') as file:
							file.write(f'{outputColour} | {mousePos} | {frameNum}\n')
							
			clock.tick()
			frameTime = clock.get_time()
			text = font.render(f"FPS: {int(1000/frameTime)}", True, (255,255,255), (0,0,0))
			SCREEN.blit(text, (0,0))
			with open('frame_times (ms).txt', 'a') as file:
				file.write(f'{frameNum}| {frameTime}\n')
				totalTime += frameTime
			py.draw.circle(SCREEN, (0,0,0), (mousePos[0], mousePos[1]), int(X*0.005), int(X*0.002))
			py.display.update()
			frameNum += 1






















