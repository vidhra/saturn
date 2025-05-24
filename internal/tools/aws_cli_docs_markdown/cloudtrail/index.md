# cloudtrailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cloudtrail

## Description

This is the CloudTrail API Reference. It provides descriptions of actions, data types, common parameters, and common errors for CloudTrail.

CloudTrail is a web service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. The recorded information includes the identity of the user, the start time of the Amazon Web Services API call, the source IP address, the request parameters, and the response elements returned by the service.

### Note

As an alternative to the API, you can use one of the Amazon Web Services SDKs, which consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .NET, iOS, Android, etc.). The SDKs provide programmatic access to CloudTrail. For example, the SDKs handle cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see [Tools to Build on Amazon Web Services](http://aws.amazon.com/tools/) .

See the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for information about the data that is included with each Amazon Web Services API call listed in the log files.

## Available Commands

- [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/add-tags.html)
- [cancel-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/cancel-query.html)
- [create-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-channel.html)
- [create-dashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-dashboard.html)
- [create-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html)
- [create-trail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html)
- [delete-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-channel.html)
- [delete-dashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-dashboard.html)
- [delete-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-event-data-store.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-resource-policy.html)
- [delete-trail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html)
- [deregister-organization-delegated-admin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/deregister-organization-delegated-admin.html)
- [describe-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-query.html)
- [describe-trails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html)
- [disable-federation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/disable-federation.html)
- [enable-federation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/enable-federation.html)
- [generate-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/generate-query.html)
- [get-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-channel.html)
- [get-dashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-dashboard.html)
- [get-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-data-store.html)
- [get-event-selectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html)
- [get-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-import.html)
- [get-insight-selectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-insight-selectors.html)
- [get-query-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-query-results.html)
- [get-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-resource-policy.html)
- [get-trail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html)
- [get-trail-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail-status.html)
- [list-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-channels.html)
- [list-dashboards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-dashboards.html)
- [list-event-data-stores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-event-data-stores.html)
- [list-import-failures](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-import-failures.html)
- [list-imports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-imports.html)
- [list-insights-metric-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-insights-metric-data.html)
- [list-public-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-public-keys.html)
- [list-queries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-queries.html)
- [list-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-tags.html)
- [list-trails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-trails.html)
- [lookup-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/lookup-events.html)
- [put-event-selectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html)
- [put-insight-selectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-resource-policy.html)
- [register-organization-delegated-admin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/register-organization-delegated-admin.html)
- [remove-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/remove-tags.html)
- [restore-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/restore-event-data-store.html)
- [search-sample-queries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/search-sample-queries.html)
- [start-dashboard-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-dashboard-refresh.html)
- [start-event-data-store-ingestion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-event-data-store-ingestion.html)
- [start-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-import.html)
- [start-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-logging.html)
- [start-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-query.html)
- [stop-event-data-store-ingestion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/stop-event-data-store-ingestion.html)
- [stop-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/stop-import.html)
- [stop-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/stop-logging.html)
- [update-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-channel.html)
- [update-dashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-dashboard.html)
- [update-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-event-data-store.html)
- [update-trail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html)
- [validate-logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/validate-logs.html)
- [verify-query-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/verify-query-results.html)