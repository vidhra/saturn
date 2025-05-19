# gcloud alpha artifacts operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/operations](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/operations)*

**NAME**

: **gcloud alpha artifacts operations - manage Artifact Registry long-running operations**

**SYNOPSIS**

: **`gcloud alpha artifacts operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/operations#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To describe a Artifact Registry operation given a valid operation id and
`artifacts/location` property is set, run:

```
gcloud alpha artifacts operations describe 13166c87-a9c0-4b5f-8ccf-c5343a93eb2b
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/operations/describe)`**:
`(ALPHA)` Describe an Artifact Registry operation.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts operations
```

```
gcloud beta artifacts operations
```