# gcloud alpha alloydb users create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create)*

**NAME**

: **gcloud alpha alloydb users create - creates a user in a given cluster**

**SYNOPSIS**

: **`gcloud alpha alloydb users create` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#USERNAME)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--region)`=`REGION` [`[--db-roles](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--db-roles)`=[`ROLE`,…]] [`[--keep-extra-roles](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--keep-extra-roles)`=`KEEP_EXTRA_ROLES`] [`[--password](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--password)`=`PASSWORD`] [`[--superuser](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--superuser)`=`SUPERUSER`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#--type)`=`TYPE`; default=`"BUILT_IN"`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Creates a user in a given cluster with specified username,
cluster, region, type, and password.

**EXAMPLES**

: To create a new user, run:

```
gcloud alpha alloydb users create my-username --cluster=my-cluster --region=us-central1 --password=postgres
```

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
AlloyDB username

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--db-roles**:
Comma separated list of database roles this new user will be granted upon
creation.

**--keep-extra-roles**:
If the user already exists and has extra roles, keep them.

**--password**:
Password for this database user.

**--superuser**:
If true, new user will have AlloyDB superuser privileges. Default value is
false.

**--type**:
Type corresponds to the user type. `TYPE` must be one of:

**`BUILT_IN`**:
This database user can authenticate via password-based authentication

**`IAM_BASED`**:
This database user can authenticate via IAM-based authentication

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
gcloud alloydb users create
```

```
gcloud beta alloydb users create
```