from dotenv import load_dotenv
import os

load_dotenv()

print("API_KEY loaded:", bool(os.getenv("API_KEY")))
print("API_SECRET loaded:", bool(os.getenv("API_SECRET")))