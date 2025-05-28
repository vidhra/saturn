# gcloud sql instances switchover  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover)*

**NAME**

: **gcloud sql instances switchover - switches over a Cloud SQL instance to one of its replicas**

**SYNOPSIS**

: **`gcloud sql instances switchover` `[REPLICA](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover#REPLICA)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover#--async)`] [`[--db-timeout](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover#--db-timeout)`=`DB_TIMEOUT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Switches over a Cloud SQL instance to one of its replicas.

**EXAMPLES**

: To switch over an instance to its replica called replica-instance:

```
gcloud sql instances switchover replica-instance
```

**POSITIONAL ARGUMENTS**

: **`REPLICA`**:
Cloud SQL replica ID.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--db-timeout**:
(MySQL and PostgreSQL only) Cloud SQL instance operations timeout, which is the
sum of all database operations. Default value is 10 minutes and can be modified
to a maximum value of 24h.

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
gcloud alpha sql instances switchover
```

```
gcloud beta sql instances switchover
```