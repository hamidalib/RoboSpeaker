import os
if __name__ == '__main__':
    print("Hello! Welcome to Robo Speaker. Created by Hamid")
    while True:
        x = input("Enter what you want me to say: ")
        if x == "q":
            os.system("Say 'program is ending'")
            break
        command = f"Say {x}"
        os.system(command)

print("Program has ended...")