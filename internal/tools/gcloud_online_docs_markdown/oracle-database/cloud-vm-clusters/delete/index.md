# gcloud oracle-database cloud-vm-clusters delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete)*

**NAME**

: **gcloud oracle-database cloud-vm-clusters delete - delete a CloudVmCluster**

**SYNOPSIS**

: **`gcloud oracle-database cloud-vm-clusters delete` (`[CLOUD_VM_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#CLOUD_VM_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#--force)`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#--request-id)`=`REQUEST_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a CloudVmCluster.

**EXAMPLES**

: To delete a CloudVmCluster with id `my-instance` in the location
`us-east4`, run:

```
gcloud oracle-database cloud-vm-clusters delete my-instance --location=us-east4
```

**POSITIONAL ARGUMENTS**

: **CloudVmCluster resource - The name of the Cloud VM Cluster in the following
format:
projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `cloud_vm_cluster` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLOUD_VM_CLUSTER`**:
ID of the cloudVmCluster or fully qualified identifier for the cloudVmCluster.
To set the `cloud_vm_cluster` attribute:

- provide the argument `cloud_vm_cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the cloudVmCluster resource.
To set the `location` attribute:

- provide the argument `cloud_vm_cluster` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If set to true, all child resources for the VM Cluster will be deleted. A VM
Cluster can only be deleted once all its child resources have been deleted.

**--request-id**:
An optional ID to identify the request. This value is used to identify duplicate
requests. If you make a request with the same request ID and the original
request is still in progress or completed, the server ignores the second
request. This prevents clients from accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

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

: This command uses the `oracledatabase/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/oracle/database/docs](https://cloud.google.com/oracle/database/docs)