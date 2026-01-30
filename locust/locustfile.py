from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    """Load testing user for the application"""
    
    # Target host - will be overridden by --host parameter or Locust web UI
    host = "http://example.com"
    
    # Wait 1-3 seconds between tasks
    wait_time = between(1, 3)
    
    @task
    def load_homepage(self):
        """Load the home page"""
        self.client.get("/")
    
    @task
    def load_health(self):
        """Check health endpoint"""
        self.client.get("/health")
