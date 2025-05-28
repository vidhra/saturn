# gcloud vmware network-policies external-access-rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete)*

**NAME**

: **gcloud vmware network-policies external-access-rules delete - delete a VMware Engine external access rule**

**SYNOPSIS**

: **`gcloud vmware network-policies external-access-rules delete` (`[EXTERNAL_ACCESS_RULE](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete#EXTERNAL_ACCESS_RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete#--location)`=`LOCATION` `[--network-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete#--network-policy)`=`NETWORK_POLICY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a VMware Engine external access firewall rule.

**EXAMPLES**

: To delete an external access firewall rule called
`my-external-access-rule` in project `my-project` and
region `us-west2` associated with network policy
`my-network-policy`, run:

```
gcloud vmware network-policies external-access-rules delete my-external-access-rule --location=us-west2 --project=my-project --network-policy=my-network-policy
```

Or:

```
gcloud vmware network-policies external-access-rules delete my-external-access-rule --network-policy=my-network-policy
```

In the second example, the project and the location are taken from gcloud
properties core/project and compute/region respectively.

**POSITIONAL ARGUMENTS**

: **VMware Engine External Access Rule resource - external_access_rule. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EXTERNAL_ACCESS_RULE`**:
ID of the VMware Engine External Access Rule or fully qualified identifier for
the VMware Engine External Access Rule.
To set the `external-access-rule` attribute:

- provide the argument `external_access_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.

**--network-policy**:
VMware Engine network policy
To set the `network-policy` attribute:

- provide the argument `external_access_rule` on the command line with
a fully specified name;
- provide the argument `--network-policy` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

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