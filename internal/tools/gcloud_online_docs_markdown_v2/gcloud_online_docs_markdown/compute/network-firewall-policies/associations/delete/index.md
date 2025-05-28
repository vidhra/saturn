# gcloud compute network-firewall-policies associations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete)*

**NAME**

: **gcloud compute network-firewall-policies associations delete - delete a new association between a firewall policy and an network or folder resource**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies associations delete` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete#--firewall-policy)`=`FIREWALL_POLICY` `[--name](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete#--name)`=`NAME` [`[--firewall-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete#--firewall-policy-region)`=`FIREWALL_POLICY_REGION`     | `[--global-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete#--global-firewall-policy)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies associations delete` is
used to delete network firewall policy associations. An network firewall policy
is a set of rules that controls access to various resources.

**EXAMPLES**

: To delete an association from a global network firewall policy with NAME
``my-policy`` and association name
``my-association``, run:

```
gcloud compute network-firewall-policies associations delete --firewall-policy=my-policy --name=my-association --global-firewall-policy
```

To delete an association from a regional network firewall policy with NAME
``my-policy`` in region
``region-a`` and association name
``my-association``, run:

```
gcloud compute network-firewall-policies associations delete --firewall-policy=my-policy --name=my-association --firewall-policy-region=region-a
```

**REQUIRED FLAGS**

: **--firewall-policy**:
Firewall policy ID with which to delete association.

**--name**:
Name of the association to delete.

**OPTIONAL FLAGS**

: **--firewall-policy-region**

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
gcloud alpha compute network-firewall-policies associations delete
```

```
gcloud beta compute network-firewall-policies associations delete
```