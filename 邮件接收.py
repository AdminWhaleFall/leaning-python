# 邮件接收
import imaplib
import email
 
def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])
 
conn = imaplib.IMAP4_SSL("imap.163.com", 993)
conn.login("mine@163.com", "******")
conn.select()
typ, data = conn.search(None, 'UNSEEN')
try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                subject=msg['subject']                   
                print(subject)
                payload=msg.get_payload()
                body=extract_body(payload)
                print(body)
        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()