from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )

    answer = response.choices[0].text.strip()
    return answer

# Create your views here.
def chatbot (request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'response': response})
    return render(request, "chatbot.html")
