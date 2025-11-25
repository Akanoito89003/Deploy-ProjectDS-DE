import os
from dotenv import load_dotenv

load_dotenv()

print("Checking environment variables...")
vars_to_check = ["DB_USER", "DB_PASS", "DB_HOST", "DB_PORT", "DB_NAME"]

for var in vars_to_check:
    value = os.getenv(var)
    if value is None:
        print(f"❌ {var} is NOT set (None)")
    else:
        # Mask password
        if var == "DB_PASS":
            print(f"✅ {var} is set (length: {len(value)})")
        else:
            print(f"✅ {var} = '{value}'")
