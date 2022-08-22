import imaplib
import email
from email.header import decode_header
import webbrowser
import os

username = 'dokaniaadi08@gmail.com'
password = 'Radhe@321'

class getlink():
    def clean(text):
        # clean text for creating a folder
        return "".join(c if c.isalnum() else "_" for c in text)

        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(username,password)
        status, messages = imap.select("INBOX")
        N = 2
        messages = int(messages[0])
        print(messages)

        for i in range(messages, messages-N, -1):
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding)
                    print("Subject:", subject)
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        subject = From.decode(encoding)
                    print("From:", From)
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type =="text/plain" and "attachment" not in content_disposition:
                                pass
                else:
                        # extract content type of email
                    content_type = msg.get_content_type()
                        # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                            # print only text email parts
                        print(body)

        imap.close()
        imap.logout()




