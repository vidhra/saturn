# gcloud ml vision detect-text-tiff  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff)*

**NAME**

: **gcloud ml vision detect-text-tiff - detect and transcribe text from TIFF files stored in Google Cloud Storage**

**SYNOPSIS**

: **`gcloud ml vision detect-text-tiff` `[INPUT_FILE](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff#INPUT_FILE)` `[OUTPUT_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff#OUTPUT_PATH)` [`[--batch-size](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff#--batch-size)`=`BATCH_SIZE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-tiff#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detect and transcribe text from TIFF files stored in Google Cloud Storage.
The Vision API accepts TIFF files up to 2000 pages. Larger files will return an
error.

**EXAMPLES**

: To detect text for input TIFF file `gs://my_bucket/input_file` and
store output in `gs://my_bucket/out_put_prefix`:

```
gcloud ml vision detect-text-tiff gs://my_bucket/input_file gs://my_bucket/out_put_prefix
```

**POSITIONAL ARGUMENTS**

: **`INPUT_FILE`**:
Google Cloud Storage location to read the input from. It must be in Google Cloud
Storage format (gs://bucket/object)

**`OUTPUT_PATH`**:
Google Cloud Storage location to store the output file. It must be in Google
Cloud Storage format (gs://bucket/object)

**FLAGS**

: **--batch-size**:
Maximum number of response protos to put into each output JSON file on Google
Cloud Storage. The valid range is [1, 100]. If not specified, the default value
is 20.

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

: This command uses the `vision/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/vision/](https://cloud.google.com/vision/)

**NOTES**

: These variants are also available:

```
gcloud alpha ml vision detect-text-tiff
```

```
gcloud beta ml vision detect-text-tiff
```