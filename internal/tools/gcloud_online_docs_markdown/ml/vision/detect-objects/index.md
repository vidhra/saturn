# gcloud ml vision detect-objects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-objects](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-objects)*

**NAME**

: **gcloud ml vision detect-objects - detect and extract multiple objects in an image with object localization**

**SYNOPSIS**

: **`gcloud ml vision detect-objects` `[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-objects#IMAGE_PATH)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-objects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detect and extract multiple objects in an image with object localization.
Object localization identifies multiple objects in an image and provides a
LocalizedObjectAnnotation for each object in the image.

**EXAMPLES**

: To detect objects for image 'gs://my_bucket/input_file':

```
gcloud ml vision detect-objects gs://my_bucket/input_file
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_PATH`**:
Path to the image to be analyzed. This can be either a local path or a URL. If
you provide a local file, the contents will be sent directly to Google Cloud
Vision. If you provide a URL, it must be in Google Cloud Storage format
(gs://bucket/object) or an HTTP URL ([http://..](http://..). or
https://…)

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
gcloud alpha ml vision detect-objects
```

```
gcloud beta ml vision detect-objects
```