import project_rpa as p

print('==== TAGUI 실행====')
p.init()


print('=====================')
print('==== 비즈메일러 실행====')
p.Bizmailer.start()


print('==== 메일발송 테스트 실행====')
p.Bizmailer.send_mail('테스트 메일')


print('==== 문자발송 테스트 실행====')
p.Bizmailer.send_message('테스트 문자','내용은 심플하게')


print('==== 주소록 테스트 실행====')
p.Bizmailer.address()


print('=====================')
print('====javaASP(애드뿌리오) 실행====')
p.wait()

p.javaASP.start()

print('====주소록 테스트 실행====')
p.javaASP.address()

print('====SMS 테스트 실행====')
p.javaASP.sms('문자발송 테스트입니다.')

# print('====MMS 테스트 실행====')
# p.javaASP.mms()

print('====선거문자 테스트 실행====')
p.javaASP.election_sms('내년은 선거입니다.', '투표 많이 해주세요')

print('====광고문자 테스트 실행====')
p.javaASP.ad_sms('이것은 광고문자입니다.')


# print('====팩스 테스트 실행====')
# p.javaASP.fax()

p.wait()
p.Bizmailer.restart()
p.Bizmailer.notify_mail()
p.Bizmailer.notify_message()

print('==== 메일,문자 테스트 결과 발송====')

p.notify.biz()
p.notify.asp()


print('=====테스트 종료======')
p.close()