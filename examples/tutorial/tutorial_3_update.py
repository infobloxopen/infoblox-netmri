# this script updates user email

import argparse

from infoblox_netmri.client import InfobloxNetMRI

parser = argparse.ArgumentParser(description='update user email')
parser.add_argument('domain', help="user email")
args = parser.parse_args()

defaults = {
    "host": "1.2.3.4",
    "username": "your_username",
    "password": "your_password",
}

client = InfobloxNetMRI(
    defaults.get("host"),
    defaults.get("username"),
    defaults.get("password"),
)

auth_users_broker = client.get_broker('AuthUser')
auth_users = auth_users_broker.index(select=['id', 'user_name'])
for user in auth_users:
    print("Current user email: {}".format(user.email))
    # compute email address based on the user name
    email = "{}@{}".format(user.user_name, args.domain)
    data = auth_users_broker.update(
        id=user.id,
        # set or replace the email address for that user
        email=args.email
    )
    print("Updated email: {}".format(data.email))
