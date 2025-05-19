# gcloud alloydb instances restart  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart)*

**NAME**

: **gcloud alloydb instances restart - restarts an AlloyDB instance within a given cluster**

**SYNOPSIS**

: **`gcloud alloydb instances restart` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#INSTANCE)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#--region)`=`REGION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#--async)`] [`[--node-ids](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#--node-ids)`=[`NODE_IDS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/restart#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restarts an AlloyDB instance within a given cluster.

**EXAMPLES**

: To restart an instance, run:

```
gcloud alloydb instances restart my-instance --cluster=my-cluster --region=us-central1
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

**--node-ids**:
Comma-separated list of node IDs. Only supported for read pool instances. (e.g.,
`--node-ids=node-1,node-2,node-3`)

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
gcloud alpha alloydb instances restart
```

```
gcloud beta alloydb instances restart
```