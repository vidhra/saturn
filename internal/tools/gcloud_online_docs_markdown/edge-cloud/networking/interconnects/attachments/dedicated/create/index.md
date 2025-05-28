# gcloud edge-cloud networking interconnects attachments dedicated create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create)*

**NAME**

: **gcloud edge-cloud networking interconnects attachments dedicated create - create a Distributed Cloud Edge Network interconnect attachment**

**SYNOPSIS**

: **`gcloud edge-cloud networking interconnects attachments dedicated create` (`[INTERCONNECT_ATTACHMENT](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#INTERCONNECT_ATTACHMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--zone)`=`ZONE`) `[--interconnect](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--interconnect)`=`INTERCONNECT` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--mtu)`=`MTU`; default=1500] [`[--network](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--network)`=`NETWORK`] [`[--vlan-id](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#--vlan-id)`=`VLAN_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/dedicated/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new dedicated Distributed Cloud Edge Network interconnect attachment.

**EXAMPLES**

: To create a dedicated interconnect attachment called 'my-attachment' in edge
zone 'us-central1-edge-den1', run:

```
gcloud edge-cloud networking interconnects attachments dedicated create my-attachment --location=us-central1 --zone=us-central1-edge-den1 --interconnect=INTERCONNECT-LINK1 --network=my-edge-network --vlan-id=200 --mtu=1500
```

**POSITIONAL ARGUMENTS**

: **Interconnect attachment resource - Distributed Cloud Edge Network
interconnectAttachment to create. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `interconnect_attachment` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCONNECT_ATTACHMENT`**:
ID of the interconnect attachment or fully qualified identifier for the
interconnect attachment.
To set the `interconnect_attachment` attribute:

- provide the argument `interconnect_attachment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `interconnect_attachment` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

**--zone**:
The name of the Google Distributed Cloud Edge zone.
To set the `zone` attribute:

- provide the argument `interconnect_attachment` on the command line
with a fully specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--interconnect**:
The underlying interconnect object that this attachment's traffic will traverse
through.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
An optional, textual description for the interconnect attachment.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--mtu**:
Maximum transmission unit (MTU) is the size of the largest IP packet that can be
transmitted on this attachment. Default value is 1500 bytes, and the valid
values are 1500 and 9000.

**--network**:
The network to use for dynamic routing.

**--vlan-id**:
The ID of the vlan to tag the subnetwork. Default value is 0.

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

: This command uses the `edgenetwork/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/distributed-cloud-edge/docs](https://cloud.google.com/distributed-cloud-edge/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking interconnects attachments dedicated create
```