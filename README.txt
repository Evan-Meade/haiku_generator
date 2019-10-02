Created by Evan Meade (github.com/Evan-Meade, aka. kracken9500) 2019

This project allows one to run a small program which scans an email inbox for new emails with image attachments. If it
finds one, it uses it to seed the pseudorandom function and uses that to procedurally generate a haiku. It then
sends a new email to the original sender containing the haiku and the original image

How to use:
1. Create new file in the project directory: login_info.py
2. Fill in this template for each value:

user = '[email address]'
password = '[pw for email]'
imap_url = '[url for your email's imap server]'

download_path = '/path/to/where/you/want/to/temporarily/save/pics'
rel_download_path = '/download/path/relative/to/project/directory' [may be same as download path]

smtp_ssl_host = '[url to your email's smtp server]'
smtp_ssl_port = 465 [probably]

3. Enjoy!

Obviously, this comes with no warranty, promises, use at own risk, modify but credit original creator, blah blah blah
