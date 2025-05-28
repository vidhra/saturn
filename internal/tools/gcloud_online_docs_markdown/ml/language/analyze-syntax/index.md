# gcloud ml language analyze-syntax  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax)*

**NAME**

: **gcloud ml language analyze-syntax - use Google Cloud Natural Language API to identify linguistic information**

**SYNOPSIS**

: **`gcloud ml language analyze-syntax` (`[--content](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#--content)`=`CONTENT`     | `[--content-file](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#--content-file)`=`CONTENT_FILE`) [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#--content-type)`=`CONTENT_TYPE`; default="plain-text"] [`[--encoding-type](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#--encoding-type)`=`ENCODING_TYPE`; default="utf8"] [`[--language](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#--language)`=`LANGUAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Syntactic Analysis extracts linguistic information, breaking up the given text
into a series of sentences and tokens (generally, word boundaries), providing
further analysis on those tokens.
Currently English, Spanish, and Japanese are supported.

**EXAMPLES**

: To analyze syntax in raw content 'They drink.':

```
gcloud ml language analyze-syntax --content='They drink'
```

To analyze syntax in file 'myfile.txt':

```
gcloud ml language analyze-syntax --content-file='myfile.txt'
```

To analyze syntax in a remote file 'gs://bucket_name/mycontent.html' for
Japanese language using UTF-8 encoding:

```
gcloud ml language analyze-syntax --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --encoding-type=utf8 --language=ja-JP
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
gcloud alpha ml language analyze-syntax
```

```
gcloud beta ml language analyze-syntax
```