from locust import FastHttpUser,task

url = 'https://api.demoblaze.com/login'

payload = {
    "username": "horacioss1",
    "password": "1234567890"
    }

class DemoBlazeTest(FastHttpUser):

    @task()
    def homePage(self):
        self.client.get("/",name="HomePage")

    @task()
    def selectProduct(self):
        self.client.get("/prod.html?idp_=1",name="Listing")

    @task()
    def login(self):
        self.client.post(url, name="login",json=payload)
