# gcloud kms keys versions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe)*

**NAME**

: **gcloud kms keys versions describe - get metadata for a given version**

**SYNOPSIS**

: **`gcloud kms keys versions describe` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#VERSION)` [`[--attestation-file](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#--attestation-file)`=`ATTESTATION_FILE`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#--key)`=`KEY`] [`[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#--keyring)`=`KEYRING`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/versions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns metadata for the given version.
The optional flag `attestation-file` specifies file to write the
attestation object into. The attestation object enables the user to verify the
integrity and provenance of the key. See [https://cloud.google.com/kms/docs/attest-key](https://cloud.google.com/kms/docs/attest-key)
for more information about attestations.

**EXAMPLES**

: The following command returns metadata for version 2 within key
`frodo` within the keyring `fellowship` in the location
`us-east1`:

```
gcloud kms keys versions describe 2 --key=frodo --keyring=fellowship --location=us-east1
```

For key versions with protection level `HSM`, use the
`--attestation-file` flag to save the attestation to a local file.

```
gcloud kms keys versions describe 2 --key=frodo --keyring=fellowship --location=us-east1 --attestation-file=path/to/attestation.dat
```

**POSITIONAL ARGUMENTS**

: **`VERSION`**:
Name of the version to describe.

**FLAGS**

: **--attestation-file**:
Path to the output attestation file.

**--key**:
The containing key.

**--keyring**:
Key ring of the key.

**--location**:
Location of the keyring.

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
gcloud alpha kms keys versions describe
```

```
gcloud beta kms keys versions describe
```