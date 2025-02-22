# instadiff
Python script to quickly check who isn't following you back on Instagram.

## How to Use
1. Use Instagram to request to download your information: https://accountscenter.instagram.com/info_and_permissions/dyi
    - Select `Download or transfer information`
    - Select `Some of your information`
    - Only select `Followers and following` then `Next`
    - Choose `Download to device` then `Next`
    - Now create the files to download
        - Set `Date range` to `All time`
        - Set `Notify` to your email
        - Set `Format` to `JSON`
        - `Media quality` doesn't matter
    - Now wait ~10 minutes for Instagram to send you your files
2. Download Python: https://www.python.org/downloads/ (newer versions should work but I used Python 3.10.6)
3. Put the ZIP folder vended by Instagram into this project's `in` folder
4. Run the following in Command Line:
```
python insta.py
```
5. Now you know how to restore balance.
