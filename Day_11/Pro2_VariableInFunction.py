# x = "Hello"
#
# def func():
#     x = "Hii"
#     print(x, "Alfaiz")
# func()
# print(x, "Alfaiz")

x="hii"
def func2():
    global x
    x="Hello"
func2()
print(x,"Alfaiz")