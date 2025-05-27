# gcloud dataproc operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/operations](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations)*

**NAME**

: **gcloud dataproc operations - view and manage Dataproc operations**

**SYNOPSIS**

: **`gcloud dataproc operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: View and manage Dataproc operations.

**EXAMPLES**

: To cancel an active operation, run:

```
gcloud dataproc operations cancel operation_id
```

To view the details of an operation, run:

```
gcloud dataproc operations describe operation_id
```

To see the list of all operations, run:

```
gcloud dataproc operations list
```

To delete the record of an inactive operation, run:

```
gcloud dataproc operations delete operation_id
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/cancel)`**:
Cancel an active operation.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/delete)`**:
Delete the record of an inactive operation.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/describe)`**:
View the details of an operation.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/get-iam-policy)`**:
Get IAM policy for an operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/list)`**:
View the list of all operations.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations/set-iam-policy)`**:
Set IAM policy for an operation.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc operations
```

```
gcloud beta dataproc operations
```