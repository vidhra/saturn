# gcloud iam service-accounts undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/undelete](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/undelete)*

**NAME**

: **gcloud iam service-accounts undelete - undelete a service account for a project**

**SYNOPSIS**

: **`gcloud iam service-accounts undelete` `[ACCOUNT_ID](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/undelete#ACCOUNT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/undelete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Undelete a service account for a project.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: The following command undeletes a service account with unique id
`103271949540120710052`:

```
gcloud iam service-accounts undelete 103271949540120710052
```

**POSITIONAL ARGUMENTS**

: **`ACCOUNT_ID`**:
The deleted service account's unique ID must be provided when using the undelete
command. Unique IDs are a 21 digit number, such as 103271949540120710052.

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
gcloud alpha iam service-accounts undelete
```

```
gcloud beta iam service-accounts undelete
```