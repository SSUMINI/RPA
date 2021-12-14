import bizmailer as b

b.start()
b.login()
b.mail.send_mail('발송테스트닷')
b.message.send_message()

b.mail.notify()
# b.close()