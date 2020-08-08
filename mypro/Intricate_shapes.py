from turtle import turtle
t = Turtle()
def spiral(n):
	if n < 300:
		t.forward(n)
		t.right(89)
		spiral(n+1)
spiral(30)