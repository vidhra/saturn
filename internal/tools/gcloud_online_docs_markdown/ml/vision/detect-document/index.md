# gcloud ml vision detect-document  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document)*

**NAME**

: **gcloud ml vision detect-document - detect dense text in an image**

**SYNOPSIS**

: **`gcloud ml vision detect-document` `[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document#IMAGE_PATH)` [`[--language-hints](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document#--language-hints)`=[`LANGUAGE_HINTS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detect dense text in an image, such as books and research reports.
Google Cloud Vision uses OCR (Optical Character Recognition) to analyze text.
This is a premium feature for dense text such as books, research reports, and
PDFs. To detect small amounts of text such as on signs, use
`detect-text` instead. For more information on this feature, see the
Google Cloud Vision documentation at [https://cloud.google.com/vision/docs/](https://cloud.google.com/vision/docs/).
Language hints can be provided to Google Cloud Vision API. In most cases, an
empty value yields the best results since it enables automatic language
detection. For languages based on the Latin alphabet, setting
`language_hints` is not needed. Text detection returns an error if
one or more of the specified languages is not one of the supported languages.
(See https://cloud.google.com/vision/docs/languages.) To provide language hints
run:

```
gcloud ml vision detect-document --language-hints ja,ko
```

**EXAMPLES**

: To detect dense text in image 'gs://my_bucket/input_file':

```
gcloud ml vision detect-document gs://my_bucket/input_file
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
gcloud alpha ml vision detect-document
```

```
gcloud beta ml vision detect-document
```