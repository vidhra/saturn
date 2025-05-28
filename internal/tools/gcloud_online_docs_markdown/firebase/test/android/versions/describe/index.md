# gcloud firebase test android versions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe)*

**NAME**

: **gcloud firebase test android versions describe - describe an Android OS version**

**SYNOPSIS**

: **`gcloud firebase test android versions describe` `[VERSION_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe#VERSION_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Android OS version.

**EXAMPLES**

: To see attributes of the Android OS version 'my-version', run:

```
gcloud firebase test android versions describe my-version
```

**POSITIONAL ARGUMENTS**

: **`VERSION_ID`**:
The version ID to describe, found using $ [gcloud firebase
test android versions list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/list).

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
gcloud alpha firebase test android versions describe
```

```
gcloud beta firebase test android versions describe
```