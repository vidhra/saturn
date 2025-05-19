# gcloud alpha compute interconnects groups get-operational-status  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/get-operational-status](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/get-operational-status)*

**NAME**

: **gcloud alpha compute interconnects groups get-operational-status - get the operational status of a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects groups get-operational-status` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/get-operational-status#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/get-operational-status#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects groups
get-operational-status` is used to get the operational status of an
interconnect group.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To get the operational status of interconnect group example-interconnect-group,
run:

```
gcloud alpha compute interconnects groups get-operational-status example-interconnect-group
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect group to get operational status.

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
gcloud compute interconnects groups get-operational-status
```

```
gcloud beta compute interconnects groups get-operational-status
```