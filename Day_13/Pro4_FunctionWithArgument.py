def func(firstname,lastname):
    print(f"This is my {firstname} {lastname}")
func("Alfaiz","Tamboli")


def family(*kids):
    print("This youngest child is "+kids[2])
family("Alfaiz","Alsafa","Namra")


def family(child1,child2,child3):
    print("This youngest child is "+child2)
family(child1="Alfaiz",child2="Alsafa",child3="Namra")



def funct(food):
    for x in food:
        print(x)
fruits=["Apple","banana","cherry"]
funct(fruits)