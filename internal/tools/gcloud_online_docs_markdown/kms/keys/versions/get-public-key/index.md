# gcloud kms keys versions get-public-key  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key)*

**NAME**

: **gcloud kms keys versions get-public-key - get the public key for a given version**

**SYNOPSIS**

: **`gcloud kms keys versions get-public-key` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#VERSION)` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#--location)`=`LOCATION`] [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#--output-file)`=`OUTPUT_FILE`] [`[--public-key-format](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#--public-key-format)`=`PUBLIC_KEY_FORMAT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns the public key of the given asymmetric key version in the specified
format.
The optional flag `output-file` indicates the path to store the
public key. If not specified, the public key will be printed to stdout.
The optional flag `public-key-format` indicates the format in which
the public key will be returned. For the PQC algorithms, this must be specified
and set to `nist-pqc`. For all other algorithms, this flag is
optional and defaults to `pem`. See "Retrieve a public key" in the
Cloud KMS documentation (https://cloud.google.com/kms/docs/retrieve-public-key)
for more information about the supported formats.

**EXAMPLES**

: The following command saves the public key for CryptoKey `frodo`
Version 2 to '/tmp/my/public_key.file':

```
gcloud kms keys versions get-public-key 2 --key=frodo --keyring=fellowship --location=us-east1 --public-key-format=pem --output-file=/tmp/my/public_key.file
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to get public key.

**FLAGS**

: **--key**:
The containing key.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--output-file**:
Path to the output file to store public key.

**--public-key-format**:
The format in which the public key will be returned.

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
gcloud alpha kms keys versions get-public-key
```

```
gcloud beta kms keys versions get-public-key
```