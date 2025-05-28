# gcloud tasks cmek-config update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update)*

**NAME**

: **gcloud tasks cmek-config update - enable, disable, or edit CMEK configuration for Cloud Tasks in the specified location**

**SYNOPSIS**

: **`gcloud tasks cmek-config update` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#--location)`=`LOCATION`] [`[--clear-kms-key](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#--clear-kms-key)`     | [`[--kms-key-name](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#--kms-key-name)`=`KMS_KEY_NAME` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#--kms-keyring)`=`KMS_KEYRING` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enable, disable, or edit CMEK configuration for Cloud Tasks in the specified
location.

**EXAMPLES**

: To update a CMEK config:

```
gcloud tasks cmek-config update --kms-key-name=projects/my-project/locations/my-location/keyRings/my-keyring/cryptoKeys/key
```

**FLAGS**

: **--location**:
Google Cloud location for the KMS key.

**--clear-kms-key**

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
gcloud alpha tasks cmek-config update
```

```
gcloud beta tasks cmek-config update
```