# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger, user_test

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(['-vv'])

# Provide possibility of user input
user_test()
