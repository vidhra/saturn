# gcloud looker operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/operations](https://cloud.google.com/sdk/gcloud/reference/looker/operations)*

**NAME**

: **gcloud looker operations - manage Looker operations**

**SYNOPSIS**

: **`gcloud looker operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/looker/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/operations#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To display the details for an operation with name `my-looker-op`,
run:

```
gcloud looker operations describe my-looker-op
```

To list all the operations, run:

```
gcloud looker operations list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/looker/operations/cancel)`**:
Cancel a Looker import or export operation.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/looker/operations/describe)`**:
Show metadata for a Looker operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/looker/operations/list)`**:
List Looker operations.

**NOTES**

: This variant is also available:

```
gcloud alpha looker operations
```