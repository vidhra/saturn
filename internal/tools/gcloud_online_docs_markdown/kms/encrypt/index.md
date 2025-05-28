# gcloud kms encrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/encrypt](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt)*

**NAME**

: **gcloud kms encrypt - encrypt a plaintext file using a key**

**SYNOPSIS**

: **`gcloud kms encrypt` `[--ciphertext-file](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--ciphertext-file)`=`CIPHERTEXT_FILE` `[--plaintext-file](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--plaintext-file)`=`PLAINTEXT_FILE` [`[--additional-authenticated-data-file](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--additional-authenticated-data-file)`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--skip-integrity-verification)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/encrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Encrypts the given plaintext file using the given CryptoKey and writes the
result to the named ciphertext file. The plaintext file must not be larger than
64KiB.
If an additional authenticated data file is provided, its contents must also be
provided during decryption. The file must not be larger than 64KiB.
The flag `--version` indicates the version of the key to use for
encryption. By default, the primary version is used.
If `--plaintext-file` or
`--additional-authenticated-data-file` is set to '-', that file is
read from stdin. Similarly, if `--ciphertext-file` is set to '-', the
ciphertext is written to stdout.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: The following command will read the file 'path/to/plaintext', encrypt it using
the CryptoKey `frodo` with the KeyRing `fellowship` and
Location `global`, and write the ciphertext to 'path/to/ciphertext'.

```
gcloud kms encrypt --key=frodo --keyring=fellowship --location=global --plaintext-file=path/to/input/plaintext --ciphertext-file=path/to/output/ciphertext
```

**REQUIRED FLAGS**

: **--ciphertext-file**:
File path of the ciphertext file to output.

**--plaintext-file**:
File path of the plaintext file to encrypt.

**OPTIONAL FLAGS**

: **--additional-authenticated-data-file**:
File path to the optional file containing the additional authenticated data.

**--key**:
The key to use for encryption.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--skip-integrity-verification**:
Skip integrity verification on request and response API fields.

**--version**:
Version to use for encryption.

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
gcloud alpha kms encrypt
```

```
gcloud beta kms encrypt
```