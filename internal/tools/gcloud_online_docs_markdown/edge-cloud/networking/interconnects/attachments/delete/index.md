# gcloud edge-cloud networking interconnects attachments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete)*

**NAME**

: **gcloud edge-cloud networking interconnects attachments delete - delete a Distributed Cloud Edge Network interconnect attachment**

**SYNOPSIS**

: **`gcloud edge-cloud networking interconnects attachments delete` (`[INTERCONNECT_ATTACHMENT](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete#INTERCONNECT_ATTACHMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/attachments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Distributed Cloud Edge Network interconnect attachment.

**EXAMPLES**

: To delete an interconnect attachment called 'my-attachment' in edge zone
'us-central1-edge-den1', run:

```
gcloud edge-cloud networking interconnects attachments delete my-attachment --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Interconnect attachment resource - Distributed Cloud Edge Network
interconnectAttachment to delete. The arguments in this group can be used to
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha edge-cloud networking interconnects attachments delete
```