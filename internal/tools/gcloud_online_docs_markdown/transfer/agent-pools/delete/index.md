# gcloud transfer agent-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/delete](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/delete)*

**NAME**

: **gcloud transfer agent-pools delete - delete a Transfer Service agent pool**

**SYNOPSIS**

: **`gcloud transfer agent-pools delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/delete#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an agent pool. Note that before you can delete a pool, all the pool's
agents must be stopped, its associated jobs must be disabled, and there must be
no associated in-progress transfer operations.

**EXAMPLES**

: To delete agent pool 'foo', run:

```
gcloud transfer agent-pools delete foo
```

To check if there are active operations associated with a pool before deleting
it, scroll through the results of:

```
gcloud transfer operations list --format=yaml --operation-statuses=in_progress
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the job you want to delete.

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

: This variant is also available:

```
gcloud alpha transfer agent-pools delete
```