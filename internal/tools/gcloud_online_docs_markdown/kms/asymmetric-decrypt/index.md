# gcloud kms asymmetric-decrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt)*

**NAME**

: **gcloud kms asymmetric-decrypt - decrypt an input file using an asymmetric-encryption key version**

**SYNOPSIS**

: **`gcloud kms asymmetric-decrypt` `[--ciphertext-file](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--ciphertext-file)`=`CIPHERTEXT_FILE` `[--plaintext-file](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--plaintext-file)`=`PLAINTEXT_FILE` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--skip-integrity-verification)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Decrypts the given ciphertext file using the provided asymmetric-encryption key
version and saves the decrypted data to the plaintext file.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: The following command will read the file '/tmp/my/secret.file.enc', decrypt it
using the asymmetric CryptoKey `dont-panic` Version 3 and write the
plaintext to '/tmp/my/secret.file.dec'.

```
gcloud kms asymmetric-decrypt --location=us-central1 --keyring=hitchhiker --key=dont-panic --version=3 --ciphertext-file=/tmp/my/secret.file.enc --plaintext-file=/tmp/my/secret.file.dec
```

**REQUIRED FLAGS**

: **--ciphertext-file**:
File path of the ciphertext file to decrypt.

**--plaintext-file**:
File path of the plaintext file to output.

**OPTIONAL FLAGS**

: **--key**:
to use for asymmetric-decryption.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--skip-integrity-verification**:
Skip integrity verification on request and response API fields.

**--version**:
Version to use for asymmetric-decryption.

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
gcloud alpha kms asymmetric-decrypt
```

```
gcloud beta kms asymmetric-decrypt
```