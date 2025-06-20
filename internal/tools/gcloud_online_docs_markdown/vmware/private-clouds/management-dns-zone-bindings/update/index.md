# gcloud vmware private-clouds management-dns-zone-bindings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update)*

**NAME**

: **gcloud vmware private-clouds management-dns-zone-bindings update - update a management DNS zone binding**

**SYNOPSIS**

: **`gcloud vmware private-clouds management-dns-zone-bindings update` (`[MANAGEMENT_DNS_ZONE_BINDING](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#MANAGEMENT_DNS_ZONE_BINDING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#--private-cloud)`=`PRIVATE_CLOUD`) `[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#--description)`=`DESCRIPTION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a management DNS zone binding.

**EXAMPLES**

: To update a management DNS zone binding called
`my-mgmt-dns-zone-binding` in private cloud
`my-private-cloud` and zone `us-west2-a` with description
`New Description`, run:

```
gcloud vmware private-clouds management-dns-zone-bindings update my-mgmt-dns-zone-binding --project=my-project --private-cloud=my-private-cloud --location=us-east2-b --description="New Description"
```

```
Or:
```

```
gcloud vmware private-clouds management-dns-zone-bindings update my-mgmt-dns-zone-binding --private-cloud=my-private-cloud --description="New Description"
```

```
In the second example, the project and location are taken from gcloud properties `core/project` and compute/zone.
```

**POSITIONAL ARGUMENTS**

: **Management DNS zone binding resource - management_dns_zone_binding. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `management_dns_zone_binding` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MANAGEMENT_DNS_ZONE_BINDING`**:
ID of the management DNS zone binding or fully qualified identifier for the
management DNS zone binding.
To set the `management-dns-zone-binding` attribute:

- provide the argument `management_dns_zone_binding` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `management_dns_zone_binding` on the command
line with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `management_dns_zone_binding` on the command
line with a fully specified name;
- provide the argument `--private-cloud` on the command line.**

**REQUIRED FLAGS**

: **--description**:
Text describing the binding resource that represents the network getting bound
to the management DNS zone.

**OPTIONAL FLAGS**

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