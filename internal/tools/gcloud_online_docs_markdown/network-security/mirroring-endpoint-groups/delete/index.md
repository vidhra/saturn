# gcloud network-security mirroring-endpoint-groups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete)*

**NAME**

: **gcloud network-security mirroring-endpoint-groups delete - delete a Mirroring Endpoint Group**

**SYNOPSIS**

: **`gcloud network-security mirroring-endpoint-groups delete` (`[MIRRORING_ENDPOINT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete#MIRRORING_ENDPOINT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete#--async)`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a mirroring endpoint group. Check the progress of endpoint group deletion
by using `[gcloud
network-security mirroring-endpoint-groups list](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To delete a mirroring endpoint group called `my-endpoint-group`, in
project ID `my-project`, run:
```
gcloud network-security mirroring-endpoint-groups delete my-endpoint-group --project=my-project --location=global
```

OR

```
gcloud network-security mirroring-endpoint-groups delete projects/my-project/locations/global/mirroringEndpointGroups/my-endpoint-group
```

**POSITIONAL ARGUMENTS**

: **Mirroring endpoint group resource - Mirroring Endpoint Group. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIRRORING_ENDPOINT_GROUP`**:
ID of the mirroring endpoint group or fully qualified identifier for the
mirroring endpoint group.
To set the `endpoint-group-id` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the mirroring endpoint group.
To set the `location` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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

**NOTES**

: These variants are also available:

```
gcloud alpha network-security mirroring-endpoint-groups delete
```

```
gcloud beta network-security mirroring-endpoint-groups delete
```