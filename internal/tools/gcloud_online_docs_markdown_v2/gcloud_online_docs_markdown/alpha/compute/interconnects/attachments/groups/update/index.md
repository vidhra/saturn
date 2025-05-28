# gcloud alpha compute interconnects attachments groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update)*

**NAME**

: **gcloud alpha compute interconnects attachments groups update - update a Compute Engine interconnect attachment group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects attachments groups update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update#NAME)` [`[--attachments](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update#--attachments)`=[`INTERCONNECT_ATTACHMENT`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update#--description)`=`DESCRIPTION`] [`[--intended-availability-sla](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update#--intended-availability-sla)`=`INTENDED_AVAILABILITY_SLA`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects attachments groups
update` is used to update interconnect attachment groups.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To update an interconnect attachment group example-attachment-group's intended
availability SLA to PRODUCTION_CRITICAL, run:

```
gcloud alpha compute interconnects attachments groups update example-attachment-group --intended-availability-sla=PRODUCTION_CRITICAL
```

To update an interconnect attachment group example-attachment-group's
description to "example attachment group description", run:

```
gcloud alpha compute interconnects attachments groups update example-attachment-group --description="example attachment group description"
```

To update an interconnect attachment group example-attachment-group's member
attachments to attachment-1 and attachment-2, run:

```
gcloud alpha compute interconnects attachments groups update example-attachment-group --attachments=region-1/attachment-1,region-2/attachment-2
```

Although you can add or remove member attachments using this command, it is
recommended to add or remove member attachments using the
`add-members` and `remove-members` commands.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment group to update.

**FLAGS**

: **--attachments**:
Member interconnect attachments to add to the interconnect attachment group
initially.

**--description**:
An optional, textual description for the interconnect attachment group.

**--intended-availability-sla**:
The availability SLA that the user intends this group to support.

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
gcloud compute interconnects attachments groups update
```

```
gcloud beta compute interconnects attachments groups update
```