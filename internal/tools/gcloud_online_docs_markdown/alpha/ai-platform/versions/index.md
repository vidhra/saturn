# gcloud alpha ai-platform versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions)*

**NAME**

: **gcloud alpha ai-platform versions - AI Platform Versions commands**

**SYNOPSIS**

: **`gcloud alpha ai-platform versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` A version is an implementation of a model, represented as a
serialized TensorFlow graph with trained parameters.
When you communicate with AI Platform services, you use the combination of the
model, version, and current project to identify a specific model implementation
that is deployed in the cloud.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create)`**:
`(ALPHA)` Create a new AI Platform version.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/delete)`**:
`(ALPHA)` Delete an existing AI Platform version.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/describe)`**:
`(ALPHA)` Describe an existing AI Platform version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/list)`**:
`(ALPHA)` List existing AI Platform versions.

**`[set-default](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/set-default)`**:
`(ALPHA)` Sets an existing AI Platform version as the default for its
model.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/update)`**:
`(ALPHA)` Update an AI Platform version.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai-platform versions
```

```
gcloud beta ai-platform versions
```