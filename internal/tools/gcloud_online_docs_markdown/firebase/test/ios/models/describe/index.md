# gcloud firebase test ios models describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/describe)*

**NAME**

: **gcloud firebase test ios models describe - describe an iOS model**

**SYNOPSIS**

: **`gcloud firebase test ios models describe` `[MODEL_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/describe#MODEL_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an iOS model.

**EXAMPLES**

: To describe an iOS model, run:

```
gcloud firebase test ios models describe iphone7
```

To describe an iOS model in JSON format, run:

```
gcloud firebase test ios models describe iphone7 --format=json
```

**POSITIONAL ARGUMENTS**

: **`MODEL_ID`**:
ID of the model to describe, found using $ [gcloud firebase test
ios models list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/list).

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
gcloud alpha firebase test ios models describe
```

```
gcloud beta firebase test ios models describe
```