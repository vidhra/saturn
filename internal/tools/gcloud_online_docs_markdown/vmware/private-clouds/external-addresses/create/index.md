# gcloud vmware private-clouds external-addresses create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create)*

**NAME**

: **gcloud vmware private-clouds external-addresses create - create an external IP address**

**SYNOPSIS**

: **`gcloud vmware private-clouds external-addresses create` (`[EXTERNAL_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#EXTERNAL_ADDRESS)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#--private-cloud)`=`PRIVATE_CLOUD`) `[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#--internal-ip)`=`INTERNAL_IP` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an external IP address that represents an allocated external IP address
and its corresponding internal IP address in the private cloud.

**EXAMPLES**

: To create an external IP address called `myip` that corresponds to
the internal IP address `165.87.54.14` that belongs to the private
cloud `my-private-cloud` in project `my-project` and
location `us-east2-b`, run:

```
gcloud vmware private-clouds external-addresses create myip --project=my-project --private-cloud=my-private-cloud --location=us-east2-b --internal-ip=165.87.54.14 --description="A short description for the new external address"
```

Or:

```
gcloud vmware private-clouds external-addresses create myip --private-cloud=my-private-cloud --internal-ip=165.87.54.14 --description="A short description for the new external address"
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

**REQUIRED FLAGS**

: **--internal-ip**:
internal ip address to which external address will be linked

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Text describing the external address

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