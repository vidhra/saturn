# gcloud compute network-endpoint-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe)*

**NAME**

: **gcloud compute network-endpoint-groups describe - describe a Compute Engine network endpoint group**

**SYNOPSIS**

: **`gcloud compute network-endpoint-groups describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Compute Engine network endpoint group.

**EXAMPLES**

: To describe a network endpoint group:

```
gcloud compute network-endpoint-groups describe my-neg --zone=us-central1-a
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
gcloud alpha compute network-endpoint-groups describe
```

```
gcloud beta compute network-endpoint-groups describe
```