# gcloud kms keys versions get-certificate-chain  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain)*

**NAME**

: **gcloud kms keys versions get-certificate-chain - get a certificate chain for a given version**

**SYNOPSIS**

: **`gcloud kms keys versions get-certificate-chain` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#VERSION)` [`[--certificate-chain-type](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#--certificate-chain-type)`=`CERTIFICATE_CHAIN_TYPE`; default="all"] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#--location)`=`LOCATION`] [`[--output-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#--output-file)`=`OUTPUT_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-certificate-chain#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns the PEM-format certificate chain for the specified key version. The
optional flag `output-file` indicates the path to store the PEM. If
not specified, the PEM will be printed to stdout.

**EXAMPLES**

: The following command saves the Cavium certificate chain for CryptoKey
``frodo`` Version 2 to
``/tmp/my/cavium.pem``:

```
gcloud kms keys versions get-certificate-chain 2 --key=frodo --keyring=fellowship --location=us-east1 --certificate-chain-type=cavium --output-file=/tmp/my/cavium.pem
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version from which to get the certificate chain.

**FLAGS**

: **--certificate-chain-type**:
Certificate chain to retrieve. `CERTIFICATE_CHAIN_TYPE`
must be one of: `all`, `cavium`, `google-card`,
`google-partition`.

**--key**:
The containing key.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--output-file**:
Path to the output file to store PEM.

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
gcloud alpha kms keys versions get-certificate-chain
```

```
gcloud beta kms keys versions get-certificate-chain
```