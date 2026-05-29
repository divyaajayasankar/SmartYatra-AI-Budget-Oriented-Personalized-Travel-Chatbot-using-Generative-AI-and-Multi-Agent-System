import os
import sys

# Create the models directory
models_dir = r"d:\travel_chatbot_project\backend\models"
os.makedirs(models_dir, exist_ok=True)
print(f"Created directory: {models_dir}")

# Verify it exists
if os.path.isdir(models_dir):
    print(f"✓ Directory exists: {models_dir}")
else:
    print(f"✗ Failed to create directory")
    sys.exit(1)
