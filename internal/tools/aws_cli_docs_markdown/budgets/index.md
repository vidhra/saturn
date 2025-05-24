# budgetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# budgets

## Description

Use the Amazon Web Services Budgets API to plan your service usage, service costs, and instance reservations. This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for the Amazon Web Services Budgets feature.

Budgets provide you with a way to see the following information:

- How close your plan is to your budgeted amount or to the free tier limits
- Your usage-to-date, including how much youâve used of your Reserved Instances (RIs)
- Your current estimated charges from Amazon Web Services, and how much your predicted usage will accrue in charges by the end of the month
- How much of your budget has been used

Amazon Web Services updates your budget status several times a day. Budgets track your unblended costs, subscriptions, refunds, and RIs. You can create the following types of budgets:

- **Cost budgets** - Plan how much you want to spend on a service.
- **Usage budgets** - Plan how much you want to use one or more services.
- **RI utilization budgets** - Define a utilization threshold, and receive alerts when your RI usage falls below that threshold. This lets you see if your RIs are unused or under-utilized.
- **RI coverage budgets** - Define a coverage threshold, and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold. This lets you see how much of your instance usage is covered by a reservation.

Service Endpoint

The Amazon Web Services Budgets API provides the following endpoint:

- [https://budgets.amazonaws.com](https://budgets.amazonaws.com)

For information about costs that are associated with the Amazon Web Services Budgets API, see [Amazon Web Services Cost Management Pricing](https://aws.amazon.com/aws-cost-management/pricing/) .

## Available Commands

- [create-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html)
- [create-budget-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget-action.html)
- [create-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-notification.html)
- [create-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-subscriber.html)
- [delete-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget.html)
- [delete-budget-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget-action.html)
- [delete-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-notification.html)
- [delete-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-subscriber.html)
- [describe-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html)
- [describe-budget-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action.html)
- [describe-budget-action-histories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action-histories.html)
- [describe-budget-actions-for-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-actions-for-account.html)
- [describe-budget-actions-for-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-actions-for-budget.html)
- [describe-budget-notifications-for-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-notifications-for-account.html)
- [describe-budget-performance-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-performance-history.html)
- [describe-budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html)
- [describe-notifications-for-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-notifications-for-budget.html)
- [describe-subscribers-for-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-subscribers-for-notification.html)
- [execute-budget-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/execute-budget-action.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/untag-resource.html)
- [update-budget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html)
- [update-budget-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget-action.html)
- [update-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-notification.html)
- [update-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-subscriber.html)