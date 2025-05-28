# gcloud kms import-jobs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe)*

**NAME**

: **gcloud kms import-jobs describe - get metadata for a given import job**

**SYNOPSIS**

: **`gcloud kms import-jobs describe` `[IMPORT_JOB](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe#IMPORT_JOB)` [`[--attestation-file](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe#--attestation-file)`=`ATTESTATION_FILE`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns metadata for the given import job.
The optional flag `--attestation-file` specifies file to write the
attestation into. The attestation enables the user to verify the integrity and
provenance of the key. See [https://cloud.google.com/kms/docs/attest-key](https://cloud.google.com/kms/docs/attest-key)
for more information about attestations.

**EXAMPLES**

: The following command returns metadata for import job 'strider' within the
keyring 'fellowship' in the location 'us-central1':

```
gcloud kms import-jobs describe strider --keyring=fellowship --location=us-central1
```

For import jobs with protection level `HSM`, use the
`--attestation-file` flag to save the attestation to a local file.

```
gcloud kms import-jobs describe strider --keyring=fellowship --location=us-central1 --attestation-file=path/to/attestation.dat
```

**POSITIONAL ARGUMENTS**

: **`IMPORT_JOB`**:
Name of the import job to describe.

**FLAGS**

: **--attestation-file**:
Path to the output attestation file.

**--keyring**:
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
gcloud alpha kms import-jobs describe
```

```
gcloud beta kms import-jobs describe
```