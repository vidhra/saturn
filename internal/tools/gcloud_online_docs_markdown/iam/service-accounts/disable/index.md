# gcloud iam service-accounts disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/disable](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/disable)*

**NAME**

: **gcloud iam service-accounts disable - disable an IAM service account**

**SYNOPSIS**

: **`gcloud iam service-accounts disable` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/disable#SERVICE_ACCOUNT)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Disable an IAM service account. After the service account is disabled,
credential generation and API requests using this service account will fail.
Using `gcloud iam service-accounts enable` to re-enable it.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To disable a service account from your project, run:

```
gcloud iam service-accounts disable my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **ServiceAccount resource - The IAM service account to disable. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `service_account` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_ACCOUNT`**:
ID of the serviceAccount or fully qualified identifier for the serviceAccount.
To set the `service_account` attribute:

- provide the argument `service_account` on the command line.**

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

**API REFERENCE**

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts disable
```

```
gcloud beta iam service-accounts disable
```