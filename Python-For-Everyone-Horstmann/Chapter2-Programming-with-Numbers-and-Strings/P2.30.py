from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)
canvas = win.canvas()


canvas.setOutline("blue")
canvas.drawOval(50, 50, 50, 50)
canvas.setOutline("black")
canvas.drawOval(101, 50, 50, 50)
canvas.setOutline("red")
canvas.drawOval(152, 50, 50, 50)
canvas.setOutline("yellow")
canvas.drawOval(75, 75, 50, 50)
canvas.setOutline("green")
canvas.drawOval(125, 75, 50, 50)








win.wait()
