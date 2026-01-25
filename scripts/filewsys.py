import os


def run_file_system():
    while True:
        print("w or r or s? (or 'e' to exit)")
    
        ch = input(">> ")
    
        if ch == "s":
            if not os.path.exists("texts"):
                os.makedirs("texts")
            _d_ = os.listdir("texts")
    
            for file in _d_:
                print(file)
    
        elif ch == "w":
            if not os.path.exists("texts"):
                os.makedirs("texts")
    
            x = input("Enter a name for the file: ")
            print("\n")
    
            fp = f"texts/{x}"
    
            if os.path.exists(fp):
                with open(fp, "a") as file:
                    while True:
                        cont = input("Enter text >>")
                        if cont == "Exit":
                            print("\n")
                            print("DONE!")
                            print("\n")
                            break
                        file.write(cont + "\n")

            else:
                with open(fp, "x") as file:
                    while True:
                        cont = input("Enter text >>")
                        if cont == "Exit":
                            print("\n")
                            print("DONE!")
    
                            print("\n")
                            break
                        file.write(cont + "\n")
    
        elif ch == "r":
            print("Current files: ")
            print("\n")
            if not os.path.exists("texts"):
                print("No files created yet.\n")
                continue

            _d_ = os.listdir("texts")
    
            for file in _d_:
                print(file)
            print("\n")
            ch__ = input("Enter the file name you want: ")
    
            pf = f"texts/{ch__}"
    
            try:
                with open(pf, "r") as file:
                    cont = file.read()
    
                    print("\n")
                    print(cont)
                    print("\n")
            except FileNotFoundError:
                print("The file doesn't exist!")
        
        elif ch == "e":
            print("Exiting file system...")
            break

if __name__ == "__main__":
    run_file_system()




