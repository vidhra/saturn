# gcloud compute interconnects groups remove-members  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/remove-members](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/remove-members)*

**NAME**

: **gcloud compute interconnects groups remove-members - remove member interconnects from a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud compute interconnects groups remove-members` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/remove-members#NAME)` `[--interconnects](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/remove-members#--interconnects)`=[`INTERCONNECT`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/remove-members#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects groups remove-members` is used to
remove member interconnects from an interconnect group.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To remove interconnects interconnect1 and interconnect2 from interconnect group
example-interconnect-group, run:

```
gcloud compute interconnects groups remove-members example-interconnect-group --interconnects=interconnect1,interconnect2
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

: These variants are also available:

```
gcloud alpha compute interconnects groups remove-members
```

```
gcloud beta compute interconnects groups remove-members
```