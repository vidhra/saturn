# payment-cryptographyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# payment-cryptography

## Description

Amazon Web Services Payment Cryptography Control Plane APIs manage encryption keys for use during payment-related cryptographic operations. You can create, import, export, share, manage, and delete keys. You can also manage Identity and Access Management (IAM) policies for keys. For more information, see [Identity and access management](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html) in the *Amazon Web Services Payment Cryptography User Guide.*

To use encryption keys for payment-related transaction processing and associated cryptographic operations, you use the [Amazon Web Services Payment Cryptography Data Plane](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/Welcome.html) . You can perform actions like encrypt, decrypt, generate, and verify payment-related data.

All Amazon Web Services Payment Cryptography API calls must be signed and transmitted using Transport Layer Security (TLS). We recommend you always use the latest supported TLS version for logging API requests.

Amazon Web Services Payment Cryptography supports CloudTrail for control plane operations, a service that logs Amazon Web Services API calls and related events for your Amazon Web Services account and delivers them to an Amazon S3 bucket you specify. By using the information collected by CloudTrail, you can determine what requests were made to Amazon Web Services Payment Cryptography, who made the request, when it was made, and so on. If you donât conï¬gure a trail, you can still view the most recent events in the CloudTrail console. For more information, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/) .

## Available Commands

- [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-alias.html)
- [create-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-key.html)
- [delete-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-alias.html)
- [delete-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-key.html)
- [export-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/export-key.html)
- [get-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-alias.html)
- [get-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-key.html)
- [get-parameters-for-export](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-parameters-for-export.html)
- [get-parameters-for-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-parameters-for-import.html)
- [get-public-key-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-public-key-certificate.html)
- [import-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/import-key.html)
- [list-aliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-aliases.html)
- [list-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-keys.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-tags-for-resource.html)
- [restore-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/restore-key.html)
- [start-key-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/start-key-usage.html)
- [stop-key-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/stop-key-usage.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/untag-resource.html)
- [update-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/update-alias.html)