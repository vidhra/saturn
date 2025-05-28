# gcloud compute networks delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete)*

**NAME**

: **gcloud compute networks delete - delete Compute Engine networks**

**SYNOPSIS**

: **`gcloud compute networks delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete#NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks delete` deletes one or more Compute Engine
networks. Networks can only be deleted when no other resources (e.g., virtual
machine instances) refer to them.

**EXAMPLES**

: To delete a network with the name 'network-name', run:

```
gcloud compute networks delete network-name
```

To delete two networks with the names 'network-name1' and 'network-name2', run:

```
gcloud compute networks delete network-name1 network-name2
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the networks to delete.

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
gcloud alpha compute networks delete
```

```
gcloud beta compute networks delete
```