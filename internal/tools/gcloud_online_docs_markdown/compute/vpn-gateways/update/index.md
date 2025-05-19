# gcloud compute vpn-gateways update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update)*

**NAME**

: **gcloud compute vpn-gateways update - update a Compute Engine Highly Available VPN gateway**

**SYNOPSIS**

: **`gcloud compute vpn-gateways update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#--region)`=`REGION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute vpn-gateways update` updates labels for a Compute
Engine Highly Available VPN gateway.
For example:

```
gcloud compute vpn-gateways update example-gateway --region us-central1 --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

will add/update labels ``k0`` and
``k1`` and remove labels with key
``k3``.
Labels can be used to identify the VPN gateway and to filter them as in

```
gcloud compute vpn-gateways list --filter='labels.k1:value2'
```

To list existing labels

```
gcloud compute vpn-gateways describe example-gateway --format="default(labels)"
```

**EXAMPLES**

: To update labels for a VPN gateway, run:

```
gcloud compute vpn-gateways update my-gateway --region=us-central1 --update-labels=k0=value1,k1=value2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the VPN Gateway to update.

**FLAGS**

: **--region**:
Region of the VPN Gateway to update. If not specified, you might be prompted to
select a region (interactive mode only).
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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha compute vpn-gateways update
```

```
gcloud beta compute vpn-gateways update
```