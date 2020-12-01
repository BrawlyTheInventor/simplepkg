import os
if input("Do you have Xcode?( 1 for yes, 2 for no)") == "1":
    print("Canceling Xcode install...")
else:
os.system("xcode-select --install")
if input("Do you have Homebrew?(same, 1 & 2") == "1":
    print("Skipping Homebrew install")
else:
    os.system("curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh")
    os.system("/bin/bash install.sh")
