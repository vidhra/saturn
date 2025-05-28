# gcloud network-management connectivity-tests create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create)*

**NAME**

: **gcloud network-management connectivity-tests create - create a new connectivity test**

**SYNOPSIS**

: **`gcloud network-management connectivity-tests create` `[CONNECTIVITY_TEST](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#CONNECTIVITY_TEST)` (`[--destination-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-cloud-sql-instance)`=`DESTINATION_CLOUD_SQL_INSTANCE` `[--destination-forwarding-rule](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-forwarding-rule)`=`DESTINATION_FORWARDING_RULE` `[--destination-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-gke-master-cluster)`=`DESTINATION_GKE_MASTER_CLUSTER` `[--destination-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-instance)`=`DESTINATION_INSTANCE` `[--destination-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-ip-address)`=`DESTINATION_IP_ADDRESS` `[--destination-redis-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-redis-cluster)`=`DESTINATION_REDIS_CLUSTER` `[--destination-redis-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-redis-instance)`=`DESTINATION_REDIS_INSTANCE`) (`[--source-app-engine-version](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-app-engine-version)`=`SOURCE_APP_ENGINE_VERSION` `[--source-cloud-function](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-cloud-function)`=`SOURCE_CLOUD_FUNCTION` `[--source-cloud-run-revision](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-cloud-run-revision)`=`SOURCE_CLOUD_RUN_REVISION` `[--source-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-cloud-sql-instance)`=`SOURCE_CLOUD_SQL_INSTANCE` `[--source-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-gke-master-cluster)`=`SOURCE_GKE_MASTER_CLUSTER` `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-instance)`=`SOURCE_INSTANCE` `[--source-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-ip-address)`=`SOURCE_IP_ADDRESS`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--async)`] [`[--bypass-firewall-checks](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--bypass-firewall-checks)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--description)`=`DESCRIPTION`] [`[--destination-fqdn](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-fqdn)`=`DESTINATION_FQDN`] [`[--destination-network](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-network)`=`DESTINATION_NETWORK`] [`[--destination-port](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-port)`=`DESTINATION_PORT`] [`[--destination-project](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--destination-project)`=`DESTINATION_PROJECT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--other-projects](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--other-projects)`=[`OTHER_PROJECTS`,…]] [`[--protocol](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--protocol)`=`PROTOCOL`] [`[--round-trip](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--round-trip)`] [`[--source-network](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-network)`=`SOURCE_NETWORK`] [`[--source-network-type](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-network-type)`=`SOURCE_NETWORK_TYPE`; default="gcp-network"] [`[--source-project](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#--source-project)`=`SOURCE_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new connectivity test with the given name.

**EXAMPLES**

: The following command creates a connectivity test with the name my-test, and the
test between a source VM and a destination IP address in a peering network.

```
gcloud network-management connectivity-tests create my-test --source-instance=projects/my-project/zones/us-west-1/instances/my-instance --destination-ip-address=10.142.0.2 --destination-network=projects/my-project/global/networks/peering-network
```

**POSITIONAL ARGUMENTS**

: **Connectivity test resource - Name of the connectivity test you want to create.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connectivity_test` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTIVITY_TEST`**:
ID of the connectivity test or fully qualified identifier for the connectivity
test.
To set the `connectivity_test` attribute:

- provide the argument `connectivity_test` on the command line.**

**REQUIRED FLAGS**

: **--destination-cloud-sql-instance**

**--source-app-engine-version**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bypass-firewall-checks**:
This boolean controls whether to skip firewall checking.

**--description**:
The description of the connectivity test.

**--destination-fqdn**:
A hostname as the destination endpoint. Only applicable for Google Kubernetes
Engine.

**--destination-network**:
A VPC network URI where the destination is located.

**--destination-port**:
The IP protocol port of the destination. Only applicable when protocol is TCP or
UDP.

**--destination-project**:
Project ID of the destination endpoint.

**--labels**:
List of label KEY=VALUE pairs to add.

**--other-projects**:
IDs of other projects involved in the connectivity test, besides the source and
destination project.

**--protocol**:
Type of protocol for the test. When not provided, "TCP" is assumed.

**--round-trip**:
This boolean controls whether return traces (from the destination to the source)
will be additionally calculated if packet successfully reaches the destination
from the source.

**--source-network**:
A VPC network URI where the source is located.

**--source-network-type**:
Type of the network where the source is located.
`SOURCE_NETWORK_TYPE` must be one of:

**`gcp-network`**:
Network in Google Cloud Platform.

**`non-gcp-network`**:
Network outside Google Cloud Platform.

**--source-project**:
Project ID of the source endpoint.

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
gcloud beta network-management connectivity-tests create
```