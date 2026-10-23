from django.db import models

class Pacjent(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.TextField(max_length=100)
    nazwisko = models.TextField(max_length=100)
    miasto = models.TextField(max_length=100)
    ulica = models.TextField(max_length=100)
    wiek = models.IntegerField()
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Wizyta(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    zalecenia = models.TextField()
    pacjent = models.ForeignKey(
        Pacjent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} {self.pacjent.nazwisko}"


