from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fullname = data.get('fullname', '')
        email = data.get('email', '')
        subject = data.get('subject', '')
        message = data.get('message', '')
        print(data)

        # Assuming you have set up email settings in your Django settings.py
        to_email = settings.EMAIL_HOST_USER
        from_email = email
        messages =f'Name: {fullname}\nEmail: {email}\nMessage: {message}'
        send_mail(subject, messages, from_email, [to_email])
        return JsonResponse({'message': 'Email sent successfully.'})
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)
