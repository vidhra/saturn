# gcloud network-connectivity service-connection-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create)*

**NAME**

: **gcloud network-connectivity service-connection-policies create - create a new Service Connection Policy**

**SYNOPSIS**

: **`gcloud network-connectivity service-connection-policies create` `[SERVICE_CONNECTION_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#SERVICE_CONNECTION_POLICY)` `[--network](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--network)`=`NETWORK` `[--service-class](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--service-class)`=`SERVICE_CLASS` (`[--subnets](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--subnets)`=[`SUBNETS`,…] : `[--allowed-google-producers-resource-hierarchy-level](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--allowed-google-producers-resource-hierarchy-level)`=[`ALLOWED_GOOGLE_PRODUCERS_RESOURCE_HIERARCHY_LEVEL`,…] `[--producer-instance-location](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--producer-instance-location)`=`PRODUCER_INSTANCE_LOCATION` `[--psc-connection-limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--psc-connection-limit)`=`PSC_CONNECTION_LIMIT`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Service Connection Policy with the given name.

**EXAMPLES**

: Create a Service Connection Policy with name
``my-service-conn-policy`` for network
``projects/my-project/global/networks/net1``
and service class ``my-service-class-ad32fa4b``
in region ``us-central1`` using subnet
projects/my-project/regions/us-central1/subnetworks/subnet1 subject to
custom-resource-hierarchy-levels that allows connections from Google-managed
producer instances in projects/my-project.

```
gcloud network-connectivity service-connection-policies create my-service-conn-policy --network="projects/my-project/global/networks/net1" --service-class=my-service-class-ad32fa4b --region=us-central1 --subnets=projects/my-project/regions/us-central1/subnetworks/subnet1 --psc-connection-limit=100 --producer-instance-location=custom-resource-hierarchy-levels --allowed-google-producers-resource-hierarchy-level=projects/my-project
```

**POSITIONAL ARGUMENTS**

: **Service connection policy resource - Name of the Service Connection Policy to be
created. This represents a Cloud resource. (NOTE) Some attributes are not given
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

**REQUIRED FLAGS**

: **Network resource - Network that this service connection policy applies to. E.g.
projects/my-project/global/networks/net1 This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `--network` on the command line.**

**--service-class**:
Service class that this policy is created for. E.g. my-service-class-ad32fa4b

**This must be specified.

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

This must be specified.

**--subnets**:
IDs of the subnetworks or fully qualified identifiers for the subnetworks.
To set the `subnetwork` attribute:

- provide the argument `--subnets` on the command line.**

**--allowed-google-producers-resource-hierarchy-level**:
List of projects, folders, or orgs where the producer instance can be located in
the form "projects/123456789", folders/123456789", or "organizations/123456789".

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
Max number of PSC connections for this policy.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the Service Connection Policy to be created.

**--labels**:
List of label KEY=VALUE pairs to add.

**--region**:
For resources [service connection policy, subnetwork], provides fallback value
for resource region attribute. When the resource's full URI path is not
provided, region will fallback to this flag value.

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