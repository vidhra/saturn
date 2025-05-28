# gcloud artifacts rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create)*

**NAME**

: **gcloud artifacts rules create - create an Artifact Registry rule**

**SYNOPSIS**

: **`gcloud artifacts rules create` (`[RULE](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--repository)`=`REPOSITORY`) `[--action](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--action)`=`ACTION` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--condition)`=`CONDITION`] [`[--operation](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--operation)`=`OPERATION`; default="DOWNLOAD"] [`[--package](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#--package)`=`PACKAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Artifact Registry rule.
This command can fail for the following reasons:

- A rule with the same name already exists.
- The active account does not have permission to create repositories.
- A rule with given package already exists.

**EXAMPLES**

: To create a rule with the name `my-rule` for package
`my-pkg` with action deny under the current project, repository, run:

```
gcloud artifacts rules create my-rule --package=my-pkg --action=deny
```

**POSITIONAL ARGUMENTS**

: **Rule resource - The Artifact Registry rule to create. The arguments in this
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

**REQUIRED FLAGS**

: **--action**:
The action the rule would make, can only be DENY or ALLOW.
`ACTION` must be one of: `allow`,
`deny`.

**OPTIONAL FLAGS**

: **--condition**:
The CEL expression for the rule.

**--operation**:
The operation the rule applies to. `OPERATION` must be
(only one value is supported): `download`.

**--package**:
The package the rule applies to. Empty means the rule is set for the entire
repository.

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