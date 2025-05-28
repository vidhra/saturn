# gcloud kms keys versions update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update)*

**NAME**

: **gcloud kms keys versions update - update a key version**

**SYNOPSIS**

: **`gcloud kms keys versions update` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#VERSION)` [`[--ekm-connection-key-path](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--ekm-connection-key-path)`=`EKM_CONNECTION_KEY_PATH`] [`[--external-key-uri](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--external-key-uri)`=`EXTERNAL_KEY_URI`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--location)`=`LOCATION`] [`[--state](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#--state)`=`STATE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud kms keys versions update can be used to update the key versions. Updates
can be made to the the key versions's state (enabling or disabling it), to its
external key URI (if the key version has protection level EXTERNAL), or to its
ekm connection key path (if the key version has protection level EXTERNAL_VPC).

**EXAMPLES**

: The following command enables the key version 8 of key `frodo` within
keyring `fellowship` and location `us-east1`:

```
gcloud kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --state=enabled
```

The following command disables the key version 8 of key `frodo`
within keyring `fellowship` and location `us-east1`:

```
gcloud kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --state=disabled
```

The following command updates the external key URI of version 8 of key
`frodo` within keyring `fellowship` and location
`us-east1`:

```
gcloud kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --external-key-uri=https://example.kms/v0/some/key/path
```

The following command updates the ekm connection key path of version 8 of key
`bilbo` within keyring `fellowship` and location
`us-east1`:

```
gcloud kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=bilbo --ekm-connection-key-path=v0/some/key/path
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to describe.

**FLAGS**

: **--ekm-connection-key-path**:
The path to the external key material on the EKM for keys with protection level
"external-vpc".

**--external-key-uri**:
The URI of the external key for keys with protection level "external".

**--key**:
The containing key.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--state**:
State of the key version.

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
gcloud alpha kms keys versions update
```

```
gcloud beta kms keys versions update
```