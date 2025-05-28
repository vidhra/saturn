# gcloud ml language analyze-entity-sentiment  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment)*

**NAME**

: **gcloud ml language analyze-entity-sentiment - use Google Cloud Natural Language API to identify entity-level sentiment**

**SYNOPSIS**

: **`gcloud ml language analyze-entity-sentiment` (`[--content](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#--content)`=`CONTENT`     | `[--content-file](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#--content-file)`=`CONTENT_FILE`) [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#--content-type)`=`CONTENT_TYPE`; default="plain-text"] [`[--encoding-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#--encoding-type)`=`ENCODING_TYPE`; default="utf8"] [`[--language](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#--language)`=`LANGUAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Entity level sentiment combines both entity analysis and sentiment analysis and
attempts to determine the sentiment (positive or negative) expressed about
entities within the text.
Currently only English is supported for this feature.

**EXAMPLES**

: To analyze entity sentiment in raw content 'puppies':

```
gcloud ml language analyze-entity-sentiment --content='puppies'
```

To analyze entity sentiment in file 'myfile.txt':

```
gcloud ml language analyze-entity-sentiment --content-file='myfile.txt'
```

To analyze entity sentiment in a remote file 'gs://bucket_name/mycontent.html'
for Japanese language using UTF-8 encoding:

```
gcloud ml language analyze-entity-sentiment --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --encoding-type=utf8 --language=ja-JP
```

**REQUIRED FLAGS**

: **--content**

**OPTIONAL FLAGS**

: **--content-type**:
Specify the format of the input text. `CONTENT_TYPE` must
be one of: `html`, `plain-text`.

**--encoding-type**:
The encoding type used by the API to calculate offsets. If set to
`none`, encoding-dependent offsets will be set at -1. This is an
optional flag only used for the entity mentions in results, and does not affect
how the input is read or analyzed. `ENCODING_TYPE` must be
one of: `none`, `utf16`, `utf32`,
`utf8`.

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
gcloud alpha ml language analyze-entity-sentiment
```

```
gcloud beta ml language analyze-entity-sentiment
```