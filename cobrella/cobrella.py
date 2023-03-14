import os
import sys

if sys.argv:
   print(green + "[" + bold + " SCANNING... \033[0m" + green + " ]")

   os.system(f"flake8 {sys.argv} --statistics")
