# gcloud compute networks vpc-access connectors create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create)*

**NAME**

: **gcloud compute networks vpc-access connectors create - create a VPC Access connector**

**SYNOPSIS**

: **`gcloud compute networks vpc-access connectors create` (`[CONNECTOR](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#CONNECTOR)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--async)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--machine-type)`=`MACHINE_TYPE`] [`[--max-instances](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--max-instances)`=`MAX_INSTANCES`; default=10 `[--min-instances](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--min-instances)`=`MIN_INSTANCES`; default=2     | `[--max-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--max-throughput)`=`MAX_THROUGHPUT` `[--min-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--min-throughput)`=`MIN_THROUGHPUT`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--network)`=`NETWORK`; default="default" `[--range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--range)`=`RANGE`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--subnet)`=`SUBNET` `[--subnet-project](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#--subnet-project)`=`SUBNET_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new VPC Access connector with the given name.
This command can fail for the following reasons:

- An instance with the same name already exists.
- The active account does not have permission to create instances.

**EXAMPLES**

: The following command creates a VPC Access connector with name
'my-vpc-connector' in region 'us-central1' in network 'my-network' with IP CIDR
range of '10.132.0.0/28'.

```
gcloud compute networks vpc-access connectors create my-vpc-connector --region=us-central1 --network=my-network --range=10.132.0.0/28
```

**POSITIONAL ARGUMENTS**

: **Connector resource - Arguments and flags that specify the VPC Access connector
you want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connector` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTOR`**:
ID of the connector or fully qualified identifier for the connector.
To set the `connector` attribute:

- provide the argument `connector` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Compute region (e.g. us-central1) for the connector.
To set the `region` attribute:

- provide the argument `connector` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--machine-type**:
Machine type of VMs underlying the VPC Access connector. Accepted values are
``e2-micro``,
``f1-micro``, and
``e2-standard-4``. If left unspecified, the
``e2-micro`` machine type is used.

**--max-instances**

**--network**

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

: This command uses the `vpcaccess/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/vpc/docs/configure-serverless-vpc-access](https://cloud.google.com/vpc/docs/configure-serverless-vpc-access)

**NOTES**

: This variant is also available:

```
gcloud beta compute networks vpc-access connectors create
```