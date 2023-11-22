from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME: str = os.environ.get("ACCOUNT_USERNAME")
PASSWORD: str = os.environ.get("ACCOUNT_PASSWORD")

if USERNAME is None or PASSWORD is None:
    print("Couldn't get username/password! Make a .env file with keys ACCOUNT_USERNAME and ACCOUNT_PASSWORD and store them in there.")
    exit()

print("Attempting login...")
cl: Client = Client()
cl.login(USERNAME, PASSWORD)

print("Collecting followers/following...")
followers = cl.user_followers(cl.user_id)
following = cl.user_following(cl.user_id)

diff = following
for k in followers.keys():
    diff.pop(k, None)

names = []
for user in diff.values():
    names.append(user.username)
print(names)