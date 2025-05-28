# gcloud compute networks vpc-access connectors update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update)*

**NAME**

: **gcloud compute networks vpc-access connectors update - update a VPC Access connector**

**SYNOPSIS**

: **`gcloud compute networks vpc-access connectors update` (`[CONNECTOR](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#CONNECTOR)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#--async)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#--machine-type)`=`MACHINE_TYPE`] [`[--max-instances](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#--max-instances)`=`MAX_INSTANCES`] [`[--min-instances](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#--min-instances)`=`MIN_INSTANCES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/vpc-access/connectors/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing VPC Access connector with the given name.
This command can fail for the following reasons:

- Invalid parameters are passed to this command.
- The active account does not have permission to update instances.

**EXAMPLES**

: The following command updates a VPC Access connector with name
`my-vpc-connector` in region `us-central1`:

```
gcloud compute networks vpc-access connectors update my-vpc-connector --region=us-central1 --min-instances=3 --max-instances=5
```

**POSITIONAL ARGUMENTS**

: **Connector resource - Arguments and flags that specify the VPC Access connector
you want to update. The arguments in this group can be used to specify the
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
If set, updates the machine type of VMs underlying the connector. Accepted
values are "e2-micro", "f1-micro", and "e2-standard-4".

**--max-instances**:
If set, updates the maximum number of instances within an autoscaling group
underlying the connector. Value must be between 3 and 10, inclusive, greater
than or equal to the currently set maximum number of instances, and greater than
the value specified by `--min-instances`.
`--min-instances` must be provided.

**--min-instances**:
If set, updates the minimum number of instances within an autoscaling group
underlying the connector. Value must be between 2 and 9, inclusive, greater than
or equal to the currently set minimum number of instances, and less than the
value specified by --max-instances`.`--max-instances`must be
provided`

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
gcloud beta compute networks vpc-access connectors update
```