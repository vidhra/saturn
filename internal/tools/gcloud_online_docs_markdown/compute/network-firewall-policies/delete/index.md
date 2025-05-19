# gcloud compute network-firewall-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete)*

**NAME**

: **gcloud compute network-firewall-policies delete - delete a Compute Engine network firewall policy**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies delete` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete#FIREWALL_POLICY)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies delete` is used to delete
network firewall policies. A network firewall policy is a set of rules that
controls access to various resources.

**EXAMPLES**

: To delete a global network firewall policy with name
``my-policy``, run:

```
gcloud compute network-firewall-policies delete my-policy --global
```

To delete a regional network firewall policy with name
``my-policy``, in region
``my-region``, run:

```
gcloud compute network-firewall-policies delete my-policy --region=my-region
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
name of the network firewall policy to delete.

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
gcloud alpha compute network-firewall-policies delete
```

```
gcloud beta compute network-firewall-policies delete
```