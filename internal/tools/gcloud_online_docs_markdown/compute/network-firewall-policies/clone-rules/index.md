# gcloud compute network-firewall-policies clone-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules)*

**NAME**

: **gcloud compute network-firewall-policies clone-rules - replace the rules of a Compute Engine network firewall policy with rules from another policy**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies clone-rules` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules#FIREWALL_POLICY)` `[--source-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules#--source-firewall-policy)`=`SOURCE_FIREWALL_POLICY` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/clone-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies clone-rules` is used to
replace the rules of network firewall policies. A network firewall policy is a
set of rules that controls access to various resources.

**EXAMPLES**

: To clone the rules of a global network firewall policy with NAME
``my-policy``, from another network firewall
policy with NAME ``source-policy``, run:

```
gcloud compute network-firewall-policies clone-rules my-policy --source-firewall-policy=source-policy --global
```

To clone the rules of a region network firewall policy with NAME
``my-region-policy``, in region
``region-a``, from another network firewall
policy with NAME ``source-policy``, run:

```
gcloud compute network-firewall-policies clone-rules my-region-policy --source-firewall-policy=source-policy --region=region-a
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
name of the network firewall policy to clone the rules to.

**REQUIRED FLAGS**

: **--source-firewall-policy**:
Name of the source network firewall policy to copy the rules from.

**OPTIONAL FLAGS**

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
gcloud alpha compute network-firewall-policies clone-rules
```

```
gcloud beta compute network-firewall-policies clone-rules
```