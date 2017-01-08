def get_area(pi, radius):
    return pi * (radius ** 2)

def get_triangle_area(height, base_width):
	    return 0.5 * height * base_width

def get_area(pi, radius):

    print("in function")
    print("pi=%0.4f, radius=%d"%(pi,radius))
    return pi * (radius **2)

pi = 3.14
radius = 3
area = get_area(pi, radius)
print(area)

new_pi = 3.1416
new_radius = 5
new_area = get_area(new_pi, new_radius)
print(new_area)

height = 5
base_width = 5
area = get_triangle_area(height, base_width)
print(area)

pi = 3.14
radius = 3
area = get_area(3.1416,5)
print("after function")
print("radius=%d"%(radius))
