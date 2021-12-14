import bizmailer as b

b.start()
b.login()
b.send_mail('메일 발송테스트')
b.notify()
# b.close()