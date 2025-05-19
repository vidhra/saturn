# gcloud alloydb clusters upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade)*

**NAME**

: **gcloud alloydb clusters upgrade - upgrade an AlloyDB cluster within a given project and region**

**SYNOPSIS**

: **`gcloud alloydb clusters upgrade` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade#CLUSTER)` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade#--region)`=`REGION` `[--version](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade#--version)`=`VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upgrade an AlloyDB cluster within a given project and region.

**EXAMPLES**

: To upgrade a cluster, run:

```
gcloud alloydb clusters upgrade my-cluster --region=us-central1 --version=POSTGRES_15
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**--version**:
Target database version for the upgrade. `VERSION` must be
one of: `POSTGRES_14`, `POSTGRES_15`,
`POSTGRES_16`.

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
gcloud alpha alloydb clusters upgrade
```

```
gcloud beta alloydb clusters upgrade
```