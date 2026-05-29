#!/usr/bin/env python3
"""Direct setup execution"""
if __name__ == "__main__":
    import os
    
    # Change to backend directory
    os.chdir("d:\\travel_chatbot_project\\backend")
    
    # Create models directory
    os.makedirs("models", exist_ok=True)
    
    # Read and copy models_requests.py to models/requests.py
    with open("models_requests.py", "r") as src:
        content = src.read()
    with open("models/requests.py", "w") as dst:
        dst.write(content)
    
    # Read and copy models___init__.py to models/__init__.py  
    with open("models___init__.py", "r") as src:
        content = src.read()
    with open("models/__init__.py", "w") as dst:
        dst.write(content)
    
    print("✓ Directory created: models")
    print("✓ File created: models/__init__.py")
    print("✓ File created: models/requests.py")
    print("\nSetup completed successfully!")
    
    # Verify files exist
    if os.path.exists("models/__init__.py") and os.path.exists("models/requests.py"):
        print("✓ All files verified")
