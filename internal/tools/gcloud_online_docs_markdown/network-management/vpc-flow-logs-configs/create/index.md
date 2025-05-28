# gcloud network-management vpc-flow-logs-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create)*

**NAME**

: **gcloud network-management vpc-flow-logs-configs create - creates a new VPC Flow Logs configuration in the specified project**

**SYNOPSIS**

: **`gcloud network-management vpc-flow-logs-configs create` (`[VPC_FLOW_LOGS_CONFIG](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#VPC_FLOW_LOGS_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--location)`=`LOCATION`) [`[--aggregation-interval](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--aggregation-interval)`=`AGGREGATION_INTERVAL`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--description)`=`DESCRIPTION`] [`[--filter-expr](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--filter-expr)`=`FILTER_EXPR`] [`[--flow-sampling](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--flow-sampling)`=`FLOW_SAMPLING`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--labels)`=[`LABELS`,…]] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--metadata)`=`METADATA`] [`[--metadata-fields](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--metadata-fields)`=[`METADATA_FIELDS`,…]] [`[--state](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--state)`=`STATE`] [`[--interconnect-attachment](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--interconnect-attachment)`=`INTERCONNECT_ATTACHMENT`     | `[--vpn-tunnel](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#--vpn-tunnel)`=`VPN_TUNNEL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new VPC Flow Logs configuration in the specified project. The
target-resource project must be the same as the configuration project.

**EXAMPLES**

: To create a new VPC Flow Logs configuration `my-config` in project
`my-project` for a VLAN attachment for Cloud Interconnect, run:

```
gcloud network-management vpc-flow-logs-configs create my-config --location=global --interconnect-attachment="projects/my-project/regions/{region}/interconnectAttachments/{interconnect_attachment_id}"
```

To create a new VPC Flow Logs configuration `my-config` in project
`my-project` for a Cloud VPN tunnel, run:

```
gcloud network-management vpc-flow-logs-configs create my-config --location=global --vpn-tunnel="projects/my-project/regions/{region}/vpnTunnels/{vpn_tunnel_id}"
```

**POSITIONAL ARGUMENTS**

: **VpcFlowLogsConfig resource - Identifier. Unique name of the configuration using
the form:
`projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `vpc_flow_logs_config` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VPC_FLOW_LOGS_CONFIG`**:
ID of the vpcFlowLogsConfig or fully qualified identifier for the
vpcFlowLogsConfig.
To set the `vpc_flow_logs_config` attribute:

- provide the argument `vpc_flow_logs_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the vpcFlowLogsConfig resource.
To set the `location` attribute:

- provide the argument `vpc_flow_logs_config` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--aggregation-interval**

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**

**--filter-expr**

**--flow-sampling**

**--labels**:
Resource labels to represent user-provided metadata.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--metadata**

**--metadata-fields**:
Custom metadata fields to include in the reported VPC flow logs. Can only be
specified if "metadata" was set to CUSTOM_METADATA.

**--state**

**--interconnect-attachment**

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

: This command uses the `networkmanagement/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This variant is also available:

```
gcloud beta network-management vpc-flow-logs-configs create
```