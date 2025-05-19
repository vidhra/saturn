# gcloud compute network-firewall-policies mirroring-rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete)*

**NAME**

: **gcloud compute network-firewall-policies mirroring-rules delete - deletes a Compute Engine network firewall policy packet mirroirng rule**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies mirroring-rules delete` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete#PRIORITY)` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete#--firewall-policy)`=`FIREWALL_POLICY` `[--global-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete#--global-firewall-policy)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies mirroring-rules delete` is
used to delete network firewall policy packet mirroring rules.

**EXAMPLES**

: To delete a rule with priority ``10`` in a
global network firewall policy with name
``my-policy``, run:

```
gcloud compute network-firewall-policies mirroring-rules delete 10 --firewall-policy=my-policy --global-firewall-policy
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the rule to be deleted. Valid in [0, 65535].

**REQUIRED FLAGS**

: **--firewall-policy**:
Firewall policy ID with which to delete rule.

**--global-firewall-policy**:
Use this flag to indicate that firewall policy is global.

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
gcloud alpha compute network-firewall-policies mirroring-rules delete
```

```
gcloud beta compute network-firewall-policies mirroring-rules delete
```