# gcloud alpha batch resource-allowances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update)*

**NAME**

: **gcloud alpha batch resource-allowances update - update a Batch resource allowance**

**SYNOPSIS**

: **`gcloud alpha batch resource-allowances update` (`[RESOURCE_ALLOWANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update#RESOURCE_ALLOWANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update#--location)`=`LOCATION`) [`[--usage-limit](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update#--usage-limit)`=`USAGE_LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command updates a Batch resource allowance.

**EXAMPLES**

: The following command updates a resource allowance limit to 0
`projects/foo/locations/us-central1/resousrceAllowances/bar`:

```
gcloud alpha batch resource-allowances update projects/foo/locations/us-central1/resousrceAllowances/bar --usage-limit 0
```

**POSITIONAL ARGUMENTS**

: **ResourceAllowance resource - The Batch resource allowance resource. If
--location not specified,the current batch/location is used. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RESOURCE_ALLOWANCE`**:
ID of the resourceAllowance or fully qualified identifier for the
resourceAllowance.
To set the `resource_allowance` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the resourceAllowance.
To set the `location` attribute:

- provide the argument `RESOURCE_ALLOWANCE` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `batch/location`.**

**FLAGS**

: **--usage-limit**:
Limit value of a UsageResourceAllowance within its one duration. Limit cannot be
a negative value. Default is 0.

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