# gcloud lustre instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update)*

**NAME**

: **gcloud lustre instances update - updates the parameters of a single Managed Lustre instance**

**SYNOPSIS**

: **`gcloud lustre instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--async)`] [`[--capacity-gib](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--capacity-gib)`=`CAPACITY_GIB`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--description)`=`DESCRIPTION`] [`[--[no-]gke-support-enabled](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--[no-]gke-support-enabled)`] [`[--per-unit-storage-throughput](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--per-unit-storage-throughput)`=`PER_UNIT_STORAGE_THROUGHPUT`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--request-id)`=`REQUEST_ID`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the parameters of a single Managed Lustre instance.

**EXAMPLES**

: To update the description of an instance `my-instance` in location
`us-central1-a` run:

```
gcloud lustre instances update my-instance --location=us-central1-a --description="<updated description>"
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Identifier. The name of the instance. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the instance resource.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--capacity-gib**:
The storage capacity of the instance in gibibytes (GiB). Allowed values are from
`18000` to `936000`, in increments of 9000.

**--description**:
A user-readable description of the instance.

**--[no-]gke-support-enabled**:
Indicates whether you want to enable support for GKE clients. By default, GKE
clients are not supported. Use `--gke-support-enabled` to enable and
`--no-gke-support-enabled` to disable.

**--per-unit-storage-throughput**:
The throughput of the instance in MB/s/TiB. Valid values are 250, 500, 1000.
Default value is 1000.

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--labels**

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

: This command uses the `lustre/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/managed-lustre/](https://cloud.google.com/managed-lustre/)

**NOTES**

: This variant is also available:

```
gcloud alpha lustre instances update
```