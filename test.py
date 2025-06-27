import sys, os

# Add src folder to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from thefirstock import thefirstock


# login = thefirstock.firstock_login(
#     userId='ABCD',
#     password='ABCD@',
#     TOTP='2001',
#     vendorCode='ABCD_API',
#     apiKey='ABCD',
# )

# print(login)

userDetails = thefirstock.firstock_userDetails("ABCD")

print(userDetails)