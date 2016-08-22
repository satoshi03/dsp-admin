from django.contrib import admin

from .models import Campaign, Client, Creative, Product


class CreativeInline(admin.TabularInline):
    model = Creative
    extra = 3
    fields = ('campaign', 'title', 'description', 'url', 'image_url')


class CreativeAdmin(admin.ModelAdmin):
    fields = ('campaign', 'title', 'description', 'url', 'image_url', 'approval_status', 'delivery_status')
    list_display = ('campaign', 'title', 'description', 'url', 'image_url', 'approval_status', 'delivery_status')


class CampaignInline(admin.StackedInline):
    model = Campaign
    extra = 1
    fields = (
        'product',
        'name',
        'daily_budget',
        'total_budget',
        'price_type',
        'price',
        'bid_type',
        'starts_at',
        'ends_at'
    ) # 変更可能なフィールド


class CampaignAdmin(admin.ModelAdmin):
    inlines = [CreativeInline]
    fields = CampaignInline.fields
    list_display = (
        'id',
        'product',
        'name',
        'daily_budget',
        'total_budget',
        'consumption',
        'price_type',
        'price',
        'bid_type',
        'status',
        'starts_at',
        'ends_at'
    ) # 表示するフィールド


class ProductAdmin(admin.ModelAdmin):
    inlines = [CampaignInline]
    list_display = ('name', 'product_type')


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Creative, CreativeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
