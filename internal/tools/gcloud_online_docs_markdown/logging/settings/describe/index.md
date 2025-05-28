# gcloud logging settings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe)*

**NAME**

: **gcloud logging settings describe - display the settings for the Cloud Logging Logs Router**

**SYNOPSIS**

: **`gcloud logging settings describe` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/settings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If `kmsKeyName` is present in the output, then CMEK is enabled for
your project, folder, organization or billing-account. You can also find the
Logs Router service account using this command.

**EXAMPLES**

: To describe the Logs Router settings for a project, run:

```
gcloud logging settings describe --project=[PROJECT_ID]
```

To describe the Logs Router settings for an organization, run:

```
gcloud logging settings describe --organization=[ORGANIZATION_ID]
```

```
kmsKeyName:
'projects/my-project/locations/my-location/keyRings/my-keyring/cryptoKeys/key'
name: 'organizations/[ORGANIZATION_ID]/settings'
serviceAccountId:
'[SERVICE_ACCOUNT_ID]@gcp-sa-logging.iam.gserviceaccount.com'
```

**FLAGS**

: **--billing-account**

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
gcloud alpha logging settings describe
```

```
gcloud beta logging settings describe
```