# gcloud compute network-firewall-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create)*

**NAME**

: **gcloud compute network-firewall-policies create - create a Compute Engine Network firewall policy**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies create` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create#FIREWALL_POLICY)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create#--description)`=`DESCRIPTION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies create` is used to create
network firewall policies. A network firewall policy is a set of rules that
controls access to various resources.

**EXAMPLES**

: To create a global network firewall policy named
``my-policy`` under project with ID
``test-project``, run:

```
gcloud compute network-firewall-policies create my-policy --project=test-project --global
```

To create a regional network firewall policy named
``my-region-policy`` under project with ID
``test-project``, in region
``my-region``, run:

```
gcloud compute network-firewall-policies create my-region-policy --project=test-project --region=my-region
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
name of the network firewall policy to create.

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
gcloud alpha compute network-firewall-policies create
```

```
gcloud beta compute network-firewall-policies create
```