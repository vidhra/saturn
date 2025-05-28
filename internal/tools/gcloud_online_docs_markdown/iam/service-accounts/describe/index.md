# gcloud iam service-accounts describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe)*

**NAME**

: **gcloud iam service-accounts describe - show metadata for a service account from a project**

**SYNOPSIS**

: **`gcloud iam service-accounts describe` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe#SERVICE_ACCOUNT)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command shows metadata for a service account.
This call can fail for the following reasons:

- The specified service account does not exist. In this case, you receive a
`PERMISSION_DENIED` error.
- The active user does not have permission to access the given service account.

**EXAMPLES**

: To print metadata for a service account from your project, run:

```
gcloud iam service-accounts describe my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`SERVICE_ACCOUNT`**:
The service account to describe. The account should be formatted either as a
numeric service account ID or as an email, like this: 123456789876543212345 or
my-iam-account@somedomain.com.

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
gcloud alpha iam service-accounts describe
```

```
gcloud beta iam service-accounts describe
```