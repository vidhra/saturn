# gcloud healthcare fhir-stores deidentify  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify)*

**NAME**

: **gcloud healthcare fhir-stores deidentify - de-identify data from the source store and write it to the destination store**

**SYNOPSIS**

: **`gcloud healthcare fhir-stores deidentify` (`[FHIR_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#FHIR_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#--location)`=`LOCATION`) `[--destination-store](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#--destination-store)`=`DESTINATION_STORE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/deidentify#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: De-identify data from the source store and write it to the destination store.

**EXAMPLES**

: To generate a de-identified version of the FHIR store 'test-fhir-store', run the
command below.

```
gcloud healthcare fhir-stores deidentify test-fhir-store --destination-store=projects/{projectId}/locations/us-central1/datasets/{datasetId}/fhirStores/test-deid-fhir-store
```

**POSITIONAL ARGUMENTS**

: **FhirStore resource - Source Cloud Healthcare API FHIR store to deidentify. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FHIR_STORE`**:
ID of the fhirStore or fully qualified identifier for the fhirStore.
To set the `fhir_store` attribute:

- provide the argument `fhir_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--destination-store**:
The name of the FHIR store to which the redacted data should be written (e.g.,
projects/{projectId}/locations/{locationId}/datasets/{datasetId}/fhirStores/{fhirStoreId}).
The destination FHIR store must already exist, or the request will fail.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare fhir-stores deidentify
```

```
gcloud beta healthcare fhir-stores deidentify
```