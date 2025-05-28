# gcloud telco-automation orchestration-cluster delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete)*

**NAME**

: **gcloud telco-automation orchestration-cluster delete - delete a telco automation orchestration cluster**

**SYNOPSIS**

: **`gcloud telco-automation orchestration-cluster delete` (`[ORCHESTRATION_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete#ORCHESTRATION_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a telco automation orchestration cluster.

**EXAMPLES**

: To delete an orchestration cluster called `test-cluster` in region
`us-central1`, run:

```
gcloud telco-automation orchestration-cluster delete test-cluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Orchestration Cluster resource - Telco automation orchestration cluster to
delete. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `orchestration_cluster` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ORCHESTRATION_CLUSTER`**:
ID of the Orchestration Cluster or fully qualified identifier for the
Orchestration Cluster.
To set the `orchestration_cluster` attribute:

- provide the argument `orchestration_cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `orchestration_cluster` on the command line with
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

: This command uses the `telcoautomation/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native](https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native)

**NOTES**

: This variant is also available:

```
gcloud alpha telco-automation orchestration-cluster delete
```