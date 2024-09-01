# Defining the function
def simple_intrest(p, n, r):
    """
    This function takes following inputs
    p = Principal in INR
    n = Number of years
    r = Rate of Intrest in %p.a.
    Output = Intrest and amount
    """
    I = (p * n * r) / 100
    A = p + I
    return I, A


# Take input from the user
p = float(input("Please enter principal in INR : "))
n = float(input("Please enter number of years : "))
r = float(input("Please enter rate of intrest in %p.a : "))

# Call the function
I, A = simple_intrest(p, n, r)

# Print the results
print(f"Simple Intrest : {I:.2f} INR")
print(f"Amount : {A:.2f} INR")
