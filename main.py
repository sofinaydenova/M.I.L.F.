# 1 milfTrains
print("Welcome to the M.I.L.F city. We are proud to introduce the new M.I.L.F.train 50+!")

milftrain_mass = 22680
milftrain_acceleration = 10
milftrain_distance = 100
milf_mass = 1
c = 3 * 10 ** 8


def get_force(mass, acceleration):
    return mass * acceleration


milftrain_force = get_force(milftrain_mass, milftrain_acceleration)
print(milftrain_force)
print("The GE train supplies " + str(milftrain_force) + " pussyNewtons of force.")


def get_energy(mass):
    return mass * c ** 2

milf_energy = get_energy(milf_mass)
print("A 1kg M.I.L.F energy supplies " + str(milf_energy) + " pussyJoules.")


# 2 M.I.L.F. work
# !!contains errors!! fix line 28
def get_milfwork(mass, acceleration, distance):
    force = get_force(mass, acceleration) * distance
    return force
    milftrain_work = get_milfwork(milftrain_mass, milftrain_acceleration, milftrain_distance)
    print("The GE train does" + str(milftrain_work) + "pussyJoules of work over" + str(milftrain_distance) + " meters.")


# 3 pussyTemperature

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


f100_in_celsius = f_to_c(100)


def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)