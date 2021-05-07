import email.message
import smtplib

msg = email.message.EmailMessage()
msg["From"] = "henry940129@gmail.com"
msg["To"] = "janeyu0427@gmail.com"
msg["Subject"] = "前端作業_個人履歷網頁"
msg.set_content("https://weixiang0815.github.io/Henry%20Wang's%20Portfolio/index.html")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("henry940129@gmail.com", "880815henry")
server.send_message(msg)
server.close()
