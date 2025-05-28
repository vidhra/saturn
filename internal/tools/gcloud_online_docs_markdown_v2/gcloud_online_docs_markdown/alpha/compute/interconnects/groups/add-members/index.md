# gcloud alpha compute interconnects groups add-members  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/add-members](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/add-members)*

**NAME**

: **gcloud alpha compute interconnects groups add-members - add member interconnects to a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects groups add-members` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/add-members#NAME)` `[--interconnects](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/add-members#--interconnects)`=[`INTERCONNECT`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/add-members#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects groups
add-members` is used to add member interconnects to an interconnect group.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To add interconnects interconnect1 and interconnect2 to interconnect group
example-interconnect-group, run:

```
gcloud alpha compute interconnects groups add-members example-interconnect-group --interconnects=interconnect1,interconnect2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect group to update.

**REQUIRED FLAGS**

: **--interconnects**:
Member interconnects to add to or remove from the interconnect group.

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
gcloud compute interconnects groups add-members
```

```
gcloud beta compute interconnects groups add-members
```