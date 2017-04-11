# Konwerter liczb binarnych i dziesiętnych. Należy podać liczbę i po spacji podać system w/w liczby (2 czy 10).

class bcolors:                    # kolory
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + "Converter BINARY to DECIMAL numbers and vice versa" + bcolors.ENDC)
while True:
    try:
        ask = input("Give a number and - after space - system (2 or 10). Or x to exit: ").upper()
        numbers = ask.split()

        if ask == "X":              # Możliwość wyjścia z programu
            print("Good bye:)")
            break

        if numbers[1] == "2":         # Konwertowanie z systemu 2 na 10
            num_binary = numbers[0]
            power = len(num_binary)
            result1 = 0
            for digit in num_binary:
                result1 += int(digit) * (2 ** (power - 1))
                power -= 1

                draw = "---"            # wyświetlacz
                for i in str(result1):
                    draw += "-"
            print(bcolors.OKGREEN + """
            / """, draw, """\ 
            """, result1,"""| 10""",""" 
            \ """, draw, """/ 
            """ + bcolors.ENDC)

        elif numbers[1] == "10":         # Konwertowanie z systemu 10 na 2
            num_decimal = numbers[0]
            result2 = []
            while int(num_decimal) != 0:
                rest = int(num_decimal) % 2
                result2.append(str(rest))
                num_decimal = int(num_decimal) / 2

            revers = result2[::-1]  
            last_result = ''.join(revers)

            draw = "---"                    # wyświetlacz
            for i in str(last_result):
                draw += "-"
            print(bcolors.OKBLUE + """
            / """, draw, """\ 
            """, last_result,"""| 2""",""" 
            \ """, draw, """/ 
            """ + bcolors.ENDC)

        else:                               # Błąd jeśli druga liczba (system) inna niż 2 lub 10
            print("\n Incorrect system! (2 or 10) \n")

    except IndexError:                      # Błąd jeśli nie wprowadzono cyfry
        print("\n Incorrect!! Try again: number to convert, space and system (2 or 10!) \n")