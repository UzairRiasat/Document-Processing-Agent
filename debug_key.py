import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('OPENAI_API_KEY')
print(f'Key exists: {key is not None}')
if key:
    print(f'Key length: {len(key)}')
    print(f'First 10 chars: {repr(key[:10])}')
    print(f'Last 10 chars: {repr(key[-10:])}')
    print(f'Full key (safely): {key[:20]}...')
else:
    print('No API key found in environment')
