num_3 = "3.14"
def isfloat (str_val):
    try:
            float(str_val)
            return True
            except ValueError:
            return False
print("Is Pi a Float :" isfloat(num_3))
