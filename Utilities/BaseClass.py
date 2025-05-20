import random
import string
import pytest
from spellchecker import SpellChecker
from selenium.webdriver.common.by import By
import pandas as pd


@pytest.mark.usefixtures("setup")
class BaseClass:

    def random_name(length=5):
        first_letter = random.choice(string.ascii_uppercase)
        other_letters = ''.join(random.choices(string.ascii_lowercase, k=length - 1))
        return first_letter + other_letters
    
    def random_phone_number():
        first_digit = random.choice(['6', '7', '8', '9'])  # valid starting digits
        remaining_digits = ''.join(random.choices('0123456789', k=9))
        return first_digit + remaining_digits
    
    
    def check_page_spelling(driver):
        spell = SpellChecker()

        # Add custom words to the dictionary (whitelist)
        custom_words = {'Emversity','ott', 'bsc', 'naac', 'dulapally', 
                        'centre', 'bvoc', 'bengaluru', 'malla', 'mangalam',
                        'incharge', 'hubbali', 'centres', 'dbs', 'mbbs', 'mlt',
                        'zirakpur', 'kukatpally', 'telangana', 'vizag', 'ugc',
                        'faqs', 'yenepoya', 'specialised', 'balanagar', 'immersive',
                        'sterilisation', 'maisammaguda', 'inr', 'rohini', 'indiranagar',
                        'kolkata', 'reddy', 'cvt', 'emt', 'haryana', 'marwadi', 'emversity', 
                        'arka', 'aott', 'patil', 'faq', 'huda', 'sco', 'kkr', 'ajeenkya', 'isbr'}
        spell.word_frequency.load_words(custom_words)
        
        # Get all visible text from the body tag
        page_text = driver.find_element(By.TAG_NAME, "body").text
        
        # Split into words and clean punctuation
        words = [word.strip('.,!?;:()[]{}"\'') for word in page_text.split()]
        
        # Filter out purely numeric and short words (e.g., 'a', 'is')
        words = [word for word in words if word.isalpha() and len(word) > 2]
        
        # Find misspelled words
        misspelled = spell.unknown(words)
        
        print(f"Total words checked: {len(words)}")
        print(f"Misspelled words: {misspelled}")
        return misspelled


    def get_urls_from_gsheet(base_url, csv_url):
        df = pd.read_csv(csv_url)
        paths = df.iloc[:, 0].dropna().tolist()  # assuming path is in first column
        full_urls = [base_url.rstrip("/") + "/" + path.lstrip("/") for path in paths]
        return full_urls
