# gcloud kms keys versions destroy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy)*

**NAME**

: **gcloud kms keys versions destroy - schedule a version to be destroyed**

**SYNOPSIS**

: **`gcloud kms keys versions destroy` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy#VERSION)` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/destroy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Schedules the given version for destruction in 24 hours.
After that time period passes it is automatically destroyed. Once destroyed, the
key material is removed but the version number can not be reused.
Only versions which are Enabled or Disabled can be Scheduled for destruction.

**EXAMPLES**

: The following command schedules version 9 of key `frodo` within
keyring `fellowship` and location `us-east1` for
destruction:

```
gcloud kms keys versions destroy 9 --location=us-east1 --keyring=fellowship --key=frodo
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to destroy.

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
gcloud alpha kms keys versions destroy
```

```
gcloud beta kms keys versions destroy
```