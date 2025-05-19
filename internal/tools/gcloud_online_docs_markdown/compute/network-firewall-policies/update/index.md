# gcloud compute network-firewall-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update)*

**NAME**

: **gcloud compute network-firewall-policies update - update a Compute Engine network firewall policy**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies update` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update#FIREWALL_POLICY)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update#--description)`=`DESCRIPTION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies update` is used to update
network firewall policies. A network firewall policy is a set of rules that
controls access to various resources.

**EXAMPLES**

: To update a global network firewall policy with name
``my-policy``, to change the description to
``New description``, run:

```
gcloud compute network-firewall-policies update my-policy --description='New description' --global
```

To update a regional network firewall policy with name
``my-policy``, in region
``my-region``, to change the description to
``New description``, run:

```
gcloud compute network-firewall-policies update my-policy --description='New description' --region=my-region
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
name of the network firewall policy to update.

**FLAGS**

: **--description**:
An optional, textual description for the network firewall policy.

**--global**

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
gcloud alpha compute network-firewall-policies update
```

```
gcloud beta compute network-firewall-policies update
```