# gcloud artifacts rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete)*

**NAME**

: **gcloud artifacts rules delete - delete an Artifact Registry rule**

**SYNOPSIS**

: **`gcloud artifacts rules delete` (`[RULE](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete#RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete#--repository)`=`REPOSITORY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Artifact Registry rule.
This command can fail for the following reasons:

- The specified rule does not exist.
- The active account does not have permission to delete rules.

**EXAMPLES**

: To delete a rule named `my-rule` under the current project,
repository, and location, run:

```
gcloud artifacts rules delete my-repo
```

**POSITIONAL ARGUMENTS**

: **Rule resource - The Artifact Registry rule to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `rule` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RULE`**:
ID of the rule or fully qualified identifier for the rule.
To set the `rule` attribute:

- provide the argument `rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the rule. Overrides the default artifacts/location property value
for this command invocation. To configure the default location, use the command:
gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `rule` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
The repository associated with the rule. Overrides the default
artifacts/repository property value for this command invocation. To configure
the default repository, use the command: gcloud config set artifacts/repository.
To set the `repository` attribute:

- provide the argument `rule` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

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

**API REFERENCE**

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)