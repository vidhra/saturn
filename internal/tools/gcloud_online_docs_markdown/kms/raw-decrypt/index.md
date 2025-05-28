# gcloud kms raw-decrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt)*

**NAME**

: **gcloud kms raw-decrypt - decrypt a ciphertext file using a raw key**

**SYNOPSIS**

: **`gcloud kms raw-decrypt` `[--ciphertext-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--ciphertext-file)`=`CIPHERTEXT_FILE` `[--plaintext-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--plaintext-file)`=`PLAINTEXT_FILE` `[--version](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--version)`=`VERSION` [`[--additional-authenticated-data-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--additional-authenticated-data-file)`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`[--initialization-vector-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--initialization-vector-file)`=`INITIALIZATION_VECTOR_FILE`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#--skip-integrity-verification)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud kms raw-decrypt` decrypts the given ciphertext file using the
given CryptoKey containing a raw key and writes the result to the named
plaintext file. The ciphertext file must not be larger than 64KiB.
The supported algorithms are: `AES-128-GCM`,
`AES-256-GCM`, `AES-128-CBC`, `AES-256-CBC`,
`AES-128-CTR`, `and AES-256-CTR`.
`AES-GCM` provides authentication which means that it accepts
additional authenticated data (AAD). So, the flag
`--additional-authenticated-data-file` is only valid with
`AES-128-GCM` and `AES-256-GCM` algorithms. If AAD is
provided during encryption, it must be provided during decryption too. The file
must not be larger than 64KiB.
If `--plaintext-file` or
`--additional-authenticated-data-file` or
`--initialization-vector-file` is set to '-', that file is read from
stdin. Similarly, if `--ciphertext-file` is set to '-', the
ciphertext is written to stdout.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: The following command reads and decrypts the file
`path/to/input/ciphertext`. The file will be decrypted using the
CryptoKey `KEYNAME` containing a raw key, from the KeyRing
`KEYRING` in the `global` location. It uses the additional
authenticated data file `path/to/input/aad` (only valid with the
`AES-GCM` algorithms) and the initialization vector file
`path/to/input/iv`. The resulting plaintext will be written to
`path/to/output/plaintext`.

```
gcloud kms raw-decrypt --key=KEYNAME --keyring=KEYRING --location=global --ciphertext-file=path/to/input/ciphertext --additional-authenticated-data-file=path/to/input/aad --initialization-vector-file=path/to/input/iv --plaintext-file=path/to/output/plaintext
```

**REQUIRED FLAGS**

: **--ciphertext-file**:
File path of the ciphertext file to decrypt.

**--plaintext-file**:
File path of the plaintext file to store the decrypted data.

**--version**:
Version to use for decryption.

**OPTIONAL FLAGS**

: **--additional-authenticated-data-file**:
File path to the optional file containing the additional authenticated data.

**--initialization-vector-file**:
File path to the optional file containing the initialization vector for
decryption.

**--key**:
The (raw) key to use for decryption.

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
gcloud alpha kms raw-decrypt
```

```
gcloud beta kms raw-decrypt
```