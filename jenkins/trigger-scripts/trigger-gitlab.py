#!/usr/bin/env python3
"""
Trigger GitLab CI/CD pipeline
"""
import os
import sys
import requests
from requests.exceptions import RequestException

# Configuration
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
PROJECT_ID = "12345678"  # Replace with your actual GitLab project ID
BRANCH = "main"
GITLAB_URL = "https://gitlab.com"

def main():
    # Validate token
    if not GITLAB_TOKEN:
        print("ERROR: GITLAB_TOKEN environment variable not found")
        sys.exit(1)

    # GitLab API endpoint
    url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/pipeline"
    
    headers = {
        "PRIVATE-TOKEN": GITLAB_TOKEN,
        "Content-Type": "application/json"
    }
    
    data = {
        "ref": BRANCH
    }

    try:
        print(f"Triggering GitLab pipeline")
        print(f"Project ID: {PROJECT_ID}")
        print(f"Branch: {BRANCH}")
        
        response = requests.post(url, headers=headers, json=data)
        
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print("✓ GitLab pipeline triggered successfully!")
            print(f"Pipeline ID: {result.get('id')}")
            print(f"Pipeline URL: {result.get('web_url')}")
            sys.exit(0)
        else:
            print(f"✗ Failed to trigger pipeline")
            print(f"Response: {response.text}")
            sys.exit(1)
            
    except RequestException as e:
        print(f"ERROR: Request failed - {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
