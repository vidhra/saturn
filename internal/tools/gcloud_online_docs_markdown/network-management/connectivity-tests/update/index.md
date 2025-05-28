# gcloud network-management connectivity-tests update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update)*

**NAME**

: **gcloud network-management connectivity-tests update - update an existing connectivity test**

**SYNOPSIS**

: **`gcloud network-management connectivity-tests update` `[CONNECTIVITY_TEST](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#CONNECTIVITY_TEST)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--async)`] [`[--bypass-firewall-checks](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--bypass-firewall-checks)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--description)`=`DESCRIPTION`] [`[--destination-fqdn](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-fqdn)`=`DESTINATION_FQDN`] [`[--destination-network](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-network)`=`DESTINATION_NETWORK`] [`[--destination-port](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-port)`=`DESTINATION_PORT`] [`[--destination-project](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-project)`=`DESTINATION_PROJECT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--other-projects](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--other-projects)`=[`OTHER_PROJECTS`,…]] [`[--protocol](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--protocol)`=`PROTOCOL`] [`[--round-trip](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--round-trip)`] [`[--source-network](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-network)`=`SOURCE_NETWORK`] [`[--source-network-type](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-network-type)`=`SOURCE_NETWORK_TYPE`; default="gcp-network"] [`[--source-project](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-project)`=`SOURCE_PROJECT`] [`[--clear-destination-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-cloud-sql-instance)`     | `[--destination-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-cloud-sql-instance)`=`DESTINATION_CLOUD_SQL_INSTANCE`] [`[--clear-destination-forwarding-rule](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-forwarding-rule)`     | `[--destination-forwarding-rule](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-forwarding-rule)`=`DESTINATION_FORWARDING_RULE`] [`[--clear-destination-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-gke-master-cluster)`     | `[--destination-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-gke-master-cluster)`=`DESTINATION_GKE_MASTER_CLUSTER`] [`[--clear-destination-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-instance)`     | `[--destination-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-instance)`=`DESTINATION_INSTANCE`] [`[--clear-destination-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-ip-address)`     | `[--destination-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-ip-address)`=`DESTINATION_IP_ADDRESS`] [`[--clear-destination-redis-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-redis-cluster)`     | `[--destination-redis-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-redis-cluster)`=`DESTINATION_REDIS_CLUSTER`] [`[--clear-destination-redis-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-destination-redis-instance)`     | `[--destination-redis-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--destination-redis-instance)`=`DESTINATION_REDIS_INSTANCE`] [`[--clear-source-app-engine-version](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-app-engine-version)`     | `[--source-app-engine-version](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-app-engine-version)`=`SOURCE_APP_ENGINE_VERSION`] [`[--clear-source-cloud-function](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-cloud-function)`     | `[--source-cloud-function](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-cloud-function)`=`SOURCE_CLOUD_FUNCTION`] [`[--clear-source-cloud-run-revision](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-cloud-run-revision)`     | `[--source-cloud-run-revision](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-cloud-run-revision)`=`SOURCE_CLOUD_RUN_REVISION`] [`[--clear-source-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-cloud-sql-instance)`     | `[--source-cloud-sql-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-cloud-sql-instance)`=`SOURCE_CLOUD_SQL_INSTANCE`] [`[--clear-source-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-gke-master-cluster)`     | `[--source-gke-master-cluster](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-gke-master-cluster)`=`SOURCE_GKE_MASTER_CLUSTER`] [`[--clear-source-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-instance)`     | `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-instance)`=`SOURCE_INSTANCE`] [`[--clear-source-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--clear-source-ip-address)`     | `[--source-ip-address](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#--source-ip-address)`=`SOURCE_IP_ADDRESS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing connectivity test with the given name.

**EXAMPLES**

: The following command updates a connectivity test with the name my-test,
modifying the description and destination IP address.

```
gcloud network-management connectivity-tests update my-test --description='update dst addr' --destination-ip-address='10.142.0.3'
```

**POSITIONAL ARGUMENTS**

: **Connectivity test resource - Name of the connectivity test you want to update.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bypass-firewall-checks**:
This boolean controls whether to skip firewall checking. Use
--no-bypass-firewall-checks to disable.

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
from the source. Use --no-round-trip to disable.

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

**--clear-destination-cloud-sql-instance**

**--clear-destination-forwarding-rule**

**--clear-destination-gke-master-cluster**

**--clear-destination-instance**

**--clear-destination-ip-address**

**--clear-destination-redis-cluster**

**--clear-destination-redis-instance**

**--clear-source-app-engine-version**

**--clear-source-cloud-function**

**--clear-source-cloud-run-revision**

**--clear-source-cloud-sql-instance**

**--clear-source-gke-master-cluster**

**--clear-source-instance**

**--clear-source-ip-address**

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
gcloud beta network-management connectivity-tests update
```