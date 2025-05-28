# gcloud ml language analyze-entities  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities)*

**NAME**

: **gcloud ml language analyze-entities - use Google Cloud Natural Language API to identify entities in text**

**SYNOPSIS**

: **`gcloud ml language analyze-entities` (`[--content](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#--content)`=`CONTENT`     | `[--content-file](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#--content-file)`=`CONTENT_FILE`) [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#--content-type)`=`CONTENT_TYPE`; default="plain-text"] [`[--encoding-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#--encoding-type)`=`ENCODING_TYPE`; default="utf8"] [`[--language](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#--language)`=`LANGUAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entities#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Entity Analysis inspects the given text for common names or known entities
(proper nouns such as public figures, landmarks, etc.), and returns information
about those entities.
Currently English, Spanish, and Japanese are supported.

**EXAMPLES**

: To analyze entites in raw content 'puppies':

```
gcloud ml language analyze-entities --content='puppies'
```

To analyze entites in file 'myfile.txt':

```
gcloud ml language analyze-entities --content-file='myfile.txt'
```

To analyze entites in a remote file 'gs://bucket_name/mycontent.html' for
Japanese language using UTF-8 encoding:

```
gcloud ml language analyze-entities --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --encoding-type=utf8 --language=ja-JP
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
gcloud alpha ml language analyze-entities
```

```
gcloud beta ml language analyze-entities
```