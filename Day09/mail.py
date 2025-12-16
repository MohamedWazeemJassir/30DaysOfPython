import os
import smtplib
from email.mime.text import MIMEText

html = """
<h2 style="color:blue;">Welcome!</h2>
<p>This is an email from Python Group Time is 21 27.</p>
"""

msg = MIMEText(html, "html")
msg["Subject"] = "Test Email From Python Group"
msg["From"] = "contact.syedjafer@gmail.com"
msg["To"] = "contact.syedjafer@gmail.com"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("contact.syedjafer@gmail.com", os.environ.get("APP_PASSWORD"))
server.send_message(msg)
server.quit()