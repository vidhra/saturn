# gcloud alpha bigtable app-profiles config export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export)*

**NAME**

: **gcloud alpha bigtable app-profiles config export - export the configuration for a Cloud Bigtable app profile**

**SYNOPSIS**

: **`gcloud alpha bigtable app-profiles config export` ([`[APP_PROFILE](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#APP_PROFILE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#--instance)`=`INSTANCE`] `[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#--all)`) [`[--path](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#--path)`=`PATH`; default="-"] [`[--resource-format](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#--resource-format)`=`RESOURCE_FORMAT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/config/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha bigtable app-profiles config
export` exports the configuration for a Cloud Bigtable app profile.
App profile configurations can be exported in Kubernetes Resource Model (krm) or
Terraform HCL formats. The default format is `krm`.
Specifying `--all` allows you to export the configurations for all
app profiles within the project.
Specifying `--path` allows you to export the configuration(s) to a
local directory.

**EXAMPLES**

: To export the configuration for an app profile, run:

```
gcloud alpha bigtable app-profiles config export my-app-profile
```

To export the configuration for an app profile to a file, run:

```
gcloud alpha bigtable app-profiles config export my-app-profile --path=/path/to/dir/
```

To export the configuration for an app profile in Terraform HCL format, run:

```
gcloud alpha bigtable app-profiles config export my-app-profile --resource-format=terraform
```

To export the configurations for all app profiles within a project, run:

```
gcloud alpha bigtable app-profiles config export --all
```

**POSITIONAL ARGUMENTS**

: **Exactly one of these must be specified:

**App profile resource - App profile to export the configuration for. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `app_profile` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**`APP_PROFILE`**:
ID of the app-profile or fully qualified identifier for the app-profile.
To set the `app_profile` attribute:

- provide the argument `app_profile` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `app_profile` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

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