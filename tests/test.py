"""

Test for the simple code generator

@author -> LokotamaTheMastermind
@email -> lokotamathemastermind2@gmail.com
@created -> 3/8/2020
@license -> MIT
@categories -> helpers, handlers, python, pip, code. generators
@supported -> [>=python3]

@tests = [
    parameter
    startup
]

@success = [
    parameter
    startuo
]

"""

if __name__ == "__main__":
    from text_generator import generate
    import time

    code = generate()
    print(f"Generated code -> {code}")
    time.sleep(3)
    print("Done")
