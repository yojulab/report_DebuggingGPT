# selenium python 코드 작성
# - Datas/self_instructs_output.json 파일 pandas로 읽기
# - https: // huggingface.co/spaces/tloen/alpaca-lora 사이트를 열기
# - 화면 열기 완료까지 대기
# - chromedriver 위치는 ../../chromedriver
# - instruction과 input을 연결해 '#component-0 .scroll-hide.svelte-drgfj5'에 넣기
# -  '#component-17'을 클릭 후 '#component-7 .scroll-hide'에 결과 기다렸다 결과 확인
# -  '#component-0 .scroll-hide.svelte-drgfj5'와 '#component-7 .scroll-hide' 결과 내용을 각각 Datas/result.json 저장

import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Datas/self_instructs_output.json 파일 pandas로 읽기
data = pd.read_json('Datas/self_instructs_output.json')

# WebDriver 초기화
driver = webdriver.Chrome('../../chromedriver')

try:
    # https://huggingface.co/spaces/tloen/alpaca-lora 사이트를 열기
    driver.get('https://huggingface.co/spaces/tloen/alpaca-lora')

    # 화면 열기 완료까지 대기
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#component-0 .scroll-hide.svelte-drgfj5')))

    for index, row in data.iterrows():
        instruction = row['instruction']
        input_data = row['input']
        resource = instruction + ' ' + input_data
        # '#component-0 .scroll-hide.svelte-drgfj5'에 input 데이터 입력
        element = driver.find_element(
            By.CSS_SELECTOR, '#component-0 .scroll-hide.svelte-drgfj5')
        element.send_keys(resource)

        # '#component-17'을 클릭 후 '#component-7 .scroll-hide'에 결과 기다렸다 결과 확인
        driver.find_element(By.CSS_SELECTOR, '#component-17').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#component-7 .scroll-hide')))

        # '#component-7 .scroll-hide' 결과를 Datas/result.json에 저장
        result = driver.find_element(
            By.CSS_SELECTOR, '#component-7 .scroll-hide').text
        with open('Datas/result.json', 'a') as f:
            json.dump({'resource': resource, 'result': result}, f)
            f.write('\n')

finally:
    # WebDriver 종료
    driver.quit()
