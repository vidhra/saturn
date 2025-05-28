# gcloud firebase test android models  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models)*

**NAME**

: **gcloud firebase test android models - explore Android models available in the Test Environment catalog**

**SYNOPSIS**

: **`gcloud firebase test android models` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore Android models available in the Test Environment catalog.

**EXAMPLES**

: To list all Android models available for running tests, along with their basic
characteristics and supported Android OS versions, run:

```
gcloud firebase test android models list
```

To view more detailed information about a specific Android model, run:

```
gcloud firebase test android models describe MODEL_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/describe)`**:
Describe an Android model.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/list)`**:
List all Android models available for testing.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test android models
```

```
gcloud beta firebase test android models
```