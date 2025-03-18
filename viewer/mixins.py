from django.contrib.auth.mixins import UserPassesTestMixin

from viewer.models import Review


class StaffRequiredMixin(UserPassesTestMixin):
    # Functia test_func(self) va fi apelata automat
    # Ea trebuie sa returneze True/False in functie de o conditie
    # pe care vrem noi sa o verificam
    def test_func(self):
        # self.request.GET.get('nume param', '') pentru parametrii din url
        return self.request.user.is_staff


class UserIsReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        # self.kwargs este un dictionar din care putem accesa parametrii din url
        # dupa cum sunt ei definiti intr-un path() din urls.py
        review = Review.objects.get(pk=self.kwargs['pk'])
        if review.user == self.request.user:
            return True

        return False