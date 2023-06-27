from locust import HttpUser, task

class BookInfoUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/productpage")