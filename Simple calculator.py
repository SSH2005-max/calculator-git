import math
import cmath


# -----------------------------
# Scientific Calculator
# -----------------------------

def calculator():
    angle_mode = "DEG"

    print("=" * 50)
    print("        SCIENTIFIC CALCULATOR")
    print("=" * 50)
    print("Type 'help' to see commands")
    print("Type 'exit' to quit")

    while True:
        try:
            expression = input(f"\n[{angle_mode}] >>> ").strip()

            if expression.lower() == "exit":
                print("Calculator closed.")
                break

            if expression.lower() == "help":
                show_help()
                continue

            # Change angle mode
            if expression.lower() == "deg":
                angle_mode = "DEG"
                print("Angle mode: Degrees")
                continue

            if expression.lower() == "rad":
                angle_mode = "RAD"
                print("Angle mode: Radians")
                continue

            # Replace common mathematical symbols
            expression = expression.replace("^", "**")
            expression = expression.replace("π", "pi")
            expression = expression.replace("√", "sqrt")

            # Calculate
            result = evaluate(expression, angle_mode)

            print("=", result)

        except Exception as e:
            print("Error:", e)


# -----------------------------
# Mathematical Functions
# -----------------------------

def evaluate(expression, angle_mode):

    # Angle conversion
    def to_radians(x):
        return math.radians(x) if angle_mode == "DEG" else x

    def from_radians(x):
        return math.degrees(x) if angle_mode == "DEG" else x

    # Trigonometry
    def sin(x):
        return math.sin(to_radians(x))

    def cos(x):
        return math.cos(to_radians(x))

    def tan(x):
        return math.tan(to_radians(x))

    # Inverse trigonometry
    def asin(x):
        return from_radians(math.asin(x))

    def acos(x):
        return from_radians(math.acos(x))

    def atan(x):
        return from_radians(math.atan(x))

    # Hyperbolic functions
    def sinh(x):
        return math.sinh(x)

    def cosh(x):
        return math.cosh(x)

    def tanh(x):
        return math.tanh(x)

    # Logarithms
    def log(x):
        return math.log10(x)

    def ln(x):
        return math.log(x)

    # Root
    def root(x, n=2):
        return x ** (1 / n)

    # Factorial
    def fact(x):
        return math.factorial(int(x))

    # Combinations
    def ncr(n, r):
        return math.comb(int(n), int(r))

    # Permutations
    def npr(n, r):
        return math.perm(int(n), int(r))

    # Safe mathematical environment
    allowed = {
        "sin": sin,
        "cos": cos,
        "tan": tan,

        "asin": asin,
        "acos": acos,
        "atan": atan,

        "sinh": sinh,
        "cosh": cosh,
        "tanh": tanh,

        "log": log,
        "ln": ln,

        "sqrt": math.sqrt,
        "root": root,

        "exp": math.exp,
        "abs": abs,

        "fact": fact,
        "ncr": ncr,
        "npr": npr,

        "floor": math.floor,
        "ceil": math.ceil,

        "pi": math.pi,
        "e": math.e,

        "inf": math.inf,

        "pow": pow,

        "complex": complex,

        "real": lambda z: z.real,
        "imag": lambda z: z.imag
    }

    return eval(expression, {"__builtins__": {}}, allowed)


# -----------------------------
# Help Menu
# -----------------------------

def show_help():

    print("""
==================================================
SCIENTIFIC CALCULATOR COMMANDS
==================================================

BASIC
--------------------------------------------------
2 + 5
10 - 3
4 * 6
20 / 4

POWER & ROOT
--------------------------------------------------
2^10
sqrt(25)
root(27,3)

TRIGONOMETRY
--------------------------------------------------
sin(30)
cos(60)
tan(45)

INVERSE TRIGONOMETRY
--------------------------------------------------
asin(0.5)
acos(0.5)
atan(1)

LOGARITHMS
--------------------------------------------------
log(100)
ln(e)

EXPONENTIAL
--------------------------------------------------
exp(2)

FACTORIAL
--------------------------------------------------
fact(5)

COMBINATIONS
--------------------------------------------------
ncr(5,2)

PERMUTATIONS
--------------------------------------------------
npr(5,2)

CONSTANTS
--------------------------------------------------
pi
e

EXAMPLES
--------------------------------------------------
sin(30)^2 + cos(30)^2
sqrt(2)^2
log(1000)
fact(5)
ncr(10,3)
npr(10,3)

ANGLE MODE
--------------------------------------------------
deg     -> Degrees
rad     -> Radians

==================================================
""")


# Start calculator
calculator()