# gcloud compute networks vpc-access connectors delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete)*

**NAME**

: **gcloud compute networks vpc-access connectors delete - delete a VPC Access connector**

**SYNOPSIS**

: **`gcloud compute networks vpc-access connectors delete` (`[CONNECTOR](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete#CONNECTOR)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a new VPC Access connector with the given name.
This command can fail for the following reasons:

- An instance with the same name already exists.
- The active account does not have permission to delete instances.

**EXAMPLES**

: The following command deletes a VPC Access connector with name
`my-vpc-connector` in region `us-central1`:

```
gcloud compute networks vpc-access connectors delete my-vpc-connector --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Connector resource - Arguments and flags that specify the VPC Access connector
you want to delete. The arguments in this group can be used to specify the
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
gcloud beta compute networks vpc-access connectors delete
```