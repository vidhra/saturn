# gcloud logging scopes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update)*

**NAME**

: **gcloud logging scopes update - update a log scope**

**SYNOPSIS**

: **`gcloud logging scopes update` `[LOG_SCOPE_ID](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update#LOG_SCOPE_ID)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update#--description)`=`DESCRIPTION`] [`[--resource-names](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update#--resource-names)`=[`RESOURCE_NAMES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the properties of a log scope.

**EXAMPLES**

: To update the description of a log scope in a project, run:

```
gcloud logging scopes update my-scope --description=my-new-description --project=my-project
```

To update the resource name of a log scope in a project. Ensure that you provide
all the resource names including the existing ones. For example, if the log
scope has the resource name my-project, and you want to update the log scope to
have the resource name another-project, run the following:

```
gcloud logging scopes update my-scope --resource-names=projects/my-project,projects/another-project --project=my-project
```

**POSITIONAL ARGUMENTS**

: **`LOG_SCOPE_ID`**:
The ID of the log scope to update.

**FLAGS**

: **--description**:
A new description for the log scope.

**--resource-names**:
A new set of resource names for the log scope.

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