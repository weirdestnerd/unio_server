from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('Api index')


def get_user_chats(request, username):
    response = [
      {
        "isBotMessage": True,
        "message": "Hi"
      },
      {
        "isBotMessage": False,
        "message": "hello"
      }
    ]
    return JsonResponse(response, safe=False)


def generate_response_to_message(request, username):
    response = {
      "response": "hello there"
    }
    return JsonResponse(response)
