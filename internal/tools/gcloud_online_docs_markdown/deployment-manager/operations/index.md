# gcloud deployment-manager operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations)*

**NAME**

: **gcloud deployment-manager operations - commands for Deployment Manager operations**

**SYNOPSIS**

: **`gcloud deployment-manager operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commands to list, examine, and wait for long-running operations.

**EXAMPLES**

: To view the details of an operation, run:

```
gcloud deployment-manager operations describe operation-name
```

To see the list of all operations, run:

```
gcloud deployment-manager operations list
```

To wait for an operation to complete, run:

```
gcloud deployment-manager operations wait operation-name
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/describe)`**:
Provide information about an operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/list)`**:
List operations in a project.

**`[wait](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations/wait)`**:
Wait for all operations specified to complete before returning.

**NOTES**

: These variants are also available:

```
gcloud alpha deployment-manager operations
```

```
gcloud beta deployment-manager operations
```