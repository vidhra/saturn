# gcloud healthcare dicom-stores import gcs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs)*

**NAME**

: **gcloud healthcare dicom-stores import gcs - import DICOM objects into a Cloud Healthcare API DICOM store**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores import gcs` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#--location)`=`LOCATION`) `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#--gcs-uri)`=`GCS_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import DICOM objects into a Cloud Healthcare API DICOM store.

**EXAMPLES**

: To import the DICOM objects from the existing bucket 'testGcsBucket' in the
folder 'someFolder' into the DICOM store 'test-dicom-store', run:

```
gcloud healthcare dicom-stores import gcs test-dicom-store --gcs-uri="gs://testGcsBucket/someFolder/*" --dataset=test-dataset
```

Note that '`' matches any files within a folder, and '**' also recursively
matches files within sub-folders.`

**POSITIONAL ARGUMENTS**

: **DicomStore resource - Cloud Healthcare API DICOM store into which the data is
imported. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DICOM_STORE`**:
ID of the dicomStore or fully qualified identifier for the dicomStore.
To set the `dicom_store` attribute:

- provide the argument `dicom_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--gcs-uri**:
Google Cloud Storage URI containing DICOM object data. It must match individual
DICOM files or use wildcards to import multiple files from one or more
directories.

- Use * to match 0 or more non-separator characters. For example,
`gs://BUCKET/DIRECTORY/Example*.dcm` matches Example.dcm and
Example22.dcm in DIRECTORY.
- Use ** to match 0 or more characters (including separators). Must be used at the
end of a path and with no other wildcards in the path. Can also be used with a
filename extension (such as .dcm), which imports all files with the filename
extension in the specified directory and its subdirectories. For example,
gs://BUCKET/DIRECTORY/**.dcm imports all files with the .dcm filename extension
in DIRECTORY and its subdirectories.
- Use ? to match 1 character. For example, gs://BUCKET/DIRECTORY/Example?.dcm
matches Example1.dcm but does not match Example.dcm or Example01.dcm.

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
gcloud alpha healthcare dicom-stores import gcs
```

```
gcloud beta healthcare dicom-stores import gcs
```