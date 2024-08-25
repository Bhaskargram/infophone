import os
from dotenv import load_dotenv

load_dotenv()

# NumVerify API Configuration
NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY')

# Google Maps API Configuration
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
