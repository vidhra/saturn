# gcloud ml-engine versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions)*

**NAME**

: **gcloud ml-engine versions - AI Platform Versions commands**

**SYNOPSIS**

: **`gcloud ml-engine versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A version is an implementation of a model, represented as a serialized
TensorFlow graph with trained parameters.
When you communicate with AI Platform services, you use the combination of the
model, version, and current project to identify a specific model implementation
that is deployed in the cloud.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/create)`**:
Create a new AI Platform version.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/delete)`**:
Delete an existing AI Platform version.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/describe)`**:
Describe an existing AI Platform version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/list)`**:
List existing AI Platform versions.

**`[set-default](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/set-default)`**:
Sets an existing AI Platform version as the default for its model.

**`[update](https://cloud.google.com/sdk/gcloud/reference/ml-engine/versions/update)`**:
Update an AI Platform version.

**NOTES**

: These variants are also available:

```
gcloud alpha ml-engine versions
```

```
gcloud beta ml-engine versions
```