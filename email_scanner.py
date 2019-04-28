import imaplib
import email
import os
import login_info
import write
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def check_email(wb):
    con = imaplib.IMAP4_SSL(login_info.imap_url)
    con.login(login_info.user, login_info.password)
    con.select('INBOX')

    types, data = con.search(None, '(UNSEEN)')

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
            file_name = part.get_filename()
            if bool(file_name):
                file_path = os.path.join(login_info.download_path, file_name)
                fp = open(file_path, 'wb')
                fp.write(part.get_payload(decode=True))
                haiku = write.gen_haiku(wb, login_info.rel_download_path + file_name)
                print(haiku + '\n')

                msg = MIMEMultipart()
                msg['Subject'] = 'A Haiku for You!'
                msg['From'] = login_info.user
                recipient = email.utils.parseaddr(email_message['From'])[1]
                msg['To'] = recipient

                txt = MIMEText(haiku)
                msg.attach(txt)

                filepath = file_path
                with open(filepath, 'rb') as f:
                    img = MIMEImage(f.read())

                img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
                msg.attach(img)

                server = smtplib.SMTP_SSL(login_info.smtp_ssl_host, login_info.smtp_ssl_port)
                server.login(login_info.user, login_info.password)
                server.sendmail(login_info.user, recipient, msg.as_string())
                server.quit()

                fp.close()
                os.remove(file_path)

    con.close()


def main():
    wb = write.WordBank()
    while True:
        check_email(wb)
        time.sleep(10)


if __name__ == '__main__':
    main()
