# billingconductorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# billingconductor

## Description

Amazon Web Services Billing Conductor is a fully managed service that you can use to customize a [proforma](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-eb.html#eb-other-definitions) version of your billing data each month, to accurately show or chargeback your end customers. Amazon Web Services Billing Conductor doesnât change the way youâre billed by Amazon Web Services each month by design. Instead, it provides you with a mechanism to configure, generate, and display rates to certain customers over a given billing period. You can also analyze the difference between the rates you apply to your accounting groupings relative to your actual rates from Amazon Web Services. As a result of your Amazon Web Services Billing Conductor configuration, the payer account can also see the custom rate applied on the billing details page of the [Amazon Web Services Billing console](https://console.aws.amazon.com/billing) , or configure a cost and usage report per billing group.

This documentation shows how you can configure Amazon Web Services Billing Conductor using its API. For more information about using the [Amazon Web Services Billing Conductor](https://console.aws.amazon.com/billingconductor/) user interface, see the [Amazon Web Services Billing Conductor User Guide](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) .

## Available Commands

- [associate-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/associate-accounts.html)
- [associate-pricing-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/associate-pricing-rules.html)
- [batch-associate-resources-to-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/batch-associate-resources-to-custom-line-item.html)
- [batch-disassociate-resources-from-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/batch-disassociate-resources-from-custom-line-item.html)
- [create-billing-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-billing-group.html)
- [create-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-custom-line-item.html)
- [create-pricing-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-pricing-plan.html)
- [create-pricing-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/create-pricing-rule.html)
- [delete-billing-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/delete-billing-group.html)
- [delete-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/delete-custom-line-item.html)
- [delete-pricing-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/delete-pricing-plan.html)
- [delete-pricing-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/delete-pricing-rule.html)
- [disassociate-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/disassociate-accounts.html)
- [disassociate-pricing-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/disassociate-pricing-rules.html)
- [get-billing-group-cost-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/get-billing-group-cost-report.html)
- [list-account-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-account-associations.html)
- [list-billing-group-cost-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-billing-group-cost-reports.html)
- [list-billing-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-billing-groups.html)
- [list-custom-line-item-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-custom-line-item-versions.html)
- [list-custom-line-items](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-custom-line-items.html)
- [list-pricing-plans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-plans.html)
- [list-pricing-plans-associated-with-pricing-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-plans-associated-with-pricing-rule.html)
- [list-pricing-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-rules.html)
- [list-pricing-rules-associated-to-pricing-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-rules-associated-to-pricing-plan.html)
- [list-resources-associated-to-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-resources-associated-to-custom-line-item.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/untag-resource.html)
- [update-billing-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-billing-group.html)
- [update-custom-line-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-custom-line-item.html)
- [update-pricing-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-pricing-plan.html)
- [update-pricing-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-pricing-rule.html)