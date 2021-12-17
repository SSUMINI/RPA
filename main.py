import project_rpa as p

print('==== TAGUI 실행====')
p.init()
print('***** TAGUI 실행 성공 *****')

print('=====================')
print('==== 비즈메일러 실행====')
p.Bizmailer.start()
print('***** 비즈메일러 로그인 성공 *****')

# print('==== 메일발송 테스트 실행====')
# p.Bizmailer.send_mail('테스트 메일')
# print('***** 메일발송 테스트 성공 *****')

# print('==== 문자발송 테스트 실행====')
# p.Bizmailer.send_message('테스트 문자','내용은 심플하게')
# print('***** 문자발송 테스트 성공 *****')

# print('==== 주소록 테스트 실행====')
# p.Bizmailer.address()
# print('***** 주소록 테스트 성공 *****')

# print('==== 메일,문자 테스트 결과 발송====')
# p.wait()
p.Bizmailer.notify_mail()
p.Bizmailer.notify_message()

# print('=====================')
# print('====javaASP 준비====')
# p.wait()
# print('====javaASP 시작====')
# p.javaASP.start()
# print('***** javaASP 로그인 성공 *****')

p.Bizmailer.notify()

# p.javaASP.sms()

print('=====테스트 종료======')
p.close()