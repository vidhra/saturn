# gcloud alloydb instances failover  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover)*

**NAME**

: **gcloud alloydb instances failover - failover an AlloyDB instance within a given cluster**

**SYNOPSIS**

: **`gcloud alloydb instances failover` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover#INSTANCE)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Failover an AlloyDB instance within a given cluster.

**EXAMPLES**

: To failover an instance, run:

```
gcloud alloydb instances failover my-instance --cluster=my-cluster --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
AlloyDB instance ID

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha alloydb instances failover
```

```
gcloud beta alloydb instances failover
```