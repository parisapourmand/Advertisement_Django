from django import forms

from advertiser_management.models import Ad


class InfoForm(forms.Form):
    id = forms.IntegerField()

    def get_info(self):
        ad = Ad.objects.get(pk=self.cleaned_data['id'])
        ad.get_total_hourly_info()
        ad.get_click_view_rate()
        ad.get_avg_difference()
        return [ad.get_total_hourly_info(),
                ad.get_click_view_rate(),
                ad.get_avg_difference()]
