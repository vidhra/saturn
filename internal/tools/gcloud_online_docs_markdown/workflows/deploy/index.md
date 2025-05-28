# gcloud workflows deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workflows/deploy](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy)*

**NAME**

: **gcloud workflows deploy - create or update a workflow**

**SYNOPSIS**

: **`gcloud workflows deploy` (`[WORKFLOW](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#WORKFLOW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--async)`] [`[--call-log-level](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--call-log-level)`=`CALL_LOG_LEVEL`; default="none"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--description)`=`DESCRIPTION`] [`[--execution-history-level](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--execution-history-level)`=`EXECUTION_HISTORY_LEVEL`; default="none"] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--labels)`=[`KEY`=`VALUE`,…]] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--service-account)`=`SERVICE_ACCOUNT`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--source)`=`SOURCE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#--tags)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workflows/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create or update a workflow.

**EXAMPLES**

: To deploy a workflow with source code myWorkflow.yaml on Workflows:

```
gcloud workflows deploy my-workflow --source=myWorkflow.yaml
```

You may also skip waiting for the operation to finish:

```
gcloud workflows deploy my-workflow --source=myWorkflow.yaml --async
```

To specify a service account as the workflow identity:

```
gcloud workflows deploy my-workflow --source=myWorkflow.yaml --service-account=my-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **Workflow resource - Name of the workflow to deploy. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKFLOW`**:
ID of the workflow or fully qualified identifier for the workflow.
To set the `workflow` attribute:

- provide the argument `workflow` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Cloud location for the workflow. Alternatively, set the property
[workflows/location].
To set the `location` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `workflows/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--call-log-level**:
Level of call logging to apply by default for the workflow.
`CALL_LOG_LEVEL` must be one of:

**`log-all-calls`**:
Log all calls to subworkflows or library functions and their results.

**`log-errors-only`**:
Log when a call is stopped due to an exception.

**`log-none`**:
Perform no call logging.

**`none`**:
No logging level specified.

**--description**:
The description of the workflow to deploy.

**--execution-history-level**:
Level of execution history to apply for the workflow.
`EXECUTION_HISTORY_LEVEL` must be one of:

**`execution-history-basic`**:
Enable basic execution history.

**`execution-history-detailed`**:
Enable detailed execution history, including expected iterations and in-scope
variable values.

**`none`**:
No execution history level specified.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--service-account**:
The service account that should be used as the workflow identity.
"projects/PROJECT_ID/serviceAccounts/" prefix may be skipped from the full
resource name, in that case "projects/-/serviceAccounts/" is prepended to the
service account ID.

**--source**:
Location of a workflow source code to deploy. Required on first deployment.
Location needs to be defined as a path to a local file with the source code.

**--tags**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
"<tag-key-namespaced-name>=<tag-value-short-name>".
Example: 123/environment=production,123/costCenter=marketing

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

: This variant is also available:

```
gcloud beta workflows deploy
```