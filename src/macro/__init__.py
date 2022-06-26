from fredapi import Fred
import os
fred = Fred(api_key=os.getenv('FRED_API_KEY'))
