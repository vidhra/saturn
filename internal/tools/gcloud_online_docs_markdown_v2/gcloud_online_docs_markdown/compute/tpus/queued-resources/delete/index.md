# gcloud compute tpus queued-resources delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete)*

**NAME**

: **gcloud compute tpus queued-resources delete - delete a Queued Resource**

**SYNOPSIS**

: **`gcloud compute tpus queued-resources delete` (`[QUEUED_RESOURCE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete#QUEUED_RESOURCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an existing Queued Resource.
To get a list of Queued Resources for deletion, run:

```
gcloud compute tpus queued-resources list
```

**EXAMPLES**

: To delete a Queued Resource with ID `my-queued-resource` in zone
`us-central1-b` and project `my-project`, run:

```
gcloud compute tpus queued-resources delete my-queued-resource --zone=us-central1-b --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Queued resource resource - The Queued Resource you want to delete. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `queued_resource` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`QUEUED_RESOURCE`**:
ID of the queued_resource or fully qualified identifier for the queued_resource.
To set the `queued_resource` attribute:

- provide the argument `queued_resource` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The compute/zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `queued_resource` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
If set to true, any nodes in this queued resource will also be deleted.
Otherwise, the request will only work if the queued resource has no nodes.

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

: This command uses the `tpu/v2` API. The full documentation for this
API can be found at: [https://cloud.google.com/tpu/](https://cloud.google.com/tpu/)

**NOTES**

: This variant is also available:

```
gcloud alpha compute tpus queued-resources delete
```