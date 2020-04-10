from django.test import TestCase
from django.urls import reverse


class ApiViewTest(TestCase):
    default_username = 'default_username'

    def test_index_route(self):
        """
        Index route returns a string
        :return:
        """
        response = self.client.get(reverse('api:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Api index")

    def test_get_chats_for_username(self):
        """
        Chats for given username are returned
        :return:
        """
        expected_response = [
            {"isBotMessage": True, "message": "Hi"},
            {"isBotMessage": False, "message": "hello"}
        ]

        response = self.client.get(
            reverse('api:chats-for-username', args=(self.default_username,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            expected_response
        )

    def test_generate_response_to_message(self):
        """
        Response for given message and username is matched
        :return:
        """
        expected_response = {
            "response": "hello there"
        }
        response = self.client.get(
            reverse('api:response-to-message', args=(self.default_username,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            expected_response
        )
