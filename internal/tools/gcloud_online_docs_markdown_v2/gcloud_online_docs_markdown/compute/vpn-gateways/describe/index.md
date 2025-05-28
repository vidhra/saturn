# gcloud compute vpn-gateways describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/describe](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/describe)*

**NAME**

: **gcloud compute vpn-gateways describe - describe a Compute Engine Highly Available VPN Gateway**

**SYNOPSIS**

: **`gcloud compute vpn-gateways describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/describe#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute vpn-gateways describe` is used to display all data
associated with a Compute Engine Highly Available VPN Gateway in a project.
Highly Available VPN Gateway provides a means to create a VPN solution with a
higher availability SLA compared to Classic Target VPN Gateway. Highly Available
VPN gateways are simply referred to as VPN gateways in the API documentation and
gcloud commands. A VPN Gateway can reference one or more VPN tunnels that
connect it to external VPN gateways or Cloud VPN Gateways.

**EXAMPLES**

: To describe a VPN gateway, run:

```
gcloud compute vpn-gateways describe my-gateway --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the VPN Gateway to describe.

**FLAGS**

: **--region**:
Region of the VPN Gateway to describe. If not specified, you might be prompted
to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute vpn-gateways describe
```

```
gcloud beta compute vpn-gateways describe
```