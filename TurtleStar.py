
def TurtleStar(cute, sidelength,npoint): ## draws a star using polygon
    anglePoly = 360/npoint
    anglePoly2 = 2*anglePoly
    anglePolyTip = 180-anglePoly2
    cute.left(anglePolyTip)
    cute.forward(sidelength)
    for i in range(npoint-1):
        cute.left(anglePoly2)
        cute.forward(sidelength)
    cute.penup()
    cute.forward(60)
    cute.pendown()
    cute.left(170)

def TurtleStar(cute, sidelength,npoint): ## draws a coloured star using polygon
    cute.fillcolor("yellow")
    cute.begin_fill()
    anglePoly = 360/npoint
    anglePoly2 = 2*anglePoly
    anglePolyTip = 180-anglePoly2
    cute.left(anglePolyTip)
    cute.forward(sidelength)
    for i in range(npoint-1):
        cute.left(anglePoly2)
        cute.forward(sidelength)
    cute.end_fill()
    cute.penup()
    cute.forward(60)
    cute.pendown()
    cute.left(170)
    
