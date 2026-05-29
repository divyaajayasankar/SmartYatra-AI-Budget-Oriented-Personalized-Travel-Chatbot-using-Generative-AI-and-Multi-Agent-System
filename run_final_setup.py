#!/usr/bin/env python3
# Quick test to import and run the final setup
import sys
import os
sys.path.insert(0, r'd:\travel_chatbot_project')

# Now execute the setup
from final_models_setup import setup
if __name__ == "__main__":
    success = setup()
    exit_code = 0 if success else 1
    print(f"\nExit code: {exit_code}")
