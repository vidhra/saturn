# gcloud network-connectivity service-connection-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update)*

**NAME**

: **gcloud network-connectivity service-connection-policies update - update a service connection policy**

**SYNOPSIS**

: **`gcloud network-connectivity service-connection-policies update` `[SERVICE_CONNECTION_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#SERVICE_CONNECTION_POLICY)` [`[--allowed-google-producers-resource-hierarchy-level](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--allowed-google-producers-resource-hierarchy-level)`=[`ALLOWED_GOOGLE_PRODUCERS_RESOURCE_HIERARCHY_LEVEL`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--producer-instance-location](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--producer-instance-location)`=`PRODUCER_INSTANCE_LOCATION`] [`[--psc-connection-limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--psc-connection-limit)`=`PSC_CONNECTION_LIMIT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--region)`=`REGION`] [`[--subnets](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#--subnets)`=[`SUBNETS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Service Connection Policy with the given name.

**EXAMPLES**

: Update a Service Connection Policy with name `my-service-conn-policy`
in region `us-central1`.

```
gcloud network-connectivity service-connection-policies update my-service-conn-policy --region=us-central1 --psc-connection-limit=5 --subnets=my-subnet --producer-instance-location=custom-resource-hierarchy-levels --allowed-google-producers-resource-hierarchy-level=projects/my-project
```

**POSITIONAL ARGUMENTS**

: **Service connection policy resource - Name of the Service Connection Policy to be
updated. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service_connection_policy` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `service_connection_policy` on the command line
with a fully specified name;
- provide the argument `--region` on the command line.

This must be specified.

**`SERVICE_CONNECTION_POLICY`**:
ID of the service connection policy or fully qualified identifier for the
service connection policy.
To set the `service_connection_policy` attribute:

- provide the argument `service_connection_policy` on the command line.**

**FLAGS**

: **--allowed-google-producers-resource-hierarchy-level**:
List of projects, folders, or orgs where the producer instance can be located in
the form "projects/123456789", folders/123456789", or "organizations/123456789".

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the Service Connection Policy to be updated.

**--labels**:
List of label KEY=VALUE pairs to add.

**--producer-instance-location**:
Option that determines where the producer instances can be located for which
connections can be created in the network controlled by this policy.
`PRODUCER_INSTANCE_LOCATION` must be one of:

**`custom-resource-hierarchy-levels`**:
The producer instance must be located in one of the values provided in the
allowed-google-producers-resource-hierarchy-level flag.

**`none`**:
The producer instance must be within the same project as this connection policy.

**--psc-connection-limit**:
Max number of PSC connections for this policy.

**--region**:
For resources [service connection policy, subnetwork], provides fallback value
for resource region attribute. When the resource's full URI path is not
provided, region will fallback to this flag value.

**Subnetwork resource - Subnetwork to use for IP address management. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--subnets` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--subnets` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

**--subnets**:
IDs of the subnetworks or fully qualified identifiers for the subnetworks.
To set the `subnetwork` attribute:

- provide the argument `--subnets` on the command line.**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)