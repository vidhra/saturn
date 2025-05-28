# gcloud policy-intelligence query-activity  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity)*

**NAME**

: **gcloud policy-intelligence query-activity - query activities on cloud resource**

**SYNOPSIS**

: **`gcloud policy-intelligence query-activity` `[--activity-type](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#--activity-type)`=`ACTIVITY_TYPE` `[--project](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#--project)`=`PROJECT` [`[--limit](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#--limit)`=`LIMIT`; default=1000] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#--page-size)`=`PAGE_SIZE`; default=500] [`[--query-filter](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#--query-filter)`=`QUERY_FILTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Query activities with certain types of specific container resource. For
--activity-type, supported values are:

- serviceAccountLastAuthentication
- serviceAccountKeyLastAuthentication

**EXAMPLES**

: To query serviceAccountKeyLastAuthentication activities of a project, run:

```
gcloud policy-intelligence query-activity --activity-type=serviceAccountKeyLastAuthentication --project=project-id
```

To query serviceAccountLastAuthentication activities of a project with no limit,
run:

```
gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --limit=unlimited
```

To query serviceAccountLastAuthentication with filtering on certain service
account, run:

```
gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name@project-id.iam.gserviceaccount.com"'
```

To query serviceAccountLastAuthentication with filtering on multiple service
accounts, run:

```
gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-1@project-id.iam.gserviceaccount.com" OR
 activities.full_resource_name="//iam.googleapis.com/projects/projec\
t-id/serviceAccounts/service-account-name-2@project-id.iam.gservicea\
ccount.com" OR
 activities.full_resource_name="//iam.googleapis.com/projects/projec\
t-id/serviceAccounts/service-account-name-3@project-id.iam.gservicea\
ccount.com"'
```

**REQUIRED FLAGS**

: **--activity-type**:
Type of the activities. `ACTIVITY_TYPE` must be one of:
`serviceAccountLastAuthentication`,
`serviceAccountKeyLastAuthentication`.

**--project**:
The project ID or number to query the activities.

**OPTIONAL FLAGS**

: **--limit**:
Max number of query result. Default to be 1000 and max to be unlimited, i.e.,
--limit=unlimited.

**--page-size**:
Max page size for each http response. Default to be 500 and max to be 1000.

**--query-filter**:
Filter on activities, separated by "OR" if multiple filters are specified. At
most 10 filter restrictions are supported in the query-filter. e.g.
--query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-1@project-id.iam.gserviceaccount.com"
OR
activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-2@project-id.iam.gserviceaccount.com"'

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