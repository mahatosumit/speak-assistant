import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Sumit")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "-":
            os.system("Say bye bye friend")
            break
        command = f"say {x}"
        os.system(command)
