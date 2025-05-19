# gcloud compute networks peerings delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete)*

**NAME**

: **gcloud compute networks peerings delete - delete a Compute Engine network peering**

**SYNOPSIS**

: **`gcloud compute networks peerings delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete#--network)`=`NETWORK` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks peerings delete` deletes a Compute Engine
network peering.

**EXAMPLES**

: To delete a network peering with the name 'peering-name' on the network
'local-network', run:

```
gcloud compute networks peerings delete peering-name --network=local-network
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the peering to delete.

**REQUIRED FLAGS**

: **--network**:
The name of the network in the current project containing the peering.

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
gcloud alpha compute networks peerings delete
```

```
gcloud beta compute networks peerings delete
```