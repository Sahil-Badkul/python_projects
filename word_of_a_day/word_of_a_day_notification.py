import requests
from plyer import notification
import datetime

LOG_FILE = "learned_words_log.txt"

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        if response.status_code == 200:
            return response.json()[0]
    except Exception as e:
        print(f"Error fetching word: {e}")
    return None

def get_word_meaning(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception as e:
        print(f"Error fetching meaning: {e}")
    return "Definition not found."

def show_notification(word, meaning):
    notification.notify(
        title=f"🧠 Word of the Day: {word.capitalize()}",
        message=meaning,
        timeout=10
    )

def log_word(word, meaning):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{timestamp} | {word.capitalize()} - {meaning}\n")

if __name__ == "__main__":
    word = get_random_word()
    if word:
        meaning = get_word_meaning(word)
        show_notification(word, meaning)
        log_word(word, meaning)
    else:
        print("Failed to fetch the word.")
