# gcloud firebase test ios locales describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales/describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales/describe)*

**NAME**

: **gcloud firebase test ios locales describe - describe an iOS locale**

**SYNOPSIS**

: **`gcloud firebase test ios locales describe` `[LOCALE](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales/describe#LOCALE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an iOS locale.

**EXAMPLES**

: To describe an iOS locale, run:

```
gcloud firebase test ios locales describe es_419
```

To describe an iOS locale in JSON format, run:

```
gcloud firebase test ios locales describe es_419 --format=json
```

**POSITIONAL ARGUMENTS**

: **`LOCALE`**:
The locale to describe, found using $ [gcloud firebase test
ios locales list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales/list).

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

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test ios locales describe
```

```
gcloud beta firebase test ios locales describe
```