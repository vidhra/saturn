# gcloud kms keys versions create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create)*

**NAME**

: **gcloud kms keys versions create - create a new version**

**SYNOPSIS**

: **`gcloud kms keys versions create` [`[--ekm-connection-key-path](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--ekm-connection-key-path)`=`EKM_CONNECTION_KEY_PATH`] [`[--external-key-uri](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--external-key-uri)`=`EXTERNAL_KEY_URI`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--location)`=`LOCATION`] [`[--primary](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#--primary)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new version within the given key.

**EXAMPLES**

: The following command creates a new version within the `frodo` key,
`fellowship` keyring, and `global` location and sets it as
the primary version:

```
gcloud kms keys versions create --location=global --keyring=fellowship --key=frodo --primary
```

The following command creates a new version within the `legolas` key,
`fellowship` keyring, `us-central1` location,
`https://example.kms/v0/some/key/path` as the address for its
external key, and sets it as the key's primary version:

```
gcloud kms keys versions create --location=us-central1 --keyring=fellowship --key=legolas --external-key-uri=https://example.kms/v0/some/key/path --primary
```

The following command creates a new version within the `bilbo` key,
`fellowship` keyring, `us-central1` location,
`v0/some/key/path` as the ekm connection key path for its external
key, and sets it as the key's primary version:

```
gcloud kms keys versions create --location=us-central1 --keyring=fellowship --key=bilbo --ekm-connection-key-path=v0/some/key/path --primary
```

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

**--primary**:
If specified, immediately makes the new version primary. This should only be
used with the `encryption` purpose.

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
gcloud alpha kms keys versions create
```

```
gcloud beta kms keys versions create
```