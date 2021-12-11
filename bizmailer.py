# use TagUI 
import os 
from dotenv import load_dotenv
import rpa as r

load_dotenv()
url = os.getenv('BIZ_URL')

# ******시작******
def start():
    # visual_automation = False, chrome_browser = True, headless_mode = False, turbo_mode = False
    # visual_automation : use keyboard automation 
    r.init(visual_automation = True, turbo_mode = True)
    r.url('https://'+ url + '/bizsmart/manager/main.do')
    r.wait(3)

# ******로그인******
def login():
    r.type('userId', os.getenv('BIZ_USER'))
    r.type('userPw',os.getenv('BIZ_PASS'))
    #login button
    r.click('bt_login mg_r6')
    return True

# ******메일 발송******
def send_mail(title):
    r.hover('txt_purp first')
    r.click('//*[@href="/bizsmart/manager/campaign/mail.do?method=makeMail"]')
    #메일 제목
    r.type('sendTitle', title)
    # 받는 사람 추가
    r.type('addr_name', os.getenv('TEST_NAME'))
    r.type('addr_email', os.getenv('TEST_EMAIL'))
    r.click('bt_s_typeB w66 mg_r4')
    # 프리뷰 내용
    r.type('prevMessege','프리뷰')
    r.wait(2)
    # 이메일 내용
    r.click('contents')
    r.type('contents', '테스트페이지 하나 둘')
    r.snap('page', 'content2.png')
    # 첨부파일 추가
    r.upload('input.ipt_fileA','content2.png')
    r.dom('window.confirm = function alert(message) {return true;}')
    # 수신동의 문구
    r.type('mailConfirm','동의하니?')
    r.click('mailConfirmChk_Label')
    # 수신 미동의 문구
    r.type('mailDeny','mail deny')
    r.click('mailDenyChk_Label')
    #발송하기
    r.click('next')
    r.popup('https://' + url + '/bizsmart/manager/campaign/mail.do?method=createMailConfirm&type=&check=createa')
    
    return True

# ******메일 발송결과******
def mail_result():
    #OCR 사용 결과 인지
    r.hover('txt_purp first')
    r.click('//*[@id="table_bi"]/div/div[2]/ul/li[1]/ul/li[1]')
    raw1 = r.read('//*[@id="aqBlue"]/tbody/tr[1]').replace('\n', '\t')
    raw2 = r.read('//*[@id="aqBlue"]/tbody/tr[2]').replace('\n', '')
    raw = raw1 + '\n' + raw2

    return raw

def notify():   
    r.telegram(os.getenv('TELEGRAM'), mail_result())

    return True

# 텔레그램 아이디.
# r.telegram('os.getenv('TELEGRAM'), a)

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


