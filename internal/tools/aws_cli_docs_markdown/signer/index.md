# signerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# signer

## Description

AWS Signer is a fully managed code-signing service to help you ensure the trust and integrity of your code.

Signer supports the following applications:

With code signing for AWS Lambda, you can sign [AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/) deployment packages. Integrated support is provided for [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/gsg/) , [Amazon CloudWatch](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) , and [AWS CloudTrail](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/) . In order to sign code, you create a signing profile and then use Signer to sign Lambda zip files in S3.

With code signing for IoT, you can sign code for any IoT device that is supported by AWS. IoT code signing is available for [Amazon FreeRTOS](http://docs.aws.amazon.com/freertos/latest/userguide/) and [AWS IoT Device Management](http://docs.aws.amazon.com/iot/latest/developerguide/) , and is integrated with [AWS Certificate Manager (ACM)](http://docs.aws.amazon.com/acm/latest/userguide/) . In order to sign code, you import a third-party code-signing certificate using ACM, and use that to sign updates in Amazon FreeRTOS and AWS IoT Device Management.

With Signer and the Notation CLI from the [Notary Project](https://notaryproject.dev/) , you can sign container images stored in a container registry such as Amazon Elastic Container Registry (ECR). The signatures are stored in the registry alongside the images, where they are available for verifying image authenticity and integrity.

For more information about Signer, see the [AWS Signer Developer Guide](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) .

## Available Commands

- [add-profile-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/add-profile-permission.html)
- [cancel-signing-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/cancel-signing-profile.html)
- [describe-signing-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/describe-signing-job.html)
- [get-revocation-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-revocation-status.html)
- [get-signing-platform](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-platform.html)
- [get-signing-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-profile.html)
- [list-profile-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-profile-permissions.html)
- [list-signing-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-jobs.html)
- [list-signing-platforms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-platforms.html)
- [list-signing-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-tags-for-resource.html)
- [put-signing-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/put-signing-profile.html)
- [remove-profile-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/remove-profile-permission.html)
- [revoke-signature](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/revoke-signature.html)
- [revoke-signing-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/revoke-signing-profile.html)
- [sign-payload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/sign-payload.html)
- [start-signing-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/start-signing-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/untag-resource.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/wait/index.html)