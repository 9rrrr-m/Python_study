# 기본 설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 사용자 에이전트와 페이지 로딩 전략 설정
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  # 페이지 로딩 전략 설정 (normal, eager, none 중 선택)

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# User-Agent 설정
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 드라이버 초기화
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 로그인 페이지로 이동
driver.get('https://nid.naver.com/nidlogin.login')

# 로그인 정보 입력 (사용자 아이디와 비밀번호를 설정하세요)
USER_ID = 'USER_ID'  # 네이버 아이디
USER_PASSWORD = 'USER_PASSWORD'  # 네이버 비밀번호

# 아이디 입력
id_input = driver.find_element(By.ID, 'id')
id_input.click()
id_input.send_keys(USER_ID)

# 비밀번호 입력
password_input = driver.find_element(By.ID, 'pw')
password_input.click()
password_input.send_keys(USER_PASSWORD)

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID, 'log.login')
login_button.click()

# CAPTCHA 수동 입력 대기
input("CAPTCHA를 입력한 후 Enter를 누르세요...")

# 네이버 메일 페이지로 이동
time.sleep(2)  # 페이지 로딩 대기
driver.get('https://mail.naver.com/')

# 최신 메일 페이지로 이동 대기
time.sleep(5)  # 메일 목록 로딩 대기

# 작업 완료 메시지 출력
print("최신 메일 페이지에 도달했습니다.")
