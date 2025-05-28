# gcloud alpha ai-platform models create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create)*

**NAME**

: **gcloud alpha ai-platform models create - create a new AI Platform model**

**SYNOPSIS**

: **`gcloud alpha ai-platform models create` `[MODEL](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#MODEL)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--description)`=`DESCRIPTION`] [`[--enable-console-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--enable-console-logging)`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--enable-logging)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--region)`=`REGION`     | `[--regions](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#--regions)`=`REGION`,[`[REGION](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#REGION)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new AI Platform model.

**POSITIONAL ARGUMENTS**

: **`MODEL`**:
Name of the model.

**FLAGS**

: **--description**:
Description of the model.

**--enable-console-logging**:
If set, enables StackDriver Logging of stderr and stdout streams for online
prediction. These logs are more verbose than the standard access logs and can be
helpful for debugging.

**--enable-logging**:
If set, enables StackDriver Logging for online prediction. These logs are like
standard server access logs, containing information such as timestamps and
latency for each request.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--region**

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
gcloud ai-platform models create
```

```
gcloud beta ai-platform models create
```