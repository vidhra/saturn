# gcloud kms keys versions restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore)*

**NAME**

: **gcloud kms keys versions restore - restore a version scheduled for destruction**

**SYNOPSIS**

: **`gcloud kms keys versions restore` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore#VERSION)` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restores the given version that was scheduled to be destroyed.
This moves the version from Scheduled for destruction to Disabled. Only versions
which are Scheduled for destruction can be Restored.

**EXAMPLES**

: The following command restores version 9 of key `frodo` within
keyring `fellowship` and location `us-east1` which was
previously scheduled for destruction:

```
gcloud kms keys versions restore 9 --location=us-east1 --keyring=fellowship --key=frodo
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to restore.

**FLAGS**

: **--key**:
The containing key.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

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
gcloud alpha kms keys versions restore
```

```
gcloud beta kms keys versions restore
```