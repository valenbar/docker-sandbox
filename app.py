import os
from dotenv import load_dotenv

load_dotenv()

var = os.getenv('MY_VAR')
var2 = os.getenv('MY_VAR2')
print("MY_VAR: ", var)
print("MY_VAR2: ", var2)
if var2 == None:
    print("MY_VAR2 is None")

# check if there is a directory called "data"
if os.path.isdir("data"):
    print("data is a directory")