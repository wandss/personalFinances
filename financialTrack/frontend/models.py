from django.db import models

class Menus(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

class NavMenu(Menus):
    link = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class DropdownMenu(Menus):
    title = models.ForeignKey(NavMenu, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name="title")
    link = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AppData(models.Model):
    app_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'App Data'

    def __str__(self):
        return self.app_name
