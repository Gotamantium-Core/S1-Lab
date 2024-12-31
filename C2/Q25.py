'''
A program that accepts the lengths of three sides of a triangle as inputs. The program
should output whether or not the triangle is a right triangle using Pythagorean Theorem.
Implement using functions
'''

def rightTriangle() -> bool:
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    hypo = int(input("Enter hypotenuse: "))

    if (hypo * hypo == base * base + height * height):
        return True;
    else:
        return False;

if rightTriangle():
    print("Right triangle")
else: print("Not right triangle")