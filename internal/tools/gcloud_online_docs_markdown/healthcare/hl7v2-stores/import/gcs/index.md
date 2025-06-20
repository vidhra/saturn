# gcloud healthcare hl7v2-stores import gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs)*

**NAME**

: **gcloud healthcare hl7v2-stores import gcs - import HL7v2 messages from Google Cloud Storage into a Cloud Healthcare API HL7v2 store**

**SYNOPSIS**

: **`gcloud healthcare hl7v2-stores import gcs` (`[HL7V2_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#HL7V2_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#--location)`=`LOCATION`) `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#--gcs-uri)`=`GCS_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/import/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import HL7v2 messages from Google Cloud Storage into a Cloud Healthcare API
HL7v2 store.

**EXAMPLES**

: To import the HL7v2 messages from the existing bucket 'testGcsBucket' in the
folder 'someFolder' into the HL7v2 store 'test-hl7v2-store', run:

```
gcloud healthcare hl7v2-stores import gcs test-hl7v2-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **Hl7v2Store resource - Cloud Healthcare API HL7v2 store into which the data is
imported. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HL7V2_STORE`**:
ID of the hl7v2Store or fully qualified identifier for the hl7v2Store.
To set the `hl7v2_store` attribute:

- provide the argument `hl7v2_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `hl7v2_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--gcs-uri**:
Cloud Storage source data locations. Each Cloud Storage object should be a text
file that contains newline-delimited JSON objects. Each JSON object has a data
field that contains a base64-encoded HL7v2 message.

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
gcloud alpha healthcare hl7v2-stores import gcs
```

```
gcloud beta healthcare hl7v2-stores import gcs
```