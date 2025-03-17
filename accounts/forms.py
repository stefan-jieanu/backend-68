from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import Textarea, CharField

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Fieldul password va fi inclus automat
        fields = ['username', 'first_name']


    biography = CharField(label='Tell us about you: ', widget=Textarea, min_length=10)

    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)

        biography_data = self.cleaned_data['biography']
        profile = Profile(user=result, biography=biography_data)

        if commit:
            profile.save()

        return result