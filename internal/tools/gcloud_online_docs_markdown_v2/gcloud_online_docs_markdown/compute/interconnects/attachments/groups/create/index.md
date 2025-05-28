# gcloud compute interconnects attachments groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create)*

**NAME**

: **gcloud compute interconnects attachments groups create - create a Compute Engine interconnect attachment group**

**SYNOPSIS**

: **`gcloud compute interconnects attachments groups create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create#NAME)` `[--intended-availability-sla](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create#--intended-availability-sla)`=`INTENDED_AVAILABILITY_SLA` [`[--attachments](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create#--attachments)`=[`INTERCONNECT_ATTACHMENT`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects attachments groups create` is used to
create interconnect attachment groups. An interconnect attachment group connects
a set of redundant interconnect attachments between Google and the customer.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To create an interconnect attachment group capable of PRODUCTION_CRITICAL, run:

```
gcloud compute interconnects attachments groups create example-attachment-group --intended-availability-sla=PRODUCTION_CRITICAL --description="Example interconnect attachment group"
```

It is easy to add members to an existing interconnect attachment group after
creation using the `add-members` command.
To create an interconnect attachment group capable of PRODUCTION_NON_CRITICAL,
with two members at creation time, run:

```
gcloud compute interconnects attachments groups create example-attachment-group --intended-availability-sla=PRODUCTION_NON_CRITICAL --attachments=region-1/attachment-1,region-2/attachment-2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment group to create.

**REQUIRED FLAGS**

: **--intended-availability-sla**:
The availability SLA that the user intends this group to support.

**OPTIONAL FLAGS**

: **--attachments**:
Member interconnect attachments to add to the interconnect attachment group
initially.

**--description**:
An optional, textual description for the interconnect attachment group.

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
gcloud alpha compute interconnects attachments groups create
```

```
gcloud beta compute interconnects attachments groups create
```