# gcloud network-management vpc-flow-logs-configs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete)*

**NAME**

: **gcloud network-management vpc-flow-logs-configs delete - deletes the specified VPC Flow Logs configuration**

**SYNOPSIS**

: **`gcloud network-management vpc-flow-logs-configs delete` (`[VPC_FLOW_LOGS_CONFIG](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete#VPC_FLOW_LOGS_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes the specified VPC Flow Logs configuration.

**EXAMPLES**

: To delete a VPC Flow Logs configuration `my-config`, run:

```
gcloud network-management vpc-flow-logs-configs delete my-config --location=global
```

**POSITIONAL ARGUMENTS**

: **VpcFlowLogsConfig resource - `VpcFlowLogsConfig` resource name using
the form:
`projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config}`
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

: This command uses the `networkmanagement/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This variant is also available:

```
gcloud beta network-management vpc-flow-logs-configs delete
```