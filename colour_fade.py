'''
Created with | Python 3.8.2
@Authur      | Isaak Choi
'''

# produce ordered colour-points via an RGB gradient generated from given colour-points
def colGradPt(selectedPoint, colourPoints=[(255,0,0), (255,0,255), (0,0,255), (0,255,255), (0,255,0), (255,255,0)], length=500): 
    '''Creates a gradient from 'colourPoints', fading evenly along the 'length'. 
    Inputting the 'selectedPoint' will return that point along the gradient.'''
    __author__ = "Isaak Choi"
    __license__ = "MIT"

    sectionLen = int(length / len(colourPoints))
    i = int(selectedPoint/sectionLen) 
    fadeFrom = colourPoints[i%len(colourPoints)]
    fadeTo = colourPoints[(i+1)%len(colourPoints)]
    differenceStep1 = (fadeTo[0]-fadeFrom[0])/sectionLen
    differenceStep2 = (fadeTo[1]-fadeFrom[1])/sectionLen
    differenceStep3 = (fadeTo[2]-fadeFrom[2])/sectionLen
    n = selectedPoint % sectionLen
    return (int(fadeFrom[0] + differenceStep1 * n), int(fadeFrom[1] + differenceStep2 * n), int(fadeFrom[2] + differenceStep3 * n)) 