# gcloud vmware private-clouds subnets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update)*

**NAME**

: **gcloud vmware private-clouds subnets update - update a subnet**

**SYNOPSIS**

: **`gcloud vmware private-clouds subnets update` (`[SUBNET](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update#SUBNET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update#--private-cloud)`=`PRIVATE_CLOUD`) `[--ip-cidr-range](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update#--ip-cidr-range)`=`IP_CIDR_RANGE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Subnet. Only ip-cidr-range can be updated. This is a synchronous
command and doesn't support `--async` and `--no-async`
flags.

**EXAMPLES**

: To update a subnet named `my-subnet`, that belongs to the private
cloud `my-private-cloud` in project `my-project` and zone
`us-west1-a` by changing its ip-cidr-range to
`10.0.0.0/24`, run:

```
gcloud vmware private-clouds subnets update my-subnet --private-cloud=my-private-cloud --location=us-west1 --project=my-project --ip-cidr-range=10.0.0.0/24
```

Or:

```
gcloud vmware private-clouds subnets update my-subnet --private-cloud=my-private-cloud --ip-cidr-range=10.0.0.0/24
```

In the second example, the project and location are taken from gcloud properties
`core/project` and `compute/zone`, respectively.

**POSITIONAL ARGUMENTS**

: **Subnet resource - subnet. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBNET`**:
ID of the subnet or fully qualified identifier for the subnet.
To set the `subnet` attribute:

- provide the argument `subnet` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--private-cloud` on the command line.**

**REQUIRED FLAGS**

: **--ip-cidr-range**:
Updated IP CIDR range for this subnet.

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