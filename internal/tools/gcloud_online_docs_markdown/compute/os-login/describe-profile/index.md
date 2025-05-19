# gcloud compute os-login describe-profile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile)*

**NAME**

: **gcloud compute os-login describe-profile - describe the OS Login profile for the current user**

**SYNOPSIS**

: **`gcloud compute os-login describe-profile` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-login/describe-profile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute os-login describe-profile` displays the OS Login
profile for the currently authenticated user, including Posix accounts and SSH
keys associated with the user.

**EXAMPLES**

: To show all of the information about your OS Login profile, including POSIX
account information and stored SSH public keys, run:

```
gcloud compute os-login describe-profile
```

To show all of the information in a different format, such as JSON, use the
`--format` flag:

```
gcloud compute os-login describe-profile --format=json
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
gcloud alpha compute os-login describe-profile
```

```
gcloud beta compute os-login describe-profile
```