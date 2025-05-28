# gcloud kms keys versions import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import)*

**NAME**

: **gcloud kms keys versions import - import a version into an existing crypto key**

**SYNOPSIS**

: **`gcloud kms keys versions import` `[--algorithm](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--algorithm)`=`ALGORITHM` `[--import-job](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--import-job)`=`IMPORT_JOB` [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--location)`=`LOCATION`] [`[--public-key-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--public-key-file)`=`PUBLIC_KEY_FILE`] [`[--target-key-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--target-key-file)`=`TARGET_KEY_FILE`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--version)`=`VERSION`] [`[--wrapped-key-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#--wrapped-key-file)`=`WRAPPED_KEY_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Imports wrapped key material into a new version within an existing crypto key
following the import procedure documented at [https://cloud.google.com/kms/docs/importing-a-key](https://cloud.google.com/kms/docs/importing-a-key).

**EXAMPLES**

: The following command will read the files 'path/to/ephemeral/key' and
'path/to/target/key' and use them to create a new version with algorithm
'google-symmetric-encryption' within the 'frodo' crypto key, 'fellowship'
keyring, and 'us-central1' location using import job 'strider' to unwrap the
provided key material.

```
gcloud kms keys versions import --location=global --keyring=fellowship --key=frodo --import-job=strider --wrapped-key-file=path/to/target/key --algorithm=google-symmetric-encryption
```

**REQUIRED FLAGS**

: **--algorithm**:
The algorithm to assign to the new key version. For more information about
supported algorithms, see [https://cloud.google.com/kms/docs/algorithms](https://cloud.google.com/kms/docs/algorithms).
`ALGORITHM` must be one of: `aes-128-cbc`,
`aes-128-ctr`, `aes-128-gcm`, `aes-256-cbc`,
`aes-256-ctr`, `aes-256-gcm`,
`ec-sign-ed25519`, `ec-sign-p256-sha256`,
`ec-sign-p384-sha384`, `ec-sign-secp256k1-sha256`,
`google-symmetric-encryption`, `hmac-sha1`,
`hmac-sha224`, `hmac-sha256`, `hmac-sha384`,
`hmac-sha512`, `pq-sign-ml-dsa-65`,
`pq-sign-slh-dsa-sha2-128s`, `rsa-decrypt-oaep-2048-sha1`,
`rsa-decrypt-oaep-2048-sha256`,
`rsa-decrypt-oaep-3072-sha1`,
`rsa-decrypt-oaep-3072-sha256`,
`rsa-decrypt-oaep-4096-sha1`,
`rsa-decrypt-oaep-4096-sha256`,
`rsa-decrypt-oaep-4096-sha512`,
`rsa-sign-pkcs1-2048-sha256`,
`rsa-sign-pkcs1-3072-sha256`,
`rsa-sign-pkcs1-4096-sha256`,
`rsa-sign-pkcs1-4096-sha512`, `rsa-sign-pss-2048-sha256`,
`rsa-sign-pss-3072-sha256`, `rsa-sign-pss-4096-sha256`,
`rsa-sign-pss-4096-sha512`, `rsa-sign-raw-pkcs1-2048`,
`rsa-sign-raw-pkcs1-3072`, `rsa-sign-raw-pkcs1-4096`.

**--import-job**:
Name of the import job to import from.

**OPTIONAL FLAGS**

: **--key**:
The containing key to import into.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

**--public-key-file**:
Path to the public key of the ImportJob, used to wrap the key for import. If
missing, the public key will be fetched on your behalf.

**--target-key-file**:
Path to the unwrapped target key to import into a Cloud KMS key version. If
specified, the key will be securely wrapped before transmission to Google.

**--version**:
Version to re-import into. Omit this field for first-time import.

**--wrapped-key-file**:
Path to the RSA/RSA+AES wrapped key file to import.

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
gcloud alpha kms keys versions import
```

```
gcloud beta kms keys versions import
```