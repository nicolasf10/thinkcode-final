# This contains the function which turns words into a math result

import re
from math import sqrt, trunc, pi, sin, cos, tan

def math_speech(words):
    try:
        advanced_operations = ['square root', '√']
        if "convert" in words:
            pass
        elif "generate" in words and "prime" in words:
            try:
                prime_found = []
                min_range = int(re.search(r"between (\d*) and (\d*)", words)[1])
                max_range = int(re.search(r"between (\d*) and (\d*)", words)[2])

                if max_range < min_range:
                    return "Please provide a valid range of integers."
                elif max_range - min_range >= 10000:
                    return "I'm sorry, please try a smaller range."
                else:
                    for i in range(min_range, max_range):
                        if i == 1: continue
                        is_prime = True
                        for n in range(2, i):
                            if i % n == 0:
                                is_prime = False
                        if is_prime: prime_found.append(i)

                if len(prime_found) == 0:
                    return f"No prime numbers found between {min_range} and {max_range}"
                else:
                    return f"{len(prime_found)} prime numbers were found, including: {prime_found}"
            except:
                return "Please provide a valid range of integers."
        elif "prime" in words:
            try:
                check_prime = int(re.search("is (.*) a? prime", words)[1])
            except:
                return "Please provide a valid integer."

            for i in range(2, int(check_prime)):
                if check_prime % i == 0:
                    return f"{check_prime} is not a prime number."

            return f"{check_prime} is a prime number."
        else:

            operation = words.replace("plus", '+').replace('minus', '-').replace('divided by', '/').replace(
                'to the power of', '**').replace("raised to the power of", "**").replace("multiplied by", '*').replace("times", "*").replace(
                "what is ", "").replace("math ", "").replace("the", "")
            if "tangent" in words or "cosine" in words or "sine" in words:
                try:
                    x = re.search(r"(tangent|cosine|sine) of (.+)", words)
                    if x[1] == "tangent":
                        pattern = re.compile(r'(tangent) of (.+)')
                        operation = pattern.sub(r'tan(\2)', operation)
                    elif x[1] == "cosine":
                        pattern = re.compile(r'(cosine) of (.+)')
                        operation = pattern.sub(r'cos(\2)', operation)
                    elif x[1] == "sine":
                        pattern = re.compile(r'(sine) of (.+)')
                        operation = pattern.sub(r'sin(\2)', operation)
                except:
                    return "Unfortunately I was unable to perform this mathematical operation."

            for i in advanced_operations:
                if i in operation:
                    if i == 'square root':
                        pattern = re.compile(r'(square root of) (\d+)')
                        operation = pattern.sub(r'sqrt(\2)', operation)
                    elif i == '√':
                        pattern = re.compile(r'(√) (.+)')
                        operation = pattern.sub(r'sqrt(\2)', operation)

            operation.replace(" ", "")
            math_result = eval(operation)

            try:
                decimals = re.search("\.(\d*)", str(math_result))[1]

                if len(decimals) >= 6:
                    math_result = round(math_result, 6)
            except:
                pass

            return f"The result is {math_result}."
    except:
        return "Unfortunately I was unable to perform this mathematical operation."