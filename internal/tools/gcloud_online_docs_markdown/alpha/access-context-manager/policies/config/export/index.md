# gcloud alpha access-context-manager policies config export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export)*

**NAME**

: **gcloud alpha access-context-manager policies config export - export the configuration for a Access Context Manager access policy**

**SYNOPSIS**

: **`gcloud alpha access-context-manager policies config export` ([`[POLICY](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export#POLICY)`] `[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export#--all)`) [`[--path](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export#--path)`=`PATH`; default="-"] [`[--resource-format](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export#--resource-format)`=`RESOURCE_FORMAT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/policies/config/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha access-context-manager policies config
export` exports the configuration for a Access Context Manager access
policy.
Access policy configurations can be exported in Kubernetes Resource Model (krm)
or Terraform HCL formats. The default format is `krm`.
Specifying `--all` allows you to export the configurations for all
access policies within the project.
Specifying `--path` allows you to export the configuration(s) to a
local directory.

**EXAMPLES**

: To export the configuration for an access policy, run:

```
gcloud alpha access-context-manager policies config export my-access-policy
```

To export the configuration for an access policy to a file, run:

```
gcloud alpha access-context-manager policies config export my-access-policy --path=/path/to/dir/
```

To export the configuration for an access policy in Terraform HCL format, run:

```
gcloud alpha access-context-manager policies config export my-access-policy --resource-format=terraform
```

To export the configurations for all access policies within a project, run:

```
gcloud alpha access-context-manager policies config export --all
```

**POSITIONAL ARGUMENTS**

: **Exactly one of these must be specified:

**[`POLICY`]**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..

**--all**:
Retrieve all resources within the project. If `--path` is specified
and is a valid directory, resources will be output as individual files based on
resource name and scope. If `--path` is not specified, resources will
be streamed to stdout.**

**FLAGS**

: **--path**:
Path of the directory or file to output configuration(s). To output
configurations to stdout, specify "--path=-".

**--resource-format**:
Format of the configuration to export. Available configuration formats are
Kubernetes Resource Model YAML (krm) or Terraform HCL (terraform). Command
defaults to "krm". `RESOURCE_FORMAT` must be one of:
`krm`, `terraform`.

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
allowlist.