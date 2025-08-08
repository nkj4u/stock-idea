from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

NOTE_USER_URL = "https://note.com/butamarukabu"


def fetch_note_posts_selenium():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(NOTE_USER_URL)
    time.sleep(3)  # JS描画待ち
    articles = []
    found = set()
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        if href and "/butamarukabu/n/" in href and href not in found:
            found.add(href)
            articles.append(href)
        if len(articles) == 2:
            break
    print("[DEBUG] articles (first 2):")
    for i, url in enumerate(articles):
        print(f"  {i}: {url}")
    print(f"Found {len(articles)} articles.")
    if len(articles) < 2:
        print("記事が2件未満です。")
        driver.quit()
        return
    # 2番目の記事のみ取得
    url = articles[1]
    driver.get(url)
    time.sleep(1.5)
    title = None
    try:
        title_elem = driver.find_element(By.TAG_NAME, "h1")
        title = title_elem.text.strip()
    except Exception:
        pass
    if not title:
        try:
            title_elem = driver.find_element(By.CSS_SELECTOR, '[class*="title"]')
            title = title_elem.text.strip()
        except Exception:
            pass
    if not title:
        try:
            title = driver.title.strip()
        except Exception:
            title = url
    # 記事本文の取得
    try:
        body_elem = driver.find_element(By.CSS_SELECTOR, 'div.c-article__body, article')
        body = body_elem.text.strip()
    except Exception:
        body = "本文の取得に失敗しました。"
    # 本文要約（100文字程度）
    summary = body[:100] + ("..." if len(body) > 100 else "")
    print(f"\n--- 最新2番目の記事（全文） ---\n{title}\n{url}\n\n{body}\n")
    driver.quit()


if __name__ == "__main__":
    fetch_note_posts_selenium()
