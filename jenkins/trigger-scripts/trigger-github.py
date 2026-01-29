#!/usr/bin/env python3
"""
Trigger GitHub Actions workflow
"""
import os
import sys
import json
import requests
from requests.exceptions import RequestException

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "Latha-107"
REPO = "testing-load"
WORKFLOW_FILE = "main.yml"
BRANCH = "main"

def main():
    # Validate token
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN environment variable not found")
        sys.exit(1)

    # GitHub API endpoint
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    payload = {
        "ref": BRANCH
    }

    try:
        print(f"Triggering GitHub Actions workflow: {WORKFLOW_FILE}")
        print(f"Repository: {OWNER}/{REPO}")
        print(f"Branch: {BRANCH}")
        
        response = requests.post(url, headers=headers, json=payload)
        
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code == 204:
            print("✓ GitHub Actions workflow triggered successfully!")
            sys.exit(0)
        else:
            print(f"✗ Failed to trigger workflow")
            print(f"Response: {response.text}")
            sys.exit(1)
            
    except RequestException as e:
        print(f"ERROR: Request failed - {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
