import bge 
from math import *
cont = bge.logic.getCurrentController()
sc = bge.logic.getCurrentScene()
obj = sc.objects
pt = obj['referencial']
class Plotter():
    def plotar(self):
        formula = 'x*(x-1)*(x+2)*(x**2)'
        for z in range(-1000, 1000):
            x = z/25
            try:
                if isinstance(eval(formula), float):
                    pt.localPosition.x  = x
                    pt.localPosition.z  = eval(formula)
                    if z % 2 == 0:
                        destino = sc.addObject('destino', pt)
                    else:        
                        origem = sc.addObject('origem', pt)
                        if 'destino' in locals():
                            pose = (origem.localPosition + destino.localPosition)/2
                            pt.localPosition = pose
                            meio = sc.addObject('meio', pt)
                            direction = destino.localPosition - origem.localPosition
                            AXIS_X = 0
                            meio.localScale = [direction.length*2,0.1, 0.1]
                            meio.alignAxisToVect(direction, AXIS_X)     
            except:
                 print("provavelmente um erro de domínio...")
def plotador():
    p = Plotter()
    p.plotar()