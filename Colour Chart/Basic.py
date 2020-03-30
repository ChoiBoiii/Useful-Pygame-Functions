# REQUIRES module 'pygame'
# Created in pygame 3.8

# mousePos    = (posX, posY)    -> py.mouse.get_pos()
# inputColour = (R, G, B)       -> Must be in RGB tuple
# chartPos    = (posX, posY)    -> Top left corner pos
# chartSize   = (width, height) -> size in pixels


def get_colour(mousePos, inputColour, chartPos, chartSize): #-> Returns RGB colour tuple from click position
	#-> takes into account size and position of chart surface on screen
	relClickX = mousePos[0]-chartPos[0]
	relClickY = mousePos[1]-chartPos[1]
	width, height = chartSize
	shader = int((255/height)*relClickY)
	differenceStep1 = (inputColour[0]-shader)/width
	differenceStep2 = (inputColour[1]-shader)/width
	differenceStep3 = (inputColour[2]-shader)/width
	outputColour = (shader +int(differenceStep1*relClickX), shader +int(differenceStep2*relClickX), shader +int(differenceStep3*relClickX))
	return outputColour


def colour_chart(chartSize, inputColour): #-> Returns a surface with the colour chart on it
	#-> Creates a 255x255 gradient chart, then scales it to specified size
	chartSurface = py.Surface((255, 255)) # Create initial surface for chart
	for i in range(255): # Y
		differenceStep1 = (inputColour[0]-i)/255
		differenceStep2 = (inputColour[1]-i)/255
		differenceStep3 = (inputColour[2]-i)/255
		for j in range(255): # X        
			chartSurface.set_at((j, i), 
				(i +int(differenceStep1*j), i +int(differenceStep2*j), i +int(differenceStep3*j)))
    return py.transform.scale(chartSurface, chartSize)




## SLOWER AND LESS USEFUL ##
def colour_chart_per_pixel(chartSize, inputColour): #-> Changes colour on surface pixel by pixel (VERY SLOW)
	#-> Iterates over pixels in a given surface area and chenges their colour
	# Requires a surface to be created outside function then have that surface specified within function
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



























