# dataexchangeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# dataexchange

## Description

AWS Data Exchange is a service that makes it easy for AWS customers to exchange data in the cloud. You can use the AWS Data Exchange APIs to create, update, manage, and access file-based data set in the AWS Cloud.

As a subscriber, you can view and access the data sets that you have an entitlement to through a subscription. You can use the APIs to download or copy your entitled data sets to Amazon Simple Storage Service (Amazon S3) for use across a variety of AWS analytics and machine learning services.

As a provider, you can create and manage your data sets that you would like to publish to a product. Being able to package and provide your data sets into products requires a few steps to determine eligibility. For more information, visit the *AWS Data Exchange User Guide* .

A data set is a collection of data that can be changed or updated over time. Data sets can be updated using revisions, which represent a new version or incremental change to a data set. A revision contains one or more assets. An asset in AWS Data Exchange is a piece of data that can be stored as an Amazon S3 object, Redshift datashare, API Gateway API, AWS Lake Formation data permission, or Amazon S3 data access. The asset can be a structured data file, an image file, or some other data file. Jobs are asynchronous import or export operations used to create or copy assets.

## Available Commands

- [accept-data-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/accept-data-grant.html)
- [cancel-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/cancel-job.html)
- [create-data-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-data-grant.html)
- [create-data-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-data-set.html)
- [create-event-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-event-action.html)
- [create-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-job.html)
- [create-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-revision.html)
- [delete-asset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-asset.html)
- [delete-data-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-data-grant.html)
- [delete-data-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-data-set.html)
- [delete-event-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-event-action.html)
- [delete-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-revision.html)
- [get-asset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-asset.html)
- [get-data-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-data-grant.html)
- [get-data-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-data-set.html)
- [get-event-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-event-action.html)
- [get-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html)
- [get-received-data-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-received-data-grant.html)
- [get-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-revision.html)
- [list-data-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-grants.html)
- [list-data-set-revisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-set-revisions.html)
- [list-data-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-sets.html)
- [list-event-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-event-actions.html)
- [list-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-jobs.html)
- [list-received-data-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-received-data-grants.html)
- [list-revision-assets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-revision-assets.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-tags-for-resource.html)
- [revoke-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/revoke-revision.html)
- [send-api-asset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/send-api-asset.html)
- [send-data-set-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/send-data-set-notification.html)
- [start-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/start-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/untag-resource.html)
- [update-asset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-asset.html)
- [update-data-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-data-set.html)
- [update-event-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-event-action.html)
- [update-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-revision.html)