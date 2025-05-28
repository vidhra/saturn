# gcloud kms mac-sign  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign)*

**NAME**

: **gcloud kms mac-sign - sign a user input file using a MAC key version**

**SYNOPSIS**

: **`gcloud kms mac-sign` `[--input-file](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--input-file)`=`INPUT_FILE` `[--signature-file](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--signature-file)`=`SIGNATURE_FILE` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--skip-integrity-verification)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/mac-sign#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a digital signature of the input file using the provided MAC signing key
version and saves the base64 encoded signature.
The required flag `signature-file` indicates the path to store
signature.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use --skip-integrity-verification to disable integrity
verification.

**EXAMPLES**

: The following command will read the file '/tmp/my/file.to.sign', and sign it
using the symmetric MAC CryptoKey `dont-panic` Version 3, and save
the signature in base64 format to '/tmp/my/signature'.

```
gcloud kms mac-sign --location=us-central1 --keyring=hitchhiker --key=dont-panic --version=3 --input-file=/tmp/my/file.to.sign --signature-file=/tmp/my/signature
```

**REQUIRED FLAGS**

: **--input-file**:
Path to the input file to sign.

**--signature-file**:
Path to the signature file to output.

**OPTIONAL FLAGS**

: **--key**:
to use for signing.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--skip-integrity-verification**:
Skip integrity verification on request and response API fields.

**--version**:
Version to use for signing.

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
gcloud alpha kms mac-sign
```

```
gcloud beta kms mac-sign
```