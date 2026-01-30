from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    """Load testing user for the application"""

    # Wait 1–3 seconds between tasks
    wait_time = between(1, 3)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_health(self):
        self.client.get("/health")
