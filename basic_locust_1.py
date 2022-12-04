from locust import FastHttpUser,task

url = 'https://api.demoblaze.com/login'

payload = {
    "username": "horacioss1",
    "password": "1234567890"
    }

class DemoBlazeTest(FastHttpUser):

    @task(1)
    def homePage(self):
        self.client.get("/",name="HomePage")

    @task(1)
    def selectProduct(self):
        self.client.get("/prod.html?idp_=1",name="Listing")

    @task(2)
    def login(self):
        self.client.post(url, name="login",json=payload)
