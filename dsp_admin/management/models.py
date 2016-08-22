from datetime import datetime

from django.db import models


class Client(models.Model):
    class Meta:
        verbose_name = 'クライアント'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True)
    name = models.CharField('クライアント名', max_length=255, default="")
    address = models.CharField('住所', max_length=65535, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'プロダクト'
        verbose_name_plural = verbose_name

    WEB = 0
    APP = 1
    PRODUCT_TYPE_CHOICES = (
        (WEB, 'web'),
        (APP, 'app'),
    )

    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='クライアント')
    name = models.CharField('商品名', max_length=255)
    product_type = models.IntegerField('商品種別', choices=PRODUCT_TYPE_CHOICES, default=WEB)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    class Meta:
        verbose_name = 'キャンペーン'
        verbose_name_plural = verbose_name

    DEFAULT = 0
    RETARGET = 1
    BID_TYPE_CHOICE = (
        (DEFAULT, 'デフォルト'),
        (RETARGET, 'リターゲティング'),
    )

    CPC = 0
    CPM = 1
    CPA = 2
    PRICE_TYPE_CHOICE = (
        (CPC, 'cpc'),
        (CPM, 'cpm'),
        (CPA, 'cpa'),
    )

    WAIT = 0
    ACTIVE = 1
    PENDING = 2
    FINISH = 3
    LUCK_OF_FUNDS = 4
    PENDING = 5
    CAMPAIGN_STATUS_CHOICE = (
        (WAIT, '開始待ち'),
        (ACTIVE, '配信中'),
        (FINISH, '終了'),
        (PENDING, '一時停止'),
        (LUCK_OF_FUNDS, '予算超過'),
    )

    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='広告商品')
    name = models.CharField('キャンペーン名', max_length=255)
    daily_budget = models.IntegerField('日予算', default=0)
    total_budget = models.IntegerField('トータル予算', default=0)
    consumption = models.IntegerField('消化予算', default=0)
    price_type = models.IntegerField('入札形式', choices=PRICE_TYPE_CHOICE, default=CPC)
    price = models.IntegerField('入札価格', default=0)
    bid_type = models.IntegerField('配信形式', choices=BID_TYPE_CHOICE, default=DEFAULT)
    status = models.IntegerField('配信ステータス', choices=CAMPAIGN_STATUS_CHOICE, default=WAIT)
    starts_at = models.DateTimeField('キャンペーン開始日時', default=datetime.now)
    ends_at = models.DateTimeField('キャンペーン終了日時', default=datetime.now)

    def __str__(self):
        return self.name


class Creative(models.Model):
    class Meta:
        verbose_name = 'クリエイティブ'
        verbose_name_plural = verbose_name

    WAIT = 0
    ACCEPT = 1
    DENY = 2
    APPROVAL_STATUS_CHOICE = (
        (WAIT, '承認待ち'),
        (ACCEPT, '承認済み'),
        (DENY, '不承認'),
    )

    STOP = 0
    START = 1
    DELIVERY_STATUS_CHOICE = (
        (STOP, '停止'),
        (START, '配信'),
    )

    id = models.IntegerField(primary_key=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, verbose_name='キャンペーン')
    title = models.CharField('タイトル', max_length=30)
    description = models.CharField('説明', max_length=255)
    url = models.CharField('遷移先URL', max_length=65535)
    image_url = models.ImageField('画像URL', upload_to='campaign/images/', max_length=65535)
    approval_status = models.IntegerField('承認ステータス', choices=APPROVAL_STATUS_CHOICE, default=WAIT)
    delivery_status = models.BooleanField('配信ステータス', choices=DELIVERY_STATUS_CHOICE, default=STOP)

    def __str__(self):
        return self.title
