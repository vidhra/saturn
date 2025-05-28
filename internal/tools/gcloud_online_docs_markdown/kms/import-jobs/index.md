# gcloud kms import-jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs)*

**NAME**

: **gcloud kms import-jobs - create and manage import jobs**

**SYNOPSIS**

: **`gcloud kms import-jobs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import jobs can be used to create CryptoKeyVersions using pre-existing key
material, generated outside of Cloud KMS.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/add-iam-policy-binding)`**:
Add IAM policy binding to a KMS import job.

**`[create](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create)`**:
Create a new import job.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe)`**:
Get metadata for a given import job.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/get-iam-policy)`**:
Get the IAM policy for an import job.

**`[list](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/list)`**:
Lists import jobs within a keyring.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/remove-iam-policy-binding)`**:
Remove IAM policy binding for a KMS import job.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/set-iam-policy)`**:
Set the IAM policy binding for a KMS import job.

**NOTES**

: These variants are also available:

```
gcloud alpha kms import-jobs
```

```
gcloud beta kms import-jobs
```