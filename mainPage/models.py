from django.db import models


class Employee(models.Model):
    
    # По хорошему я бы вынес константы за класс, но есть вроде рекомендация определять их в классе
    LEVEL_OF_DIVISION = {
        '1':'LEVEL_1',
        '2':'LEVEL_1',
        '3':'LEVEL_1',
        '4':'LEVEL_1',
        '5':'LEVEL_1',
        '6':'LEVEL_2',
        '7':'LEVEL_2',
        '8':'LEVEL_2',
        '9':'LEVEL_2',
        '10':'LEVEL_2',
        '11':'LEVEL_3',
        '12':'LEVEL_3',
        '13':'LEVEL_3',
        '14':'LEVEL_3',
        '15':'LEVEL_3',
        '16':'LEVEL_4',
        '17':'LEVEL_4',
        '18':'LEVEL_4',
        '19':'LEVEL_4',
        '20':'LEVEL_4',
        '21':'LEVEL_5',
        '22':'LEVEL_5',
        '23':'LEVEL_5',
        '24':'LEVEL_5',
        '25':'LEVEL_5',
    }
    
    DIVISION_CHOICES = [
        ('1', 'division_1'),
        ('2', 'division_2'),
        ('3', 'division_3'),
        ('4', 'division_4'),
        ('5', 'division_5'),
        ('6', 'division_6'),
        ('7', 'division_7'),
        ('8', 'division_8'),
        ('9', 'division_9'),
        ('10', 'division_10'),
        ('11', 'division_11'),
        ('12', 'division_12'),
        ('13', 'division_13'),
        ('14', 'division_14'),
        ('15', 'division_15'),
        ('16', 'division_16'),
        ('17', 'division_17'),
        ('18', 'division_18'),
        ('19', 'division_19'),
        ('20', 'division_20'),
        ('21', 'division_21'),
        ('22', 'division_22'),
        ('23', 'division_23'),
        ('24', 'division_24'),
        ('25', 'division_25'),
    ]
    
    ID = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=900)
    position = models.CharField(max_length=900)
    date_of_employment = models.CharField(max_length=900)
    wages = models.CharField(max_length=900)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    # level = models.CharField(max_length=900)
    
    def level(self):
        return self.LEVEL_OF_DIVISION.get(self.division, 'LEVEL_1')
    
    def __str__(self):
        return f'ID: {self.ID}, FULLNAME: {self.fullname}, DIVISION: {self.division}, LEVEL: {self.LEVEL_OF_DIVISION.get(self.division, "LEVEL_1")}'
