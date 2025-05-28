# gcloud kms raw-encrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt)*

**NAME**

: **gcloud kms raw-encrypt - encrypt a plaintext file using a raw key**

**SYNOPSIS**

: **`gcloud kms raw-encrypt` `[--ciphertext-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--ciphertext-file)`=`CIPHERTEXT_FILE` `[--plaintext-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--plaintext-file)`=`PLAINTEXT_FILE` `[--version](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--version)`=`VERSION` [`[--additional-authenticated-data-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--additional-authenticated-data-file)`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`[--initialization-vector-file](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--initialization-vector-file)`=`INITIALIZATION_VECTOR_FILE`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--location)`=`LOCATION`] [`[--skip-integrity-verification](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#--skip-integrity-verification)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Encrypts the given plaintext file using the given CryptoKey containing a raw key
and writes the result to the named ciphertext file. The plaintext file must not
be larger than 64KiB. For the AES-CBC algorithms, no server-side padding is
being done, so the plaintext must be a multiple of the block size.
The supported algorithms are: `AES-128-GCM`,
`AES-256-GCM`, `AES-128-CBC`, `AES-256-CBC`,
`AES-128-CTR`, `and AES-256-CTR`.
`AES-GCM` provides authentication which means that it accepts
additional authenticated data (AAD). So, the flag
`--additional-authenticated-data-file` is only valid with
`AES-128-GCM` and `AES-256-GCM` algorithms.
The initialization vector (flag `--initialization-vector-file`) is
only supported for `AES-CBC` and `AES-CTR` algorithms, and
must be 16B in length.
Therefore, both additional authenticated data and initialization vector can't be
provided during encryption. If an additional authenticated data file is
provided, its contents must also be provided during decryption. The file must
not be larger than 64KiB.
The flag `--version` indicates the version of the key to use for
encryption.
If `--plaintext-file` or
`--additional-authenticated-data-file` or
`--initialization-vector-file` is set to '-', that file is read from
stdin. Similarly, if `--ciphertext-file` is set to '-', the
ciphertext is written to stdout.
By default, the command performs integrity verification on data sent to and
received from Cloud KMS. Use `--skip-integrity-verification` to
disable integrity verification.

**EXAMPLES**

: The following command reads and encrypts the file
`path/to/input/plaintext`. The file will be encrypted using the
`AES-GCM` CryptoKey `KEYNAME` from the KeyRing
`KEYRING` in the `global` location using the additional
authenticated data file `path/to/input/aad`. The resulting ciphertext
will be written to `path/to/output/ciphertext`.

```
gcloud kms raw-encrypt --key=KEYNAME --keyring=KEYRING --location=global --plaintext-file=path/to/input/plaintext --additional-authenticated-data-file=path/to/input/aad --ciphertext-file=path/to/output/ciphertext
```

The following command reads and encrypts the file
`path/to/input/plaintext`. The file will be encrypted using the
`AES-CBC` CryptoKey `KEYNAME` from the KeyRing
`KEYRING` in the `global` location using the
initialization vector stored at `path/to/input/aad`. The resulting
ciphertext will be written to `path/to/output/ciphertext`.

```
gcloud kms raw-encrypt --key=KEYNAME --keyring=KEYRING --location=global --plaintext-file=path/to/input/plaintext --initialization-vector-file=path/to/input/iv --ciphertext-file=path/to/output/ciphertext
```

**REQUIRED FLAGS**

: **--ciphertext-file**:
File path of the ciphertext file to output.

**--plaintext-file**:
File path of the plaintext file to encrypt.

**--version**:
Version to use for encryption.

**OPTIONAL FLAGS**

: **--additional-authenticated-data-file**:
File path to the optional file containing the additional authenticated data.

**--initialization-vector-file**:
File path to the optional file containing the initialization vector for
encryption.

**--key**:
The key to use for encryption.

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
gcloud alpha kms raw-encrypt
```

```
gcloud beta kms raw-encrypt
```