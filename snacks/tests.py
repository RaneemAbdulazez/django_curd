from django.urls import reverse
from django.test import TestCase 
from django.contrib.auth import get_user_model
from .models import Snack


class snack_test(TestCase):
    def test_snacks(self):
        # arrange
        # assign
        url=reverse("list_view")
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )



        self.snack = Snack.objects.create(
            title="chips", purchaser="raneem", describtion="describtion",
        )



    def test_string_representation(self):
        self.assertEqual(str(self.snack), "chips")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "chips")
        self.assertEqual(f"{self.snack.purchaser}", "raneem")
        self.assertEqual(self.snack.describtion, "describtion")

    def test_snack_list_view(self):
        response = self.client.get(reverse("list_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "chips")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_list_detail_view(self):
        response = self.client.get(reverse("detail_view", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "raneem")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("create_view"),
            {
                "title": "spagiti",
                "purchaser": "rami",
                "describtion": "it is very beautiful"
            }, follow=True
        )

        self.assertRedirects(response, reverse("detail_view", args="2"))


# purchaser
# describtion
    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update_view", args="1"),
            {"title": "Updated name","purchaser":"samer","describtion":"it's very good"}
        )

        self.assertRedirects(response, reverse("detail_view", args="1"))

    def test_sanck_delete_view(self):
        response = self.client.get(reverse("delete_view", args="1"))
        self.assertEqual(response.status_code, 200)