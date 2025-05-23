# kmsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# kms

## Description

Key Management Service (KMS) is an encryption and key management web service. This guide describes the KMS operations that you can call programmatically. For general information about KMS, see the ` *Key Management Service Developer Guide* [https://docs.aws.amazon.com/kms/latest/developerguide/](https://docs.aws.amazon.com/kms/latest/developerguide/)[`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#id1)__ .

### Note

KMS has replaced the term *customer master key (CMK)* with *KMS key* and *KMS key* . The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.

Amazon Web Services provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, macOS, Android, etc.). The SDKs provide a convenient way to create programmatic access to KMS and other Amazon Web Services services. For example, the SDKs take care of tasks such as signing requests (see below), managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/) .

We recommend that you use the Amazon Web Services SDKs to make programmatic API calls to KMS.

If you need to use FIPS 140-2 validated cryptographic modules when communicating with Amazon Web Services, use the FIPS endpoint in your preferred Amazon Web Services Region. For more information about the available FIPS endpoints, see [Service endpoints](https://docs.aws.amazon.com/general/latest/gr/kms.html#kms_region) in the Key Management Service topic of the *Amazon Web Services General Reference* .

All KMS API calls must be signed and be transmitted using Transport Layer Security (TLS). KMS recommends you always use the latest supported TLS version. Clients must also support cipher suites with Perfect Forward Secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

**Signing Requests**

Requests must be signed using an access key ID and a secret access key. We strongly recommend that you do not use your Amazon Web Services account root access key ID and secret access key for everyday work. You can use the access key ID and secret access key for an IAM user or you can use the Security Token Service (STS) to generate temporary security credentials and use those to sign requests.

All KMS requests must be signed with [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

**Logging API Requests**

KMS supports CloudTrail, a service that logs Amazon Web Services API calls and related events for your Amazon Web Services account and delivers them to an Amazon S3 bucket that you specify. By using the information collected by CloudTrail, you can determine what requests were made to KMS, who made the request, when it was made, and so on. To learn more about CloudTrail, including how to turn it on and find your log files, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/) .

**Additional Resources**

For more information about credentials and request signing, see the following:

- [Amazon Web Services Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) - This topic provides general information about the types of credentials used to access Amazon Web Services.
- [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) - This section of the *IAM User Guide* describes how to create and use temporary security credentials.
- [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) - This set of topics walks you through the process of signing a request using an access key ID and a secret access key.

**Commonly Used API Operations**

Of the API operations discussed in this guide, the following will prove the most useful for most applications. You will likely perform operations other than these, such as creating keys and assigning policies, by using the console.

- Encrypt
- Decrypt
- GenerateDataKey
- GenerateDataKeyWithoutPlaintext

## Available Commands

- [cancel-key-deletion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/cancel-key-deletion.html)
- [connect-custom-key-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/connect-custom-key-store.html)
- [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-alias.html)
- [create-custom-key-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-custom-key-store.html)
- [create-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-grant.html)
- [create-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html)
- [decrypt](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/decrypt.html)
- [delete-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-alias.html)
- [delete-custom-key-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-custom-key-store.html)
- [delete-imported-key-material](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-imported-key-material.html)
- [derive-shared-secret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/derive-shared-secret.html)
- [describe-custom-key-stores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-custom-key-stores.html)
- [describe-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html)
- [disable-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html)
- [disable-key-rotation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key-rotation.html)
- [disconnect-custom-key-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disconnect-custom-key-store.html)
- [enable-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key.html)
- [enable-key-rotation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key-rotation.html)
- [encrypt](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/encrypt.html)
- [generate-data-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key.html)
- [generate-data-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key-pair.html)
- [generate-data-key-pair-without-plaintext](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key-pair-without-plaintext.html)
- [generate-data-key-without-plaintext](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-data-key-without-plaintext.html)
- [generate-mac](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-mac.html)
- [generate-random](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/generate-random.html)
- [get-key-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html)
- [get-key-rotation-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-rotation-status.html)
- [get-parameters-for-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-parameters-for-import.html)
- [get-public-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-public-key.html)
- [import-key-material](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/import-key-material.html)
- [list-aliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-aliases.html)
- [list-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-grants.html)
- [list-key-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-key-policies.html)
- [list-key-rotations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-key-rotations.html)
- [list-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-keys.html)
- [list-resource-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-resource-tags.html)
- [list-retirable-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-retirable-grants.html)
- [put-key-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/put-key-policy.html)
- [re-encrypt](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html)
- [replicate-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/replicate-key.html)
- [retire-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/retire-grant.html)
- [revoke-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/revoke-grant.html)
- [rotate-key-on-demand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/rotate-key-on-demand.html)
- [schedule-key-deletion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/schedule-key-deletion.html)
- [sign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/sign.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/untag-resource.html)
- [update-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-alias.html)
- [update-custom-key-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-custom-key-store.html)
- [update-key-description](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-key-description.html)
- [update-primary-region](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-primary-region.html)
- [verify](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/verify.html)
- [verify-mac](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/verify-mac.html)