from django.db import models


class Vote(models.Model):
    subject = models.CharField(max_length=200)
    positive = models.BooleanField(default=True)

    @classmethod
    def in_favour(cls, subject):
        "Create a new vote in favour of the subject."
        return cls.objects.create(subject=subject)

    @classmethod
    def against(cls, subject):
        "Create a new vote against of the subject."
        return cls.objects.create(subject=subject, positive=False)

    @classmethod
    def results_for(cls, subject):
        "Return the voting results for the subject."
        # BEGIN (write your solution here)
        in_favour = Vote.objects.filter(positive=True).filter(subject=subject).count()
        print(in_favour)
        against = Vote.objects.filter(positive=False).filter(subject=subject).count()
        print(against)
        return {"in favour": in_favour, "against": against}
        # END
# решение преподавателя:
"""        # BEGIN
        subject_votes = cls.objects.filter(subject=subject)
        return {
            'in favour': subject_votes.filter(positive=True).count(),
            'against': subject_votes.filter(positive=False).count(),
        }
        # END"""