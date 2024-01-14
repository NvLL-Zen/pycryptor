import sys
print("")
NEnc = {"a":"n1", "g":"n2", "m":"n3", "s":"n4", "y":"n5",
         "b":"l1", "h":"l2", "n":"l3", "t":"l4",
         "f":"c1", "l":"c2", "r":"c3", "x":"c4",
         "c":"d1", "i":"d2", "o":"d3",
         "k":"f1", "q":"f2", "w":"f3",
         "d":"e1", "e":"e2", "j":"e3",
         "p":"g1", "u":"g2", "v":"g3", "z":"g4",
         " ":"g5","/":"g6",",":"g7",".":"g8","\\":"g9", "!":"g10"
         }

# NEnc_decrypt = {
#         "n1":"a", "n2":"g", "n":"m", "n4":"s", "n5":"y",
#         "l1":"b", "l2":"h", "l3":"n", "l4":"t",
#         "c1":"f", "c2":"l", "c3":"r", "c4":"x",
#         "d1":"c", "d2":"i", "d3":"o",
#         "f1":"k", "f2":"q", "f3":"w",
#         "e1":"d", "e":"e2", "j":"e3",
#         "p":"g1", "u":"g2", "v":"g3", "z":"g4",
#         " ":"g5","/":"g6",",":"g7",".":"g8","\\":"g9", "!":"g10"
# }

MorseEnc = {
    "a":".-", "g":"--.", "m":"--", "s":"...", "y":"-.--",
    "b":"-...", "h":"....", "n":"-.", "t":"-",
    "f":"..-.", "l":".-..", "r":".-.", "x":"-..-",
    "c":"-.-.", "i":"..", "o":"---",
    "k":"-.-", "q":"--.-", "w":".--",
    "d":"-..", "e":".", "j":".---",
    "p":".--.", "u":"..-", "v":"...-", "z":"--..",
    "1":".----", "2":"..---", "3":"...--", "4":"....-", "5": ".....",
    "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0": "-----",
    " ":"/","/":"/",",":",",".":".","\\":"\\", "!":"!"
}

def uppercase(case):
    return case.upper()

args = sys.argv

if len(args) < 2:
    print("[X] No message provided")
    print("[?] pass in '-h' 'help'")
    exit()

help_str = """PyCryptor - A dummy project for encrypting text to
other form such as morse and n (A dummy encryption made by me)

[?]: pycryptor.py -m/--message "<message to encrypt>" -f/--format "<format> (default: n)"
"""

def flags():
    flag_status = [False, False, False]
    format_list = ["n", "morse"]
    mode_list = ["dec", "enc"]

    for i in range(len(args)):
        # Handle help flag
        if args[i] == "-h" or args[i] == "--help":
            print(help_str)
            sys.exit()
        # Handle message flag
        elif args[i] == "-m" or args[i] == "--message":
            try:
                if args[i+1][0] == "-":
                    if args[i+1] == "-h" or args[i+1] == "--help":
                        print("[?] -m/--message <Message to encrypt>")
                        print("")
                        sys.exit()
                    else:
                        print("[X] Invalid argument provided")
                elif args[i+1][0] == " " or args[i+1] == "":
                    print("[X] Invalid mwssage argument provided")
                    sys.exit()
                else:
                    message = args[i+1]
                    flag_status[0] = True
            except:
                sys.exit()
        # Handle mode flag
        elif args[i] == "-t" or args[i] == "--type":
            try:
                if args[i+1][0] == "-":
                    if args[i+1] == "-h" or args[i+1] == "--help":
                        print("[?] -t/--type <dec>(decrypt) / <enc>(encrypt)")
                        print("")
                        sys.exit()
                    else:
                        print("[X] Invalid argument provided")
                elif args[i+1][0] == " " or args[i+1] == "":
                    print("[X] Invalid argument provided")
                    sys.exit()
                elif args[i+1] in mode_list:
                    mode = args[i+1]
                    flag_status[2] = True
                else:
                    print("Invalid argument provided")
            except:
                sys.exit()
        # Handle format flag
        elif args[i] == "-f" or args[i] == "--format":
            try:
                if args[i+1][0] == "-":
                    if args[i+1] == "-h" or args[i+1] == "--help":
                        print("[?] -f/--format <Format to encrypt>")
                        print("n     = N-Cryption")
                        print("morse = Morse Code")
                        print("")
                        sys.exit()
                    else:
                        print("[X] Invalid argument provided")
                elif args[i+1][0] == " " or args[i+1] == "":
                    print("[X] Invalid argument provided")
                    sys.exit()
                else:
                    if args[i+1] in format_list:
                        format = args[i+1]
                        flag_status[1] = True
                    else:
                        print("[X] Invalid format")
                        sys.exit()
            except:
                sys.exit()

    if flag_status[1] == False:
        format = "n"
    if flag_status[2] == False:
        print("[X] No type provided")
        exit()
    if flag_status[0] == False:
        print("[X] No message to decrypt")
        exit()
    return message, format, mode

flags_arg = flags()

# Initial process

def main():
    after_str = ""
    if flags_arg[2] == "enc":
        if flags_arg[1] == "n":
            for char in flags_arg[0]:
                if char.isupper() == True:
                    after_str += uppercase(NEnc[f'{char.lower()}'])
                elif char.isdigit() == True:
                    after_str += char
                else:
                     try:
                         after_str += NEnc[f'{char}']
                     except:
                         after_str += "uc"
        elif flags_arg[1] == "morse":
            for char in flags_arg[0]:
                if char.isupper() == True:
                    after_str += MorseEnc[f'{char.lower()}']
                    after_str += " "
                else:
                    try:
                        after_str += MorseEnc[f'{char}']
                    except:
                        after_str += "uc"
        print(f'message: "{after_str}"\n ')
    elif flags_arg[2] == "dec":
        print("Decrypted")
    
    
    

if __name__ == "__main__":
    main()