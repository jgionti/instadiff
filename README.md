# instadiff
Python script to quickly check who isn't following you back on Instagram.

## How to Use
1. Download Python: https://www.python.org/downloads/ (newer versions should work but I used Python 3.10.6)
2. Create a file in the directory with the name `.env` with this exact structure:
```
ACCOUNT_USERNAME = "your_username"
ACCOUNT_PASSWORD = "your_password"
```

3. Run the following in Command Line:
```
pip install -r requirements.txt
python insta.py
```
You'll get a login confirmation on your app. Allow it, and you'll eventually see a full list of folks who don't follow you back.
