from django.contrib.auth.mixins import UserPassesTestMixin


class StaffRequiredMixin(UserPassesTestMixin):
    # Functia test_func(self) va fi apelata automat
    # Ea trebuie sa returneze True/False in functie de o conditie
    # pe care vrem noi sa o verificam
    def test_func(self):
        # self.request.GET.get('nume param', '') pentru parametrii din url
        return self.request.user.is_staff