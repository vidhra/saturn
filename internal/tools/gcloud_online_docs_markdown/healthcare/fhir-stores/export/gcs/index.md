# gcloud healthcare fhir-stores export gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs)*

**NAME**

: **gcloud healthcare fhir-stores export gcs - export Cloud Healthcare API FHIR resources to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud healthcare fhir-stores export gcs` (`[FHIR_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#FHIR_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--location)`=`LOCATION`) `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--gcs-uri)`=`GCS_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--async)`] [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--resource-type)`=`RESOURCE_TYPE`] [`[--since](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#--since)`=`SINCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export Cloud Healthcare API FHIR resources to Google Cloud Storage.

**EXAMPLES**

: To export the fhir-store 'test-fhir-store' to the existing bucket
'testGcsBucket' in the folder 'someFolder', run:

```
gcloud healthcare fhir-stores export gcs test-fhir-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **FhirStore resource - Cloud Healthcare API FHIR store to export resources from.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

: **--gcs-uri**:
The Cloud Storage destination location. Specify a path to a Cloud Storage bucket
or folder rather than a concrete object. The exported outputs are organized by
FHIR resource types. The server will create one object per resource type. Each
object contains newline delimited JSON, and each line is a FHIR resource.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--resource-type**:
String of comma-delimited FHIR resource types. If provided, only resources of
the specified resource type(s) are exported.

**--since**:
If provided, only resources updated after this time are exported. The time uses
the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example,
2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z. The time must be
specified to the second and include a time zone.

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
gcloud alpha healthcare fhir-stores export gcs
```

```
gcloud beta healthcare fhir-stores export gcs
```