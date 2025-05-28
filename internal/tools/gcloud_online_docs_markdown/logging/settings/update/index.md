# gcloud logging settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/settings/update](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update)*

**NAME**

: **gcloud logging settings update - update the settings for the Cloud Logging Logs Router**

**SYNOPSIS**

: **`gcloud logging settings update` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--organization)`=`ORGANIZATION_ID`) [`[--disable-default-sink](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--disable-default-sink)`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--storage-location)`=`STORAGE_LOCATION`] [`[--clear-kms-key](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--clear-kms-key)`     | [`[--kms-key-name](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--kms-key-name)`=`KMS_KEY_NAME` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#--kms-project)`=`KMS_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Use this command to update the `--kms-key-name, --storage-location,
--disable-default-sink` and --analytics-mode associated with the Cloud
Logging Logs Router.
The Cloud KMS key must already exist and Cloud Logging must have permission to
access it.
The storage location must be allowed by Org Policy.
Customer-managed encryption keys (CMEK) for the Logs Router can currently only
be configured at the organization-level and will apply to all projects in the
organization.

**EXAMPLES**

: To enable CMEK for the Logs Router for an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --kms-key-name='projects/my-project/locations/my-location/keyRings/my-keyring/cryptoKeys/key'
```

To disable CMEK for the Logs Router for an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --clear-kms-key
```

To update storage location for the Logs Router for an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --storage-location=[LOCATION_ID]
```

To update storage location for the Logs Router for a folder, run:

```
gcloud logging settings update --folder=[FOLDER_ID] --storage-location=[LOCATION_ID]
```

To disable default sink for the Logs Router for an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=true
```

To enable default sink for the Logs Router for an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=false
```

To enable analytics for the log buckets under an organization, run:

```
gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=false --analytics-mode=required
```

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--disable-default-sink**:
Enable or disable `_Default` sink for the `_Default`
bucket. Specify --no-disable-default-sink to enable a disabled
`_Default` sink. Note: It only applies to the newly created projects
and will not affect the projects created before.

**--storage-location**:
Update the storage location for `_Default` bucket and
`_Required` bucket. Note: It only applies to the newly created
projects and will not affect the projects created before.

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
gcloud alpha logging settings update
```

```
gcloud beta logging settings update
```