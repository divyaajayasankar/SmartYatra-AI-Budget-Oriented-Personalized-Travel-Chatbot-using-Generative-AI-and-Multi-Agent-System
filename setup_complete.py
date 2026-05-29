#!/usr/bin/env python3
import sys
import os

# Set up the path
backend_path = r"d:\travel_chatbot_project\backend"
models_path = os.path.join(backend_path, "models")

# Create the models directory
try:
    os.makedirs(models_path, exist_ok=True)
    print(f"✓ Created directory: {models_path}")
except Exception as e:
    print(f"✗ Error creating directory: {e}")
    sys.exit(1)

# Copy models_requests.py to models/requests.py
try:
    src_file = os.path.join(backend_path, "models_requests.py")
    dst_file = os.path.join(models_path, "requests.py")
    
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created file: {dst_file}")
except Exception as e:
    print(f"✗ Error creating requests.py: {e}")
    sys.exit(1)

# Copy models___init__.py to models/__init__.py
try:
    src_file = os.path.join(backend_path, "models___init__.py")
    dst_file = os.path.join(models_path, "__init__.py")
    
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created file: {dst_file}")
except Exception as e:
    print(f"✗ Error creating __init__.py: {e}")
    sys.exit(1)

# Verify
try:
    if os.path.exists(os.path.join(models_path, "__init__.py")):
        print("\n✓ models/__init__.py verified")
    if os.path.exists(os.path.join(models_path, "requests.py")):
        print("✓ models/requests.py verified")
    print("\n✓ Setup completed successfully!")
except Exception as e:
    print(f"✗ Verification failed: {e}")
    sys.exit(1)
