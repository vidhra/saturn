# gcloud vmware private-clouds external-addresses update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update)*

**NAME**

: **gcloud vmware private-clouds external-addresses update - update an external IP address in a VMware Engine private cloud**

**SYNOPSIS**

: **`gcloud vmware private-clouds external-addresses update` (`[EXTERNAL_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#EXTERNAL_ADDRESS)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#--private-cloud)`=`PRIVATE_CLOUD`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#--description)`=`DESCRIPTION`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#--internal-ip)`=`INTERNAL_IP`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an external IP address in a VMware Engine private cloud. Only
description and internal-ip can be updated.

**EXAMPLES**

: To update an external IP address called `myip` that belongs to the
private cloud `my-private-cloud` in project `my-project`
and location `us-west1-a` by changing its description to
`"Updated description for the external IP address"` and internal-ip
to `165.87.54.14`, run:

```
gcloud vmware private-clouds external-addresses update myip --project=my-project --private-cloud=my-private-cloud --location=us-west1-a --internal-ip=165.87.54.14 --description="Updated description for the external IP address"
```

Or:

```
gcloud vmware private-clouds external-addresses update myip --private-cloud=my-private-cloud --internal-ip=165.87.54.14 --description="Updated description for the external IP address"
```

In the second example, the project and region are taken from gcloud properties
core/project and vmware/region.

**POSITIONAL ARGUMENTS**

: **External address resource - external_address. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `external_address` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`EXTERNAL_ADDRESS`**:
ID of the external address or fully qualified identifier for the external
address.
To set the `external-address` attribute:

- provide the argument `external_address` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `external_address` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `external_address` on the command line with a
fully specified name;
- provide the argument `--private-cloud` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Updated description for this external address

**--internal-ip**:
Updated internal ip address for this external address

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