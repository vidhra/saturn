# gcloud network-connectivity hubs reject-spoke-update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update)*

**NAME**

: **gcloud network-connectivity hubs reject-spoke-update - reject a proposal to update a spoke in a hub**

**SYNOPSIS**

: **`gcloud network-connectivity hubs reject-spoke-update` `[HUB](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#HUB)` `[--spoke](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#--spoke)`=`SPOKE` `[--spoke-etag](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#--spoke-etag)`=`SPOKE_ETAG` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#--async)`] [`[--details](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#--details)`=`DETAILS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/reject-spoke-update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Reject a VPC spoke update proposal. By rejecting a spoke update, you prevent
updating the connectivity between the associated VPC network and any other VPC
networks that are attached to the same hub.

**EXAMPLES**

: To reject updating a spoke named ``my-spoke``
with ``etag`` in a hub named
``my-hub`` with reason
``my-reason``, run:

```
gcloud network-connectivity hubs reject-spoke-update my-hub --spoke="projects/spoke-project/locations/global/hubs/my-spoke" --spoke-etag=etag --details=my-reason
```

**POSITIONAL ARGUMENTS**

: **Hub resource - Name of the hub to reject the spoke update. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `hub` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HUB`**:
ID of the hub or fully qualified identifier for the hub.
To set the `hub` attribute:

- provide the argument `hub` on the command line.**

**REQUIRED FLAGS**

: **--spoke**:
URI of the spoke to reject update

**--spoke-etag**:
Etag of the spoke to reject update

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--details**:
Additional details behind the rejection

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs reject-spoke-update
```