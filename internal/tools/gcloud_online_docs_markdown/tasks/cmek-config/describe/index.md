# gcloud tasks cmek-config describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/describe](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/describe)*

**NAME**

: **gcloud tasks cmek-config describe - get CMEK configuration for Cloud Tasks in the specified location**

**SYNOPSIS**

: **`gcloud tasks cmek-config describe` `[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/describe#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get CMEK configuration for Cloud Tasks in the specified location.

**EXAMPLES**

: To get a CMEK config:

```
gcloud tasks cmek-config describe --location=my-location
```

**REQUIRED FLAGS**

: **--location**:
Google Cloud location for the KMS key.

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
gcloud alpha tasks cmek-config describe
```

```
gcloud beta tasks cmek-config describe
```