# gcloud kms decrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt)*

**NAME**

: **gcloud kms decrypt - decrypt a ciphertext file using a Cloud KMS key**

**SYNOPSIS**

: **`gcloud kms decrypt` `[--ciphertext-file](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--ciphertext-file)`=`CIPHERTEXT_FILE` `[--plaintext-file](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--plaintext-file)`=`PLAINTEXT_FILE` [`[--additional-authenticated-data-file](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--additional-authenticated-data-file)`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#--skip-integrity-verification)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud kms decrypt` decrypts the given ciphertext file using the
given Cloud KMS key and writes the result to the named plaintext file. Note that
to permit users to decrypt using a key, they must be have at least one of the
following IAM roles for that key:
`roles/cloudkms.cryptoKeyDecrypter`,
`roles/cloudkms.cryptoKeyEncrypterDecrypter`.
Additional authenticated data (AAD) is used as an additional check by Cloud KMS
to authenticate a decryption request. If an additional authenticated data file
is provided, its contents must match the additional authenticated data provided
during encryption and must not be larger than 64KiB. If you don't provide a
value for `--additional-authenticated-data-file`, an empty string is
used. For a thorough explanation of AAD, refer to this guide: [https://cloud.google.com/kms/docs/additional-authenticated-data](https://cloud.google.com/kms/docs/additional-authenticated-data)
If `--ciphertext-file` or
`--additional-authenticated-data-file` is set to '-', that file is
read from stdin. Note that both files cannot be read from stdin. Similarly, if
`--plaintext-file` is set to '-', the decrypted plaintext is written
to stdout.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: To decrypt the file 'path/to/ciphertext' using the key `frodo` with
key ring `fellowship` and location `global` and write the
plaintext to 'path/to/plaintext.dec', run:

```
gcloud kms decrypt --key=frodo --keyring=fellowship --location=global --ciphertext-file=path/to/input/ciphertext --plaintext-file=path/to/output/plaintext.dec
```

To decrypt the file 'path/to/ciphertext' using the key `frodo` and
the additional authenticated data that was used to encrypt the ciphertext, and
write the decrypted plaintext to stdout, run:

```
gcloud kms decrypt --key=frodo --keyring=fellowship --location=global --additional-authenticated-data-file=path/to/aad --ciphertext-file=path/to/input/ciphertext --plaintext-file='-'
```

**REQUIRED FLAGS**

: **--ciphertext-file**:
File path of the ciphertext file to decrypt. This file should contain the result
of encrypting a file with `[gcloud kms encrypt](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt)`.

**--plaintext-file**:
File path of the plaintext file to output.

**OPTIONAL FLAGS**

: **--additional-authenticated-data-file**:
File path to the optional file containing the additional authenticated data.

**--key**:
Cloud KMS key to use for decryption.

- For symmetric keys, Cloud KMS detects the decryption key version from the
ciphertext. If you specify a key version as part of a symmetric decryption
request, an error is logged and decryption fails.
- For asymmetric keys, the encryption key version can't be detected automatically.
You must keep track of this information and provide the key version in the
decryption request. The key version itself is not sensitive data and does not
need to be encrypted.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--skip-integrity-verification**:
Skip integrity verification on request and response API fields.

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
gcloud alpha kms decrypt
```

```
gcloud beta kms decrypt
```