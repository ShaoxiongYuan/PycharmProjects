d = float(input("Distance："))
t = float(input("Time："))
v0 = float(input("Initial Speed："))
a = (d - v0 * t / 2) / t ** 2
print("Acceleration is " + str(a) + "m/(s^2).")
