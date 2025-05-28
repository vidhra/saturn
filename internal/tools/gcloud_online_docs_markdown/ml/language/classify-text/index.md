# gcloud ml language classify-text  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text)*

**NAME**

: **gcloud ml language classify-text - classifies input document into categories**

**SYNOPSIS**

: **`gcloud ml language classify-text` (`[--content](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text#--content)`=`CONTENT`     | `[--content-file](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text#--content-file)`=`CONTENT_FILE`) [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text#--content-type)`=`CONTENT_TYPE`; default="plain-text"] [`[--language](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text#--language)`=`LANGUAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/language/classify-text#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Classifies input document into categories. Returns a list of categories
representing the document. Only the most relevant categories a document are
returned e.g. if `/Science` and `/Science/Astronomy` both
apply to a document, then only the `/Science/Astronomy` category is
returned, as it is the more specific result.
Currently only English is supported for this feature.

**EXAMPLES**

: To classify text in raw content 'Long Political Text.':

```
gcloud ml language classify-text --content='Long Political Text.'
```

To classify text in file 'myfile.txt':

```
gcloud ml language classify-text --content-file='myfile.txt'
```

To classify text in a remote file 'gs://bucket_name/mycontent.html' for Japanese
language:

```
gcloud ml language classify-text --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --language=ja-JP
```

**REQUIRED FLAGS**

: **--content**

**OPTIONAL FLAGS**

: **--content-type**:
Specify the format of the input text. `CONTENT_TYPE` must
be one of: `html`, `plain-text`.

**--language**:
Specify the language of the input text. If omitted, the server will attempt to
auto-detect. Both ISO (such as `en` or `es`) and BCP-47
(such as `en-US` or `ja-JP`) language codes are accepted.

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

: This command uses the `language/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/natural-language/](https://cloud.google.com/natural-language/)

**NOTES**

: These variants are also available:

```
gcloud alpha ml language classify-text
```

```
gcloud beta ml language classify-text
```