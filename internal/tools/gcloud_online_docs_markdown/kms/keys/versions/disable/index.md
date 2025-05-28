# gcloud kms keys versions disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable)*

**NAME**

: **gcloud kms keys versions disable - disable a given version**

**SYNOPSIS**

: **`gcloud kms keys versions disable` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable#VERSION)` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Disables the specified version within the given key.
Only a version which is Enabled can be Disabled.

**EXAMPLES**

: The following command disables version 3 of key `frodo` within
keyring `fellowship` and location `us-east1`:

```
gcloud kms keys versions disable 3 --location=us-east1 --keyring=fellowship --key=frodo
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to disable.

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
gcloud alpha kms keys versions disable
```

```
gcloud beta kms keys versions disable
```