# gcloud alloydb users set-roles  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles)*

**NAME**

: **gcloud alloydb users set-roles - update an AlloyDB user's database roles within a given cluster and region**

**SYNOPSIS**

: **`gcloud alloydb users set-roles` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#USERNAME)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#--cluster)`=`CLUSTER` `[--db-roles](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#--db-roles)`=[`ROLE`,…] `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#--region)`=`REGION` [`[--keep-extra-roles](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#--keep-extra-roles)`=`KEEP_EXTRA_ROLES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an AlloyDB user's database roles within a given cluster and region.

**EXAMPLES**

: To update a user's database roles, run:

```
gcloud alloydb users set-roles my-username --cluster=my-cluster --region=us-central1 --db-roles=role1,role2
```

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
AlloyDB username

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--db-roles**:
Comma separated list of database roles this new user will be granted upon
creation.

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--keep-extra-roles**:
If the user already exists and has extra roles, keep them.

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
gcloud alpha alloydb users set-roles
```

```
gcloud beta alloydb users set-roles
```