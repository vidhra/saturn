# gcloud compute network-endpoint-groups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete)*

**NAME**

: **gcloud compute network-endpoint-groups delete - delete a Compute Engine network endpoint group**

**SYNOPSIS**

: **`gcloud compute network-endpoint-groups delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Compute Engine network endpoint group.

**EXAMPLES**

: To delete a network endpoint group named
``my-neg``:

```
gcloud compute network-endpoint-groups delete my-neg --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network endpoint group to operate on.

**FLAGS**

: **--global**

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
gcloud alpha compute network-endpoint-groups delete
```

```
gcloud beta compute network-endpoint-groups delete
```