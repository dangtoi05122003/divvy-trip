from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass
class Setting:
    bucket_name: str

def load_setting():
    load_dotenv()
    bucket_name = os.getenv("BUCKET_NAME")
    return Setting(bucket_name=bucket_name)