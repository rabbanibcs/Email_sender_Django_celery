from time import sleep
from django import forms
# from django.core.mail import send_mail
from .tasks import send_feedback_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    # def send_email(self):
    #     """Sends an email when the feedback form has been submitted."""
    #     sleep(20)  # Simulate expensive operation that freezes Django
    #     send_mail(
    #         "Your Feedback",
    #         f"\t{self.cleaned_data['message']}\n\nThank you!",
    #         "rabbanibcs@gmail.com",
    #         [self.cleaned_data["email"]],
    #         fail_silently=False,
    #     )


    def send_email(self):
        res=send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
        print("ID? ",res.id)
        print("successfull? ",res.successful())
        # print("exception? ",res.get(timeout=2))
