# gcloud healthcare hl7v2-stores export gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs)*

**NAME**

: **gcloud healthcare hl7v2-stores export gcs - export Cloud Healthcare API HL7v2 messages to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud healthcare hl7v2-stores export gcs` (`[HL7V2_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#HL7V2_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--location)`=`LOCATION`) `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--gcs-uri)`=`GCS_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--async)`] [`[--end-time](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--end-time)`=`END_TIME`] [`[--message-view](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--message-view)`=`MESSAGE_VIEW`] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#--start-time)`=`START_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/export/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export Cloud Healthcare API HL7v2 messages to Google Cloud Storage.

**EXAMPLES**

: To export the hl7v2-store 'test-hl7v2-store' to the existing bucket
'testGcsBucket' in the folder 'someFolder', run:

```
gcloud healthcare hl7v2-stores export gcs test-hl7v2-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset
```

To perform the same export, but exporting messages with the message view of
'RAW_ONLY', run:

```
gcloud healthcare hl7v2-stores export gcs test-hl7v2-store --gcs-uri=gs://testGcsBucket/someFolder --dataset=test-dataset --message-view=RAW_ONLY
```

**POSITIONAL ARGUMENTS**

: **Hl7v2Store resource - Cloud Healthcare API HL7v2 store to export messages from.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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
The Cloud Storage destination location. Specify a path to a Cloud Storage bucket
or folder rather than a concrete object. The exported messages are ordered by
the message send_time (MSH.7) in ascending order. The server will create one or
more objects. Each object contains newline delimited JSON, and each line is an
HL7v2 message.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--end-time**:
The end of the range in message send_time (MSH.7) to process. If not specified,
the time when the export is scheduled is used.

**--message-view**:
Specifies the parts of the Message resource to include in the export. The
default is FULL. `MESSAGE_VIEW` must be one of:

**`basic`**:
Exported resources include only the name field.

**`full`**:
Exported resources include all the message fields.

**`parsed-only`**:
Exported resources include all the message fields except data and
schematizedData fields.

**`raw-only`**:
Exported resources include all the message fields except parsedData and
schematizedData fields.

**`schematized-only`**:
Exported resources include all the message fields except data and parsedData
fields.

**--start-time**:
The start of the range in message send_time (MSH.7) to process. If not
specified, the UNIX epoch (1970-01-01T00:00:00Z) is used.

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
gcloud alpha healthcare hl7v2-stores export gcs
```

```
gcloud beta healthcare hl7v2-stores export gcs
```