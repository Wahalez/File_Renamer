import os
import sys


try:
    from colorama import init, AnsiToWin32, Fore, Back, Style
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
except ImportError:
    print("Please install colorama: pip install colorama")
    exit(1)
        
        
def reset_style():
    print(Style.RESET_ALL, file=stream)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(Fore.RED + Style.BRIGHT + "Usage: main.py <folder_path> <new_name> <start_index>", file=stream)
        reset_style()
        exit(1)
    
    folder_path = sys.argv[1]
    new_name    = sys.argv[2]
    start_index = sys.argv[3]
    
    #check if <start_index> is a number
    if not start_index.isdigit():
        print(Fore.RED + Style.BRIGHT + "<start_index> needs to be a number ", file=stream)
        exit(1)
    

    #Asks the user if to proceed with the operation
    print(Fore.YELLOW + Style.BRIGHT + "About to change files :", file=stream)
    print(Fore.CYAN + Style.BRIGHT + Back.BLUE ,file=stream)
    
    for file in os.listdir(folder_path):
        print(Fore.CYAN + Style.BRIGHT + Back.BLUE + '{0:<25} TO {1:>20}'.format(file, new_name + start_index + file[-4:]), file=stream)
    
    reset_style()
    print(Fore.YELLOW + Style.BRIGHT + "\nContinue ?" , file=stream)
    answer = input("Y/N: ")
    reset_style()
    
    #proceed if answered yes
    if answer in ['y','Y','yes','YES']:
        start_index = int(start_index)
        for file in os.listdir(folder_path):
            print(Fore.GREEN + Style.BRIGHT + "Renaming " + file + "...", file=stream) # renamed ...
            try:
                os.renames(os.path.join(folder_path,file), os.path.join(folder_path , new_name + str(start_index) + file[-4:]))
            except FileExistsError:
                print(Fore.RED + Style.BRIGHT + "Couldn't rename file : " + file + " - File already exists", file=stream)
            start_index += 1
        print("\nDONE")
    else:
        print(Fore.RED + Style.BRIGHT + 'exits', file=stream)
        exit(0) #User did not accept to process the files
    
