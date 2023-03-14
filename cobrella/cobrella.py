import os
import sys

if sys.argv:
   
   os.system("pip install vulture")
   os.system(f"vulture {sys.argv}")
