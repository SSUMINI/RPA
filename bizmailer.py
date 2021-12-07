# use TagUI 
import os 
from dotenv import load_dotenv
import rpa as r

load_dotenv()
url = os.getenv('BIZ_URL')

# visual_automation = False, chrome_browser = True, headless_mode = False, turbo_mode = False
# visual_automation : use keyboard automation 
r.init(visual_automation = True, turbo_mode = True)

r.url('https://'+ url + '/bizsmart/manager/main.do')
r.wait(3)

# element_identifier = None, text_to_type = None, test_coordinate = None
# login
r.type('userId', os.getenv('BIZ_USER'))
r.type('userPw',os.getenv('BIZ_PASS'))

#login button
r.click('bt_login mg_r6')

# func1. 메일발송
r.hover('txt_purp first')
r.click('//*[@href="/bizsmart/manager/campaign/mail.do?method=makeMail"]')
#메일 제목
r.type('sendTitle', '수민테스트')
# 받는 사람 추가
r.type('addr_name', os.getenv('TEST_NAME'))
r.type('addr_email', os.getenv('TEST_EMAIL'))
r.click('bt_s_typeB w66 mg_r4')

#프리뷰 내용
r.type('prevMessege','프리뷰')
r.wait(2)
# 이메일 내용
r.click('contents')
r.type('contents', '테스트페이지 하나 둘')
# 수신동의 문구
r.type('mailConfirm','동의하니?')
r.click('mailConfirmChk_Label')
# 수신 미동의 문구
r.type('mailDeny','mail deny')
r.click('mailDenyChk_Label')

#발송하기
r.click('next')
r.popup('https://' + url + '/bizsmart/manager/campaign/mail.do?method=createMailConfirm&type=&check=createa')

#테스트 결과 OCR
a = r.read('//*[@id="aqBlue"]/tbody/tr[1]').replace('\n', '')
b = r.read('//*[@id="aqBlue"]/tbody/tr[2]').replace('\n', '')
print(a)
print(b)
# a = r.read('//*[@class="basic_datagrid report_table"]/tbody/tr[1]').replace('\n', '')
# print(a)
# r.telegram('5084632752', a)

# r.click('bt_s_typeC w150')
# r.keyboard('[enter]')

# # func2.자동메일발송
# r.hover('txt_purp first')
# r.click('//*[@href="/bizsmart/manager/campaign/auto.do"]')
# # func3. A/B 메일 발송
# r.hover('txt_purp first')
# r.click('//*[@href="/bizsmart/manager/campaign/ab.do"]')
# # func4. 이메일 템플릿
# r.hover('txt_purp first')
# r.click('//*[@href="/bizsmart/manager/campaign/mailTemplate.do"]')
# # func5. 첨부파일관리 
# r.hover('txt_purp first')
# r.click('//*[@href="/bizsmart/manager/campaign/attach.do"]')


