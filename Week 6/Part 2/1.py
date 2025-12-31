'''
Creating Function types() that prints a given value both as a float and an integer.
This function do type conversion
'''

def types(val):
    integer_val = int(val)
    print("Value in integer: ", integer_val)

    float_val = float(val)
    print("Value in Float: ", float_val)

types("123")


