# gcloud scc operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/operations/describe](https://cloud.google.com/sdk/gcloud/reference/scc/operations/describe)*

**NAME**

: **gcloud scc operations describe - describe a Cloud SCC's long running scan operation**

**SYNOPSIS**

: **`gcloud scc operations describe` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/scc/operations/describe#OPERATION)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/operations/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud SCC's long running scan operation.

**EXAMPLES**

: Return long running scan operation status for operation id
(9c5fa5e5-e368-439a-baa4-08c17b77ec23) and organization 123456. Operation id is
obtained using run-discovery command:

```
gcloud scc operations describe 9c5fa5e5-e368-439a-baa4-08c17b77ec23 --organization=123456
```

**POSITIONAL ARGUMENTS**

: **Operation resource - Cloud SCC's API operation to describe. The arguments in
this group can be used to specify the attributes of this resource.
This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
(Optional) If the full resource name isn't provided e.g. organizations/123, then
provide the organization id which is the suffix of the organization. Example:
organizations/123, the id is 123.
To set the `organization` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line;
- Set the organization property in configuration using `gcloud config set
scc/organization` if it is not specified in command line..**

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

: This command uses the `securitycenter/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: These variants are also available:

```
gcloud alpha scc operations describe
```

```
gcloud beta scc operations describe
```