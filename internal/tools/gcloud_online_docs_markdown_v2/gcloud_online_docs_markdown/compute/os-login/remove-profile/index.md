# gcloud compute os-login remove-profile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-login/remove-profile](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/remove-profile)*

**NAME**

: **gcloud compute os-login remove-profile - remove the posix account information for the current user**

**SYNOPSIS**

: **`gcloud compute os-login remove-profile` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/remove-profile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute os-login remove-profile` removes the posix account
information for the current user where the account ID field is set to the
current project ID. Posix account entries for G Suite users do not set the
account ID field and can only be modified by a domain administrator.

**EXAMPLES**

: To remove all POSIX accounts associated with the current user and project, run:

```
gcloud compute os-login remove-profile
```

To remove all POSIX accounts associated with the current user in the project
named `example-project`, run:

```
gcloud compute os-login remove-profile --project=example-project
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
gcloud alpha compute os-login remove-profile
```

```
gcloud beta compute os-login remove-profile
```