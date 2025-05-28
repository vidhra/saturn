# gcloud firebase test ios models  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models)*

**NAME**

: **gcloud firebase test ios models - explore iOS models available in the Test Environment catalog**

**SYNOPSIS**

: **`gcloud firebase test ios models` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore iOS models available in the Test Environment catalog.

**EXAMPLES**

: To list all iOS models available for running tests, along with their model names
and supported iOS versions, run:

```
gcloud firebase test ios models list
```

To view information about a single iOS model, run:

```
gcloud firebase test ios models describe MODEL_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/describe)`**:
Describe an iOS model.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models/list)`**:
List all iOS models available for testing.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test ios models
```

```
gcloud beta firebase test ios models
```