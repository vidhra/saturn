# gcloud alloydb users set-password  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password)*

**NAME**

: **gcloud alloydb users set-password - update an AlloyDB user's password within a given cluster and region**

**SYNOPSIS**

: **`gcloud alloydb users set-password` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password#USERNAME)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password#--cluster)`=`CLUSTER` `[--password](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password#--password)`=`PASSWORD` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password#--region)`=`REGION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an AlloyDB user's password within a given cluster and region.

**EXAMPLES**

: To update a user's password, run:

```
gcloud alloydb users set-password my-username --cluster=my-cluster --region=us-central1 --password=postgres
```

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
AlloyDB username

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--password**:
Password for this database user.

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

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
gcloud alpha alloydb users set-password
```

```
gcloud beta alloydb users set-password
```