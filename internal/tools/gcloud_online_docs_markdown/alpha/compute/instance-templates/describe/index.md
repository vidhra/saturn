# gcloud alpha compute instance-templates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe)*

**NAME**

: **gcloud alpha compute instance-templates describe - describe a virtual machine instance template**

**SYNOPSIS**

: **`gcloud alpha compute instance-templates describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe#NAME)` [`[--view](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe#--view)`=`VIEW`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-templates
describe` displays all data associated with a Google Compute Engine
virtual machine instance template.

**EXAMPLES**

: To describe the instance template named 'INSTANCE-TEMPLATE', run:

```
gcloud alpha compute instance-templates describe INSTANCE-TEMPLATE
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance template to describe.

**FLAGS**

: **--view**:
Specifies the information that the output should contain.
`VIEW` must be one of:

**`BASIC`**:
Default output view. Output contains all configuration details of the instance
template, except partner metadata.

**`FULL`**:
Output contains all configuration details of the instance template, including
partner metadata.

**--global**

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
gcloud compute instance-templates describe
```

```
gcloud beta compute instance-templates describe
```