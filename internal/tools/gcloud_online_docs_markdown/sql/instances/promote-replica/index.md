# gcloud sql instances promote-replica  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica)*

**NAME**

: **gcloud sql instances promote-replica - promotes Cloud SQL read replica to a stand-alone instance**

**SYNOPSIS**

: **`gcloud sql instances promote-replica` `[REPLICA](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica#REPLICA)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica#--async)`] [`[--[no-]failover](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica#--[no-]failover)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Promotes Cloud SQL read replica to a stand-alone instance.

**POSITIONAL ARGUMENTS**

: **`REPLICA`**:
Cloud SQL read replica ID.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--[no-]failover**:
Whether the promote operation is a failover. Use `--failover` to
enable and `--no-failover` to disable.

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

: These variants are also available:

```
gcloud alpha sql instances promote-replica
```

```
gcloud beta sql instances promote-replica
```