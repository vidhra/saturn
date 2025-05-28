# gcloud iam service-accounts update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update)*

**NAME**

: **gcloud iam service-accounts update - update an IAM service account**

**SYNOPSIS**

: **`gcloud iam service-accounts update` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update#SERVICE_ACCOUNT)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an IAM service account.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To update the description and display name for a service account, run:

```
gcloud iam service-accounts update my-iam-account@my-project.iam.gserviceaccount.com --description="Updated description." --display-name="Updated Name"
```

**POSITIONAL ARGUMENTS**

: **ServiceAccount resource - The service account to update. The account should be
formatted either as a numeric service account ID or as an email, like this:
123456789876543212345 or my-iam-account@somedomain.com. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

**FLAGS**

: **--description**:
The new textual description for the account.

**--display-name**:
The new textual name to display for the account.

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
gcloud alpha iam service-accounts update
```

```
gcloud beta iam service-accounts update
```