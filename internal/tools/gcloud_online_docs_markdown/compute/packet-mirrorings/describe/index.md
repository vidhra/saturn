# gcloud compute packet-mirrorings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe)*

**NAME**

: **gcloud compute packet-mirrorings describe - describe a Compute Engine packet mirroring policy**

**SYNOPSIS**

: **`gcloud compute packet-mirrorings describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Compute Engine Packet Mirroring policy.

**EXAMPLES**

: Describe the Packet Mirroring policy pm-1 in region us-central1.

```
gcloud compute packet-mirrorings describe pm-1 --region us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the packet mirroring to describe.

**FLAGS**

: **--region**:
Region of the packet mirroring to describe. Overrides the default
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
gcloud alpha compute packet-mirrorings describe
```

```
gcloud beta compute packet-mirrorings describe
```