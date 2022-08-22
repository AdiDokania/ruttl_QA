import imaplib
import email
from email.header import decode_header
import webbrowser
import os

class get_otp:
    @staticmethod
    def otp1():
        otp = []

        username = 'dokaniaadi08@gmail.com'
        password = 'Radhe@321'
        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        imap.login(username, password)

        status, messages = imap.select("Inbox")
        # number of top emails to fetch
        N = 1
        # total number of emails
        messages = int(messages[0])

        for i in range(messages, messages - N, -1):
            # fetch the email message by ID
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                pass

                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            pass
                    if content_type == "text/html":
                        # if it's HTML, create a new HTML file and open it in browser
                        body = body.split('Please verify your email by providing the following code: ')[1]
                        body = body.split('.')[0]
                        otp.append(int(body))
        imap.close()
        imap.logout()
        return otp