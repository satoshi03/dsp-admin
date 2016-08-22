from django.contrib import admin

from .models import Campaign


class CampaignReportAdmin(admin.ModelAdmin):
    list_display = ('campaign_id',
                    'impression',
                    'click',
                    'conversion',
                    'consumption',
                    'ctr',
                    'cvr',
                    'cpa',
                    )


admin.site.register(Campaign, CampaignReportAdmin)
