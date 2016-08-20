SELECT
  campaign.id AS campaign_id,
  creative.id AS creative_id,
  campaign.price_type,
  campaign.price,
  campaign.bid_type,
  creative.url,
  creative.image_url,
  creative.title
FROM
  campaign_campaign AS campaign
JOIN
  campaign_creative AS creative
ON
  campaign.id = creative.campaign_id
WHERE
  campaign.starts_at <= 'datetime.now'
AND
(
  campaign.ends_at > 'datetime.now'
OR
  campaign.ends_at is NULL
)
AND
  creative.approval_status = 1 -- accept
AND
  creative.delivery_status = 1 -- start
AND
  campaign.consumption < campaign.total_budget
