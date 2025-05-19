# gcloud alpha alloydb instances describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe)*

**NAME**

: **gcloud alpha alloydb instances describe - describes an AlloyDB instance within a given cluster**

**SYNOPSIS**

: **`gcloud alpha alloydb instances describe` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe#INSTANCE)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe#--region)`=`REGION` [`[--view](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe#--view)`=`VIEW`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describes an AlloyDB instance within a given cluster.

**EXAMPLES**

: To describe an instance, run:

```
gcloud alpha alloydb instances describe my-instance --cluster=my-cluster --region=us-central1 --view=BASIC/FULL
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

: **--view**:
View of the instance to return. `VIEW` must be one of:
`basic`, `full`.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb instances describe
```

```
gcloud beta alloydb instances describe
```