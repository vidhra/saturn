# gcloud alpha compute interconnects attachments groups remove-members  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/remove-members](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/remove-members)*

**NAME**

: **gcloud alpha compute interconnects attachments groups remove-members - remove member interconnect attachments from a Compute Engine interconnect attachment group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects attachments groups remove-members` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/remove-members#NAME)` `[--attachments](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/remove-members#--attachments)`=[`INTERCONNECT_ATTACHMENT`,…] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/remove-members#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects attachments groups
remove-members` is used to remove member interconnect attachments from an
interconnect attachment group.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To remove attachment-1 and attachment-2 from interconnect attachment group
example-attachment-group, run:

```
gcloud alpha compute interconnects attachments groups remove-members example-attachment-group --attachments=region-1/attachment-1,region-2/attachment-2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment group to update.

**REQUIRED FLAGS**

: **--attachments**:
Member interconnect attachments to add to or remove from the interconnect
attachment group.

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
gcloud compute interconnects attachments groups remove-members
```

```
gcloud beta compute interconnects attachments groups remove-members
```