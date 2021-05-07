# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "henry940129@gmail.com"
msg["To"] = "b07302229@ntu.edu.tw"
msg["Subject"] = "哈囉!威翔!"
# 寄送純文字的內容
# msg.set_content("測試看看")
# 寄送比較多樣式的內容 (html)
msg.add_alternative("<h3>測試看看</h3>測試看看", subtype="html")
# 連線到 SMTP Server，驗證寄件人身分並發送郵件
# 到網路上搜尋 gmail smtp server 或是 yahoo smtp server
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("henry940129@gmail.com", "880815henry")
server.send_message(msg)
server.close()
