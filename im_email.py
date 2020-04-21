# import smtplib,ssl
#
# from email.message import EmailMessage
# from email.utils import make_msgid
#
# msg = EmailMessage()
#
# asparagus_cid = make_msgid()
# msg.set_content('This is a text message')
# msg.add_alternative("""\
# <html>
#   <head></head>
#   <body>
#     <p>Hello</p>
#     <p>
# 		Spidy sent you a attachment of IMG using Python code.
#     </p>
# 	<img src="cid:{asparagus_cid}" />
#   </body>
# </html>
# """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
#
# with open("ef.jpg", 'rb') as img:
#     k = msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid=asparagus_cid)
#
# fromEmail = 'kushalbhavsar58@gmail.com'
# toEmail = 'test@gmail.com'
#
# msg['Subject'] = 'Spidy sending one image using Python'
# msg['From'] = fromEmail
# msg['To'] = toEmail
#
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# con = ssl.create_default_context()
# s.ehlo()
# s.login(fromEmail, 'kushal14320')
# s.send_message(msg)
# print('msg sent')
# s.quit()
