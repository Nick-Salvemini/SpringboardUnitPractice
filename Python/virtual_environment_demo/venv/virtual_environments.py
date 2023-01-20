# # While in the directory in the terminal you want the environment contained to
# python3 -m venv venv
# # this creates the virtual environment which you then need to cd into like any directory
# # done once per project

# # then run this line to actually enter the virtual environment
# source venv/bin/activate

# # IF YOU'RE IN THE VENV DIRECTORY ONLY USE "source bin/activate"

# # this must be done every time you want to work in this environment
# # modules installed globally won't be in this environment, you need to install it's own packages, which won't work globally

# faker.Faker()

# from faker import Faker
# fake = Faker()

# print(fake.name())
# print(fake.address())
# print(fake.text())

# to leave virtual environment
# deactivate

from mondrian_art import generate
plt = generate()
plt.show()