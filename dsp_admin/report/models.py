from django.db import models

from management.models import Campaign

class Campaign(models.Model):
    class Meta:
        verbose_name = 'キャンペーンレポート'
        verbose_name_plural = verbose_name

    campaign = models.ForeignKey(Campaign)
    impression = models.IntegerField('インプレッション数', default=0)
    click = models.IntegerField('クリック数', default=0)
    conversion = models.IntegerField('コンバージョン数', default=0)
    consumption = models.IntegerField('消化予算', default=0)
    ctr = models.DecimalField('クリック率', max_digits=10, decimal_places=3, default=0.0)
    cvr = models.DecimalField('コンバージョン率', max_digits=10, decimal_places=3, default=0.0)
    cpa = models.DecimalField('CPA', max_digits=10, decimal_places=3, default=0.0)
    delivered_at = models.DateField('配信日')

