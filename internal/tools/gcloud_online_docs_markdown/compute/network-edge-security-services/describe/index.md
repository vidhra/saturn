# gcloud compute network-edge-security-services describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe)*

**NAME**

: **gcloud compute network-edge-security-services describe - describe a Compute Engine network edge security service**

**SYNOPSIS**

: **`gcloud compute network-edge-security-services describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-edge-security-services describe` displays all
data associated with a Compute Engine network edge security service in a
project.

**EXAMPLES**

: To describe a network edge security service with the name 'my-service' in region
'us-central1', run:

```
gcloud compute network-edge-security-services describe my-service --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network edge security service to describe.

**FLAGS**

: **--region**:
Region of the network edge security service to describe. Overrides the default
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
gcloud alpha compute network-edge-security-services describe
```

```
gcloud beta compute network-edge-security-services describe
```