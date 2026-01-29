#!/usr/bin/env python3
"""
Trigger Bitbucket Pipelines
"""
import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

# Configuration
BITBUCKET_USERNAME = os.getenv("BITBUCKET_USERNAME")
BITBUCKET_APP_PASSWORD = os.getenv("BITBUCKET_APP_PASSWORD")
WORKSPACE = "your-workspace"  # Replace with your Bitbucket workspace
REPO_SLUG = "your-repo"       # Replace with your repository slug
BRANCH = "main"

def main():
    # Validate credentials
    if not BITBUCKET_USERNAME or not BITBUCKET_APP_PASSWORD:
        print("ERROR: Bitbucket credentials not found")
        print("Required: BITBUCKET_USERNAME and BITBUCKET_APP_PASSWORD")
        sys.exit(1)

    # Bitbucket API endpoint
    url = f"https://api.bitbucket.org/2.0/repositories/{WORKSPACE}/{REPO_SLUG}/pipelines/"
    
    payload = {
        "target": {
            "type": "pipeline_ref_target",
            "ref_type": "branch",
            "ref_name": BRANCH
        }
    }

    try:
        print(f"Triggering Bitbucket pipeline")
        print(f"Workspace: {WORKSPACE}")
        print(f"Repository: {REPO_SLUG}")
        print(f"Branch: {BRANCH}")
        
        response = requests.post(
            url,
            auth=HTTPBasicAuth(BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD),
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code in [200, 201]:
            result = response.json()
            print("✓ Bitbucket pipeline triggered successfully!")
            print(f"Pipeline UUID: {result.get('uuid')}")
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
