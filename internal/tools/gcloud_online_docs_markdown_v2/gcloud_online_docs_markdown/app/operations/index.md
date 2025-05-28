# gcloud app operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/operations](https://cloud.google.com/sdk/gcloud/reference/app/operations)*

**NAME**

: **gcloud app operations - view and manage your App Engine Operations**

**SYNOPSIS**

: **`gcloud app operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/operations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing App Engine
operations.

**EXAMPLES**

: To list your App Engine operations, run:

```
gcloud app operations list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/app/operations/describe)`**:
Describes the operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/app/operations/list)`**:
List the operations.

**`[wait](https://cloud.google.com/sdk/gcloud/reference/app/operations/wait)`**:
Polls an operation until completion.

**NOTES**

: This variant is also available:

```
gcloud beta app operations
```