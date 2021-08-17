def double(x):
    return x * 2

def apply_to_one(f):
    return f(3)

my_double = double
x = apply_to_one(my_double)

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

print(full_name(last="Valle"))

print(x)

print(double(2))