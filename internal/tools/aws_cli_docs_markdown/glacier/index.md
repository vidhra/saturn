# glacierÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# glacier

## Description

Amazon S3 Glacier (Glacier) is a storage solution for âcold data.â

Glacier is an extremely low-cost storage service that provides secure, durable, and easy-to-use storage for data backup and archival. With Glacier, customers can store their data cost effectively for months, years, or decades. Glacier also enables customers to offload the administrative burdens of operating and scaling storage to AWS, so they donât have to worry about capacity planning, hardware provisioning, data replication, hardware failure and recovery, or time-consuming hardware migrations.

Glacier is a great storage choice when low storage cost is paramount and your data is rarely retrieved. If your application requires fast or frequent access to your data, consider using Amazon S3. For more information, see [Amazon Simple Storage Service (Amazon S3)](http://aws.amazon.com/s3/) .

You can store any kind of data in any format. There is no maximum limit on the total amount of data you can store in Glacier.

If you are a first-time user of Glacier, we recommend that you begin by reading the following sections in the *Amazon S3 Glacier Developer Guide* :

- [What is Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) - This section of the Developer Guide describes the underlying data model, the operations it supports, and the AWS SDKs that you can use to interact with the service.
- [Getting Started with Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html) - The Getting Started section walks you through the process of creating a vault, uploading archives, creating jobs to download archives, retrieving the job output, and deleting archives.

## Available Commands

- [abort-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-multipart-upload.html)
- [abort-vault-lock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-vault-lock.html)
- [add-tags-to-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/add-tags-to-vault.html)
- [complete-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-multipart-upload.html)
- [complete-vault-lock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-vault-lock.html)
- [create-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/create-vault.html)
- [delete-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-archive.html)
- [delete-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault.html)
- [delete-vault-access-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-access-policy.html)
- [delete-vault-notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-notifications.html)
- [describe-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-job.html)
- [describe-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-vault.html)
- [get-data-retrieval-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-data-retrieval-policy.html)
- [get-job-output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-job-output.html)
- [get-vault-access-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-access-policy.html)
- [get-vault-lock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-lock.html)
- [get-vault-notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-notifications.html)
- [initiate-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-job.html)
- [initiate-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-multipart-upload.html)
- [initiate-vault-lock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-vault-lock.html)
- [list-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-jobs.html)
- [list-multipart-uploads](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-multipart-uploads.html)
- [list-parts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-parts.html)
- [list-provisioned-capacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-provisioned-capacity.html)
- [list-tags-for-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-tags-for-vault.html)
- [list-vaults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-vaults.html)
- [purchase-provisioned-capacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/purchase-provisioned-capacity.html)
- [remove-tags-from-vault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/remove-tags-from-vault.html)
- [set-data-retrieval-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-data-retrieval-policy.html)
- [set-vault-access-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-vault-access-policy.html)
- [set-vault-notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-vault-notifications.html)
- [upload-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/upload-archive.html)
- [upload-multipart-part](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/upload-multipart-part.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/wait/index.html)