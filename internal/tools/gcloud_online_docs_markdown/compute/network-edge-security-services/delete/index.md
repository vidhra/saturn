# gcloud compute network-edge-security-services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete)*

**NAME**

: **gcloud compute network-edge-security-services delete - delete network edge security services**

**SYNOPSIS**

: **`gcloud compute network-edge-security-services delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-edge-security-services delete` deletes
Compute Engine network edge security services.

**EXAMPLES**

: To delete a network edge security service with the name 'my-service' in region
'us-central1', run:

```
gcloud compute network-edge-security-services delete my-service --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network edge security service to delete.

**FLAGS**

: **--region**:
Region of the network edge security service to delete. Overrides the default
`compute/region` property value for this command invocation.

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
gcloud alpha compute network-edge-security-services delete
```

```
gcloud beta compute network-edge-security-services delete
```