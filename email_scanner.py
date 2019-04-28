import imaplib
import email
import os
import login_info


con = imaplib.IMAP4_SSL(login_info.imap_url)
con.login(login_info.user, login_info.password)
con.select('INBOX')

type, data = con.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = con.fetch(num, '(RFC822)')
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(login_info.path + 'haiku_generator/media/', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                print('Downloaded "{file}".'.format(file=fileName))

con.close()
