from random import randint

from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):
    @task(1)
    def vote_random(self):
        response = self.client.get("/polls/1/", name="Open first poll form")
        csrftoken = response.cookies["csrftoken"]
        self.client.post(
            "/polls/1/vote/",
            {"choice": str(randint(1, 4))},
            headers={"X-CSRFToken": csrftoken},
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)
