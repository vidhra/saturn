# cognito-syncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cognito-sync

## Description

Amazon Cognito Sync provides an AWS service and client library that enable cross-device syncing of application-related user data. High-level client libraries are available for both iOS and Android. You can use these libraries to persist data locally so that itâs available even if the device is offline. Developer credentials donât need to be stored on the mobile device to access the service. You can use Amazon Cognito to obtain a normalized user ID and credentials. User data is persisted in a dataset that can store up to 1 MB of key-value pairs, and you can have up to 20 datasets per user identity.

With Amazon Cognito Sync, the data stored for each identity is accessible only to credentials assigned to that identity. In order to use the Cognito Sync service, you need to make API calls using credentials retrieved with [Amazon Cognito Identity service](http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html) .

If you want to use Cognito Sync in an Android or iOS application, you will probably want to make API calls via the AWS Mobile SDK. To learn more, see the [Developer Guide for Android](http://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/cognito-sync.html) and the [Developer Guide for iOS](http://docs.aws.amazon.com/mobile/sdkforios/developerguide/cognito-sync.html) .

## Available Commands

- [bulk-publish](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/bulk-publish.html)
- [delete-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/delete-dataset.html)
- [describe-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/describe-dataset.html)
- [describe-identity-pool-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/describe-identity-pool-usage.html)
- [describe-identity-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/describe-identity-usage.html)
- [get-bulk-publish-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/get-bulk-publish-details.html)
- [get-cognito-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/get-cognito-events.html)
- [get-identity-pool-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/get-identity-pool-configuration.html)
- [list-datasets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-datasets.html)
- [list-identity-pool-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-identity-pool-usage.html)
- [list-records](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-records.html)
- [register-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/register-device.html)
- [set-cognito-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/set-cognito-events.html)
- [set-identity-pool-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/set-identity-pool-configuration.html)
- [subscribe-to-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/subscribe-to-dataset.html)
- [unsubscribe-from-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/unsubscribe-from-dataset.html)
- [update-records](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/update-records.html)