import os
import sys

if sys.argv:
   print(green + "[" + bold + " STARTING... \033[0m" + green + " ]")
   
   os.system("pip install vulture")
   os.system(f"vulture {sys.argv}")
