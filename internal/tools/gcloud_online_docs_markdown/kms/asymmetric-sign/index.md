# gcloud kms asymmetric-sign  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign)*

**NAME**

: **gcloud kms asymmetric-sign - sign a user input file using an asymmetric-signing key version**

**SYNOPSIS**

: **`gcloud kms asymmetric-sign` `[--input-file](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--input-file)`=`INPUT_FILE` `[--signature-file](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--signature-file)`=`SIGNATURE_FILE` [`[--digest-algorithm](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--digest-algorithm)`=`DIGEST_ALGORITHM`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--skip-integrity-verification)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a digital signature of the input file using the provided
asymmetric-signing key version and saves the base64 encoded signature.
The required flag `signature-file` indicates the path to store
signature.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: The following command will read the file '/tmp/my/file.to.sign', digest it with
the digest algorithm 'sha256' and sign it using the asymmetric CryptoKey
`dont-panic` Version 3, and save the signature in base64 format to
'/tmp/my/signature'.

```
gcloud kms asymmetric-sign --location=us-central1 --keyring=hitchhiker --key=dont-panic --version=3 --digest-algorithm=sha256 --input-file=/tmp/my/file.to.sign --signature-file=/tmp/my/signature
```

**REQUIRED FLAGS**

: **--input-file**:
Path to the input file to sign.

**--signature-file**:
Path to the signature file to output.

**OPTIONAL FLAGS**

: **--digest-algorithm**:
The algorithm to digest the input. `DIGEST_ALGORITHM` must
be one of: `sha256`, `sha384`, `sha512`.

**--key**:
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
gcloud alpha kms asymmetric-sign
```

```
gcloud beta kms asymmetric-sign
```