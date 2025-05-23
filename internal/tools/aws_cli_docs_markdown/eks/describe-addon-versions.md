# describe-addon-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-addon-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-addon-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# describe-addon-versions

## Description

Describes the versions for an add-on.

Information such as the Kubernetes versions that you can use the add-on with, the `owner` , `publisher` , and the `type` of the add-on are returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeAddonVersions)

`describe-addon-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `addons`

## Synopsis

```
describe-addon-versions
[--kubernetes-version <value>]
[--addon-name <value>]
[--types <value>]
[--publishers <value>]
[--owners <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--kubernetes-version` (string)

The Kubernetes versions that you can use the add-on with.

`--addon-name` (string)

The name of the add-on. The name must match one of the names returned by ` `ListAddons` [https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons).html`__ .

`--types` (list)

The type of the add-on. For valid `types` , donât specify a value for this property.

(string)

Syntax:

```
"string" "string" ...
```

`--publishers` (list)

The publisher of the add-on. For valid `publishers` , donât specify a value for this property.

(string)

Syntax:

```
"string" "string" ...
```

`--owners` (list)

The owner of the add-on. For valid `owners` , donât specify a value for this property.

(string)

Syntax:

```
"string" "string" ...
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: List all the available addons for EKS Cluster**

The following `describe-addon-versions` example list all the available AWS addons.

```
aws eks describe-addon-versions  \
    --query 'sort_by(addons  &owner)[].{publisher: publisher, owner: owner, addonName: addonName, type: type}' \
    --output table
```

Output:

```
--------------------------------------------------------------------------------------------------------------------
|                                               DescribeAddonVersions                                              |
+---------------------------------------------+------------------+-----------------------+-------------------------+
|                  addonName                  |      owner       |       publisher       |          type           |
+---------------------------------------------+------------------+-----------------------+-------------------------+
|  vpc-cni                                    |  aws             |  eks                  |  networking             |
|  snapshot-controller                        |  aws             |  eks                  |  storage                |
|  kube-proxy                                 |  aws             |  eks                  |  networking             |
|  eks-pod-identity-agent                     |  aws             |  eks                  |  security               |
|  coredns                                    |  aws             |  eks                  |  networking             |
|  aws-mountpoint-s3-csi-driver               |  aws             |  s3                   |  storage                |
|  aws-guardduty-agent                        |  aws             |  eks                  |  security               |
|  aws-efs-csi-driver                         |  aws             |  eks                  |  storage                |
|  aws-ebs-csi-driver                         |  aws             |  eks                  |  storage                |
|  amazon-cloudwatch-observability            |  aws             |  eks                  |  observability          |
|  adot                                       |  aws             |  eks                  |  observability          |
|  upwind-security_upwind-operator            |  aws-marketplace |  Upwind Security      |  security               |
|  upbound_universal-crossplane               |  aws-marketplace |  upbound              |  infra-management       |
|  tetrate-io_istio-distro                    |  aws-marketplace |  tetrate-io           |  policy-management      |
|  teleport_teleport                          |  aws-marketplace |  teleport             |  policy-management      |
|  stormforge_optimize-live                   |  aws-marketplace |  StormForge           |  cost-management        |
|  splunk_splunk-otel-collector-chart         |  aws-marketplace |  Splunk               |  monitoring             |
|  solo-io_istio-distro                       |  aws-marketplace |  Solo.io              |  service-mesh           |
|  rafay-systems_rafay-operator               |  aws-marketplace |  rafay-systems        |  kubernetes-management  |
|  new-relic_kubernetes-operator              |  aws-marketplace |  New Relic            |  observability          |
|  netapp_trident-operator                    |  aws-marketplace |  NetApp Inc.          |  storage                |
|  leaksignal_leakagent                       |  aws-marketplace |  leaksignal           |  monitoring             |
|  kubecost_kubecost                          |  aws-marketplace |  kubecost             |  cost-management        |
|  kong_konnect-ri                            |  aws-marketplace |  kong                 |  ingress-service-type   |
|  kasten_k10                                 |  aws-marketplace |  Kasten by Veeam      |  data-protection        |
|  haproxy-technologies_kubernetes-ingress-ee |  aws-marketplace |  HAProxy Technologies |  ingress-controller     |
|  groundcover_agent                          |  aws-marketplace |  groundcover          |  monitoring             |
|  grafana-labs_kubernetes-monitoring         |  aws-marketplace |  Grafana Labs         |  monitoring             |
|  factorhouse_kpow                           |  aws-marketplace |  factorhouse          |  monitoring             |
|  dynatrace_dynatrace-operator               |  aws-marketplace |  dynatrace            |  monitoring             |
|  datree_engine-pro                          |  aws-marketplace |  datree               |  policy-management      |
|  datadog_operator                           |  aws-marketplace |  Datadog              |  monitoring             |
|  cribl_cribledge                            |  aws-marketplace |  Cribl                |  observability          |
|  calyptia_fluent-bit                        |  aws-marketplace |  Calyptia Inc         |  observability          |
|  accuknox_kubearmor                         |  aws-marketplace |  AccuKnox             |  security               |
+---------------------------------------------+------------------+-----------------------+-------------------------+
```

For more information, see [Managing Amazon EKS add-ons - Creating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#creating-an-add-on) in the *Amazon EKS User Guide*.

**Example 2: List all the available addons for specified Kubernetes version suppoerted for EKS**

The following `describe-addon-versions` example list all the available addons for specified Kubernetes version suppoerted for EKS.

```
aws eks describe-addon-versions  \
    --kubernetes-version=1.26 \
    --query 'sort_by(addons  &owner)[].{publisher: publisher, owner: owner, addonName: addonName, type: type}' \
    --output table
```

Output:

```
--------------------------------------------------------------------------------------------------------------------
|                                               DescribeAddonVersions                                              |
+---------------------------------------------+------------------+-----------------------+-------------------------+
|                  addonName                  |      owner       |       publisher       |          type           |
+---------------------------------------------+------------------+-----------------------+-------------------------+
|  vpc-cni                                    |  aws             |  eks                  |  networking             |
|  snapshot-controller                        |  aws             |  eks                  |  storage                |
|  kube-proxy                                 |  aws             |  eks                  |  networking             |
|  eks-pod-identity-agent                     |  aws             |  eks                  |  security               |
|  coredns                                    |  aws             |  eks                  |  networking             |
|  aws-mountpoint-s3-csi-driver               |  aws             |  s3                   |  storage                |
|  aws-guardduty-agent                        |  aws             |  eks                  |  security               |
|  aws-efs-csi-driver                         |  aws             |  eks                  |  storage                |
|  aws-ebs-csi-driver                         |  aws             |  eks                  |  storage                |
|  amazon-cloudwatch-observability            |  aws             |  eks                  |  observability          |
|  adot                                       |  aws             |  eks                  |  observability          |
|  upwind-security_upwind-operator            |  aws-marketplace |  Upwind Security      |  security               |
|  tetrate-io_istio-distro                    |  aws-marketplace |  tetrate-io           |  policy-management      |
|  stormforge_optimize-live                   |  aws-marketplace |  StormForge           |  cost-management        |
|  splunk_splunk-otel-collector-chart         |  aws-marketplace |  Splunk               |  monitoring             |
|  solo-io_istio-distro                       |  aws-marketplace |  Solo.io              |  service-mesh           |
|  rafay-systems_rafay-operator               |  aws-marketplace |  rafay-systems        |  kubernetes-management  |
|  new-relic_kubernetes-operator              |  aws-marketplace |  New Relic            |  observability          |
|  netapp_trident-operator                    |  aws-marketplace |  NetApp Inc.          |  storage                |
|  leaksignal_leakagent                       |  aws-marketplace |  leaksignal           |  monitoring             |
|  kubecost_kubecost                          |  aws-marketplace |  kubecost             |  cost-management        |
|  kong_konnect-ri                            |  aws-marketplace |  kong                 |  ingress-service-type   |
|  haproxy-technologies_kubernetes-ingress-ee |  aws-marketplace |  HAProxy Technologies |  ingress-controller     |
|  groundcover_agent                          |  aws-marketplace |  groundcover          |  monitoring             |
|  grafana-labs_kubernetes-monitoring         |  aws-marketplace |  Grafana Labs         |  monitoring             |
|  dynatrace_dynatrace-operator               |  aws-marketplace |  dynatrace            |  monitoring             |
|  datadog_operator                           |  aws-marketplace |  Datadog              |  monitoring             |
|  cribl_cribledge                            |  aws-marketplace |  Cribl                |  observability          |
|  calyptia_fluent-bit                        |  aws-marketplace |  Calyptia Inc         |  observability          |
|  accuknox_kubearmor                         |  aws-marketplace |  AccuKnox             |  security               |
+---------------------------------------------+------------------+-----------------------+-------------------------+
```

For more information, see [Managing Amazon EKS add-ons - Creating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#creating-an-add-on) in the *Amazon EKS User Guide*.

**Example 3: List all the available vpc-cni addons version for specified Kubernetes version suppoerted for EKS**

The following `describe-addon-versions` example list all the available vpc-cni addons version for specified Kubernetes version suppoerted for EKS.

```
aws eks describe-addon-versions \
    --kubernetes-version=1.26 \
    --addon-name=vpc-cni \
    --query='addons[].addonVersions[].addonVersion'
```

Output:

```
[
    "v1.18.0-eksbuild.1",
    "v1.17.1-eksbuild.1",
    "v1.16.4-eksbuild.2",
    "v1.16.3-eksbuild.2",
    "v1.16.2-eksbuild.1",
    "v1.16.0-eksbuild.1",
    "v1.15.5-eksbuild.1",
    "v1.15.4-eksbuild.1",
    "v1.15.3-eksbuild.1",
    "v1.15.1-eksbuild.1",
    "v1.15.0-eksbuild.2",
    "v1.14.1-eksbuild.1",
    "v1.14.0-eksbuild.3",
    "v1.13.4-eksbuild.1",
    "v1.13.3-eksbuild.1",
    "v1.13.2-eksbuild.1",
    "v1.13.0-eksbuild.1",
    "v1.12.6-eksbuild.2",
    "v1.12.6-eksbuild.1",
    "v1.12.5-eksbuild.2",
    "v1.12.0-eksbuild.2"
]
```

For more information, see [Managing Amazon EKS add-ons - Creating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#creating-an-add-on) in the *Amazon EKS User Guide*.

## Output

addons -> (list)

The list of available versions with Kubernetes version compatibility and other properties.

(structure)

Information about an add-on.

addonName -> (string)

The name of the add-on.

type -> (string)

The type of the add-on.

addonVersions -> (list)

An object representing information about available add-on versions and compatible Kubernetes versions.

(structure)

Information about an add-on version.

addonVersion -> (string)

The version of the add-on.

architecture -> (list)

The architectures that the version supports.

(string)

computeTypes -> (list)

Indicates the compute type of the addon version.

(string)

compatibilities -> (list)

An object representing the compatibilities of a version.

(structure)

Compatibility information.

clusterVersion -> (string)

The supported Kubernetes version of the cluster.

platformVersions -> (list)

The supported compute platform.

(string)

defaultVersion -> (boolean)

The supported default version.

requiresConfiguration -> (boolean)

Whether the add-on requires configuration.

requiresIamPermissions -> (boolean)

Indicates if the Addon requires IAM Permissions to operate, such as networking permissions.

publisher -> (string)

The publisher of the add-on.

owner -> (string)

The owner of the add-on.

marketplaceInformation -> (structure)

Information about the add-on from the Amazon Web Services Marketplace.

productId -> (string)

The product ID from the Amazon Web Services Marketplace.

productUrl -> (string)

The product URL from the Amazon Web Services Marketplace.

nextToken -> (string)

The `nextToken` value to include in a future `DescribeAddonVersions` request. When the results of a `DescribeAddonVersions` request exceed `maxResults` , you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.

### Note

This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.