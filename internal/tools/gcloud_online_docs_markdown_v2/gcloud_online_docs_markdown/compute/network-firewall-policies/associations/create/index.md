# gcloud compute network-firewall-policies associations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create)*

**NAME**

: **gcloud compute network-firewall-policies associations create - create a new association between a firewall policy and a network**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies associations create` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--firewall-policy)`=`FIREWALL_POLICY` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--network)`=`NETWORK` [`[--name](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--name)`=`NAME`] [`[--replace-association-on-target](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--replace-association-on-target)`] [`[--firewall-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--firewall-policy-region)`=`FIREWALL_POLICY_REGION`     | `[--global-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#--global-firewall-policy)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies associations create` is
used to create network firewall policy associations. A network firewall policy
is a set of rules that controls access to various resources.

**EXAMPLES**

: To associate a global network firewall policy with name
``my-policy`` to network
``my-network`` with an association named
``my-association``, run:

```
gcloud compute network-firewall-policies associations create --firewall-policy=my-policy --network=my-network --name=my-association --global-firewall-policy
```

To associate a network firewall policy with name
``my-region-policy`` in region
``region-a`` to network
``my-network`` with an association named
``my-association``, run:

```
gcloud compute network-firewall-policies associations create --firewall-policy=my-policy --network=my-network --name=my-association --firewall-policy-region=region-a
```

**REQUIRED FLAGS**

: **--firewall-policy**:
Firewall policy ID with which to create association.

**--network**:
Name of the network with which the association is created.

**OPTIONAL FLAGS**

: **--name**:
Name of the association.

**--replace-association-on-target**:
By default, if you attempt to insert an association to a network that is already
associated with a firewall policy the method will fail. If this is set, the
existing association will be deleted at the same time that the new association
is created.

**--firewall-policy-region**

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
gcloud alpha compute network-firewall-policies associations create
```

```
gcloud beta compute network-firewall-policies associations create
```