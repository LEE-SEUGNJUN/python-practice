import turtle
##전역 변수 부분##

num=0
swidth,sheight=1000,300
curX,curY=0,0

##메인 코드 부분##
if __name__ == "__main__":
    turtle.title("거북으로 2진수 표현하기")
    turtle.shape("turtle")
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)
    
    num1=int(input("숫자1를 입력하세요 : "))
    num2=int(input("숫자2를 입력하세요 : "))
    binary= bin(num1)
    binary2= bin(num2)
    
    curX=swidth/2
    curY=0

    for i in range(len(binary1)-2):
        for s in range(len(binary2)-2) :
        turtle.goto(curX,curY)
        if num & 1:
            turtle.color("red")
            turtle.turtlesize(2)
        else:
            turtle.color("blue")
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>=1
        
turtle.done()