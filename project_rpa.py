# use TagUI 
from logging import log
import os 
from dotenv import load_dotenv
import rpa as r

load_dotenv()
biz_url = os.getenv('BIZ_URL')
asp_url = os.getenv('ASP_URL')
notify_msg = []

# ******시작******
def init():
    # visual_automation = False, chrome_browser = True, headless_mode = False, turbo_mode = False
    # visual_automation : use keyboard automation 
    r.init(visual_automation= True,turbo_mode = True)
def wait():
    r.wait(30)
    return True
def close():
    r.close()

class Bizmailer:
    def start():
        r.url('https://'+ biz_url + '/bizsmart/manager/main.do')
        r.wait()
        #login
        r.type('userId', os.getenv('BIZ_USER'))
        r.type('userPw',os.getenv('BIZ_PASS'))
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
        r.wait(1)
        r.click('bt_s_typeB w66 mg_r4')
        # 프리뷰 내용
        r.type('prevMessege','프리뷰')
        # 이메일 내용
        r.click('contents')
        r.type('contents', '테스트페이지 내용 작성 완료!')
        # r.snap('page', 'content.png')
        r.wait(3)
        # 첨부파일 추가
        r.hover('input.ipt_fileA')
        r.upload('input.ipt_fileA','content.png')
        r.dom('window.confirm = function alert(message) {return true;}')
        r.wait(2)
        #발송하기
        r.click('next')
        r.wait(2)
        r.popup('https://' + biz_url + '/bizsmart/manager/campaign/mail.do?method=createMailConfirm&type=&check=create')
        r.click('bt_s_typeC w150')
        r.wait(2)
        r.keyboard('[enter]')
        r.keyboard('[enter]')
        r.popup()
        return True


    # ******메일 발송결과******
    def notify_mail():
        global notify_mail
        r.hover('txt_purp first')
        r.click('//*[@id="table_bi"]/div/div[2]/ul/li[1]/ul/li[1]/a')
        r.click('//*[@id="aqBlue"]/tbody/tr[2]/td[2]/a')
        send_good= r.read('blueBL').split(' ')
        send_fail = r.read('//*[@id="info"]/tbody/tr[2]/td[5]/span/text()').split(' ')
        send_sub = r.read('subject')
        if send_good[1] != '(100.0%)':
            r.click('TABClass4')
            fail_text = r.read('/html/body/div[5]/div/table[9]/tbody/tr[2]/td/table/tbody').replace('\n', '')

            notify_mail = '***** \"'+send_fail[0]+'\"건발송 오류***** \n' + fail_text

        else: 
            notify_mail = '\"'+send_sub+'\"' + send_good[0]+' 건 테스트 성공'

        return True

    def send_message(title, content):
        r.hover('txt_purp first')
        r.click('//*[@id="table_bi"]/div/div[2]/ul/li[3]/ul/li[1]/a')
        r.click('sendTitle')
        r.type('sendTitle', title)
        r.type('sendContents', content)
        # 첨부파일 등록
        r.dom('fileAttach(this, true);')
        r.upload('input.intext','content2.jpg')
        r.click('btnBlueSmall')
        r.wait()
        # 첨부파일 삭제
        r.dom('window.confirm = function alert(message) {return true;}')
        r.dom('fileAttach(this, false);')

        # 보낼 연락처
        r.wait(2)
        r.type('rcvPerson1', os.getenv('FAIL_PHONE_1'))
        r.type('rcvPerson2', os.getenv('TEST_PHONE_1'))
        r.type('rcvPerson3', os.getenv('TEST_PHONE_2'))
        r.type('rcvPerson4', os.getenv('FAIL_PHONE_2'))

        r.click('btnSend')
        r.wait(2)
        r.keyboard('[enter]')
        r.keyboard('[enter]')
        r.keyboard('[enter]')
        r.wait()
        return True

    def notify_message():
        global notify_msg
        list = []

        r.hover('txt_purp first')
        r.click('//*[@id="table_bi"]/div/div[2]/ul/li[1]/ul/li[3]/a')
        r.click('//*[@id="aqBlue"]/tbody/tr[2]/td[3]/a')

        total = r.read('/html/body/div[5]/div/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]')
        table = '/html/body/div[5]/div/table[3]/tbody/tr[6]/td/table/tbody/'
        success = r.read('blueBL').split(' ')
        fail= r.read('redBL').split(' ')

        list.append('총 발신 통수 = '+ total + '건, 성공 = ' + success[0] + '건, 실패 = '+ fail[0] +'입니다.')

        if success[1] != '(100%)':
            list.append('문자발송 상세분석 결과')
            for i in range(1,6):
                for j in range(1,6):
                    result = r.read(table+'tr['+str(i)+']/th['+str(j)+']')
                    count = r.read(table+'tr['+str(i)+']/td['+str(j)+']')
                    if count != '-':
                        list.append('- '+ result + '  "' + count + '" 건 ')

        notify_msg = '\n'.join(list)


    def address():
        r.hover('txt_purp first')
        r.click('//*[@id="table_bi"]/div/div[2]/ul/li[4]/ul/li[1]/a')
        r.click('btnGreen')
        r.select('//*[@name="groupKey"]','1639524862489F8wA3lM' )
        r.upload('input.intext','address.csv')
        r.click('btnBlueSmall')
        r.click('isHeader')
        r.dom('window.confirm = function alert(message) {return true;}')
        r.frame('fileFrame')
        r.select('//*[@id="aqBlue"]/tbody/tr[1]/th[1]/select','customName')
        r.select('//*[@id="aqBlue"]/tbody/tr[1]/th[2]/select','customEmail')
        r.select('//*[@id="aqBlue"]/tbody/tr[1]/th[3]/select','customSms')
        r.frame()
        r.dom('window.confirm = function alert(message) {return true;}')
        r.click('btnGreen')
        r.dom('window.confirm = function alert(message) {return true;}')
        # r.click('btnBlue')
        return True

    def notify():
        r.telegram(os.getenv('TELEGRAM'), '1.문자발송테스트결과 \n' +  notify_mail + '\n\n' + '2.메일발송테스트결과 \n'+ notify_msg )

        # print('1.문자발송테스트결과 \n' +  notify_mail + '\n\n' + '2.메일발송테스트결과 \n'+ notify_msg)


    # # ******OCR로 메일전송결과 확인******
    # def send_result():
    #     raw1 = r.read('//*[@id="aqBlue"]/tbody/tr[1]').replace('\n', '\t')
    #     raw2 = r.read('//*[@id="aqBlue"]/tbody/tr[2]').replace('\n', '')
    #     raw = raw1 + '\n' + raw2
    #     return raw

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

class javaASP:
    def start():
        r.url('http://'+ asp_url)
        r.wait()
        # login
        r.type('userId', os.getenv('ASP_USER'))
        r.type('userPwd',os.getenv('ASP_PASS'))  
        r.click('funfunBtnLogin')
        return True

    def sms():
        r.hover('//*[@id="lnb"]/div/ul/li[1]')
        r.click('ico_sms')


    


