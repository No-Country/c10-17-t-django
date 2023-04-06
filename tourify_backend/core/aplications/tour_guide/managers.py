from django.db import models

class TourGuideManager(models.Manager):

    def get_all_tour_guide(self):
        return self.all()

    def search_user_guide(self,pk):
        user_guide = self.get(
            id_user=pk
        )

        return user_guide

class CertificationsManager(models.Manager):

    def get_all_certifications(self):
        return self.all()