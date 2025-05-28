# gcloud logging scopes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create)*

**NAME**

: **gcloud logging scopes create - create a log scope**

**SYNOPSIS**

: **`gcloud logging scopes create` `[LOG_SCOPE_ID](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#LOG_SCOPE_ID)` `[--resource-names](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#--resource-names)`=[`RESOURCE_NAMES`,…] [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#--description)`=`DESCRIPTION`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: After creating a log scope, you can use it to view logs in 1 or more resources.

**EXAMPLES**

: To create a log scope in a project, run:

```
gcloud logging scopes create my-scope --resource-names=projects/my-project
```

To create a log scope in a project with a description, run:

```
gcloud logging scopes create my-scope --resource-names=projects/my-project --description="my
custom log scope"
```

To create a log scope that contains more than 1 resource, such as projects and
views, run:

```
gcloud logging scopes create my-scope --resource-names=projects/my-project,projects/my-project2, projects/my-project/locations/global/buckets/my-bucket/views/my-view1, projects/my-project/locations/global/buckets/my-bucket/views/my-view2,
```

**POSITIONAL ARGUMENTS**

: **`LOG_SCOPE_ID`**:
ID of the log scope to create.

**REQUIRED FLAGS**

: **--resource-names**:
Comma-separated list of resource names in this log scope. It could be one or
more parent resources or one or more views. A log scope can include a maximum of
50 projects and a maximum of 100 resources in total. For example,
projects/[PROJECT_ID],
projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]``

**OPTIONAL FLAGS**

: **--description**:
A textual description for the log scope.

**--folder**

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