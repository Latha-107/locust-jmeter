from locust import HttpUser, task, between, events
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WebsiteUser(HttpUser):
    """
    Simulated user for load testing the application
    """
    # Set the target host - can be overridden with --host flag
    # Example: locust --host=http://your-app-url:3000
    host = "http://localhost:3000"
    
    # Wait time between tasks (1-3 seconds)
    wait_time = between(1, 3)
    
    def on_start(self):
        """Called when a simulated user starts"""
        logger.info("Starting new user session")
    
    @task(3)  # Weight: 3x more likely than other tasks
    def load_home(self):
        """Load the home page"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task(2)  # Weight: 2x more likely than health check
    def load_testing_endpoint(self):
        """Load the testing-load endpoint"""
        with self.client.get("/testing-load", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task(1)  # Weight: baseline
    def health_check(self):
        """Check the health endpoint"""
        with self.client.get("/health", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Health check failed with status {response.status_code}")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Called when test starts"""
    logger.info("Load test starting...")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Called when test stops"""
    logger.info("Load test completed")
