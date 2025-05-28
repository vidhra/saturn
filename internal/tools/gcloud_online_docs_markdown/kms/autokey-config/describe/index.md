# gcloud kms autokey-config describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/describe](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/describe)*

**NAME**

: **gcloud kms autokey-config describe - describe the AutokeyConfig of a folder**

**SYNOPSIS**

: **`gcloud kms autokey-config describe` `[--folder](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/describe#--folder)`=`FOLDER` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud kms autokey-config describe can be used to retrieve the AutokeyConfig of
a folder.

**EXAMPLES**

: The following command retrieves the AutokeyConfig of a folder having folder-id
`123`:

```
gcloud kms autokey-config describe --folder=123
```

**REQUIRED FLAGS**

: **--folder**:
The folder id in which the AutokeyConfig resource exists.

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
gcloud alpha kms autokey-config describe
```

```
gcloud beta kms autokey-config describe
```