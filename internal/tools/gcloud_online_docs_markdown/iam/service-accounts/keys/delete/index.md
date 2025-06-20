# gcloud iam service-accounts keys delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete)*

**NAME**

: **gcloud iam service-accounts keys delete - delete a service account key**

**SYNOPSIS**

: **`gcloud iam service-accounts keys delete` `KEY-ID` `[--iam-account](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete#--iam-account)`=`IAM_ACCOUNT` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To delete a key with ID `b4f1037aeef9ab37deee9` for the service
account `my-iam-account@my-project.iam.gserviceaccount.com`, run:

```
gcloud iam service-accounts keys delete b4f1037aeef9ab37deee9 --iam-account=my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`KEY-ID`**:
The key to delete.

**REQUIRED FLAGS**

: **--iam-account**:
The service account from which to delete a key.
To list all service accounts in the project, run:

```
gcloud iam service-accounts list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts keys delete
```

```
gcloud beta iam service-accounts keys delete
```