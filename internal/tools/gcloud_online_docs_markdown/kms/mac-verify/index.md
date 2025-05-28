# gcloud kms mac-verify  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify)*

**NAME**

: **gcloud kms mac-verify - verify a user signature file using a MAC key version**

**SYNOPSIS**

: **`gcloud kms mac-verify` `[--input-file](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--input-file)`=`INPUT_FILE` `[--signature-file](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--signature-file)`=`SIGNATURE_FILE` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--skip-integrity-verification)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/mac-verify#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Verifies a digital signature using the provided MAC signing key version.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use --skip-integrity-verification to disable integrity
verification.

**EXAMPLES**

: The following command will read the file '/tmp/my/file.to.verify', and verify it
using the symmetric MAC CryptoKey `dont-panic` Version 3 and the file
used previously to generate the MAC tag ('/tmp/my/original.data.file').

```
gcloud kms mac-verify --location=us-central1 --keyring=hitchhiker --key=dont-panic --version=3 --input-file=/tmp/my/original.data.file --signature-file=/tmp/my/file.to.verify
```

**REQUIRED FLAGS**

: **--input-file**:
Path to the input file to use for verification.

**--signature-file**:
Path to the signature file to be verified.

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
gcloud alpha kms mac-verify
```

```
gcloud beta kms mac-verify
```