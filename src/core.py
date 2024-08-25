import requests
import os
from dotenv import load_dotenv
import re
import whois

load_dotenv()

def mobile_number_lookup(number):
    """Lookup mobile number using NumVerify API."""
    api_key = os.getenv('NUMVERIFY_API_KEY')
    url = "http://apilayer.net/api/validate"
    params = {
        'access_key': api_key,
        'number': number,
        'format': '1'
    }
    response = requests.get(url, params=params)
    return response.json()

def extract_email_ids(text):
    """Extract email addresses from the given text."""
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

def extract_website_details(domain):
    """Extract details about a domain using whois."""
    domain_info = whois.whois(domain)
    return domain_info
