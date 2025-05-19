# gcloud alpha batch resource-allowances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create)*

**NAME**

: **gcloud alpha batch resource-allowances create - create a Batch resource allowance**

**SYNOPSIS**

: **`gcloud alpha batch resource-allowances create` [[`[RESOURCE_ALLOWANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create#RESOURCE_ALLOWANCE)`] `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create#--location)`=`LOCATION`] `[--config](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create#--config)`=`PATH_TO_FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command creates a Batch resource allowance.

**EXAMPLES**

: The following command submit a resource allowance with config.json sample config
file `projects/foo/locations/us-central1/resousrceAllowances/bar`:

```
gcloud alpha batch resource-allowances create projects/foo/locations/us-central1/resousrceAllowances/bar --config config.json
```

**POSITIONAL ARGUMENTS**

: **ResourceAllowance resource - The Batch resource allowance resource. If
--location not specified,the current batch/location is used. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line with a
fully specified name;
- resource allowance ID is optional and will be generated if not specified with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`RESOURCE_ALLOWANCE`]**:
ID of the resourceAllowance or fully qualified identifier for the
resourceAllowance.
To set the `resource_allowance` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line;
- resource allowance ID is optional and will be generated if not specified.

**--location**:
Google Cloud location for the resourceAllowance.
To set the `location` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line with a
fully specified name;
- resource allowance ID is optional and will be generated if not specified with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `batch/location`.**

**REQUIRED FLAGS**

: **--config**:
The config file of a resource allowance. Use a full or relative path to a local
file containing the value of config.

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