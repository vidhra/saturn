# gcloud ml vision suggest-crop  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/vision/suggest-crop](https://cloud.google.com/sdk/gcloud/reference/ml/vision/suggest-crop)*

**NAME**

: **gcloud ml vision suggest-crop - suggest a bounding box in an image**

**SYNOPSIS**

: **`gcloud ml vision suggest-crop` `[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/vision/suggest-crop#IMAGE_PATH)` [`[--aspect-ratios](https://cloud.google.com/sdk/gcloud/reference/ml/vision/suggest-crop#--aspect-ratios)`=[`ASPECT_RATIOS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/vision/suggest-crop#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Returns the coordinates of a bounding box that surrounds the dominant object or
face in an image.

**EXAMPLES**

: To get the coordinates of a bounding box that surrounds the dominant object or
face in an image `gs://my_bucket/input_file`:

```
gcloud ml vision suggest-crop gs://my_bucket/input_file
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_PATH`**:
Path to the image to be analyzed. This can be either a local path or a URL. If
you provide a local file, the contents will be sent directly to Google Cloud
Vision. If you provide a URL, it must be in Google Cloud Storage format
(gs://bucket/object) or an HTTP URL ([http://..](http://..). or
https://…)

**FLAGS**

: **--aspect-ratios**:
A list of aspect ratio hints for the suggested bounding box. Aspect ratios may
be specified either as a decimal number (ex. 1.333) or as a ratio of width to
height (ex 4:3).

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
gcloud alpha ml vision suggest-crop
```

```
gcloud beta ml vision suggest-crop
```