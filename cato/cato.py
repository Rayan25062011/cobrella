import os
import sys

if sys.argv:
   os.system(f"flake8 {sys.argv} --statistics")
