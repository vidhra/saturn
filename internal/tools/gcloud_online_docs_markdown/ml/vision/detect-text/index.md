# gcloud ml vision detect-text  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text)*

**NAME**

: **gcloud ml vision detect-text - detect and extract text within an image**

**SYNOPSIS**

: **`gcloud ml vision detect-text` `[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text#IMAGE_PATH)` [`[--language-hints](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text#--language-hints)`=[`LANGUAGE_HINTS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detect and extract text within an image.
Google Cloud Vision uses OCR (Optical Character Recognition) to detect text
within an image, with support for a broad array of languages and automatic label
detection.
Language hints can be provided to Google Cloud Vision API. In most cases, an
empty value yields the best results since it enables automatic language
detection. For languages based on the Latin alphabet, setting
`language_hints` is not needed. Text detection returns an error if
one or more of the specified languages is not one of the supported languages.
(See https://cloud.google.com/vision/docs/languages.) To provide language hints
run:

```
gcloud ml vision detect-text --language-hints ja,ko
```

**EXAMPLES**

: To detect and extract text within an image 'gs://my_bucket/input_file':

```
gcloud ml vision detect-text gs://my_bucket/input_file
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_PATH`**:
Path to the image to be analyzed. This can be either a local path or a URL. If
you provide a local file, the contents will be sent directly to Google Cloud
Vision. If you provide a URL, it must be in Google Cloud Storage format
(gs://bucket/object) or an HTTP URL ([http://..](http://..). or
https://…)

**FLAGS**

: **--language-hints**:
List of languages to use for text detection.

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
gcloud alpha ml vision detect-text
```

```
gcloud beta ml vision detect-text
```