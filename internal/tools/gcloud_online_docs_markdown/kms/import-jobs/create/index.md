# gcloud kms import-jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create)*

**NAME**

: **gcloud kms import-jobs create - create a new import job**

**SYNOPSIS**

: **`gcloud kms import-jobs create` `[IMPORT_JOB](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#IMPORT_JOB)` `[--import-method](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#--import-method)`=`IMPORT_METHOD` `[--protection-level](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#--protection-level)`=`PROTECTION_LEVEL` [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new import job within the given keyring.

**EXAMPLES**

: The following command creates a new import job named 'strider' within the
'fellowship' keyring, and 'us-central1' location:

```
gcloud kms import-jobs create strider --location=us-central1 --keyring=fellowship --import-method=rsa-oaep-3072-sha256-aes-256 --protection-level=hsm
```

**POSITIONAL ARGUMENTS**

: **`IMPORT_JOB`**:
Name of the import job to create.

**REQUIRED FLAGS**

: **--import-method**:
The wrapping method to be used for incoming key material. For more information
about choosing an import method, see [https://cloud.google.com/kms/docs/key-wrapping](https://cloud.google.com/kms/docs/key-wrapping).
`IMPORT_METHOD` must be one of:
`rsa-oaep-3072-sha1-aes-256`, `rsa-oaep-3072-sha256`,
`rsa-oaep-3072-sha256-aes-256`,
`rsa-oaep-4096-sha1-aes-256`, `rsa-oaep-4096-sha256`,
`rsa-oaep-4096-sha256-aes-256`.

**--protection-level**:
Protection level of the import job. `PROTECTION_LEVEL`
must be one of: `software`, `hsm`.

**OPTIONAL FLAGS**

: **--keyring**:
Key ring of the import job.

**--location**:
Location of the import job.

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
gcloud alpha kms import-jobs create
```

```
gcloud beta kms import-jobs create
```