from django.core.mail import send_mail


def sendEmailConfirmation(adoption):
    topic = "Adoção realizada com sucesso!"
    content = f"Parabens por adotar {adoption.pet.name} pelo valor de {adoption.value} reais mensais."
    sender = "savepets16@gmail.com"
    receiver = [adoption.email]
    send_mail(topic, content, sender, receiver)
