# gcloud vmware private-clouds subnets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe)*

**NAME**

: **gcloud vmware private-clouds subnets describe - describe a subnet in a VMware Engine private cloud**

**SYNOPSIS**

: **`gcloud vmware private-clouds subnets describe` (`[SUBNET](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe#SUBNET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe#--private-cloud)`=`PRIVATE_CLOUD`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Subnet by its resource name. It contains details of the subnet, such
as ip_cidr_range, gateway_ip, state, and type.

**EXAMPLES**

: To get the information about a subnet resource called `my-subnet`,
that belongs to the private cloud `my-private-cloud` in project
`my-project` and zone `us-west1-a`, run:

```
gcloud vmware private-clouds subnets describe my-subnet --private-cloud=my-private-cloud --location=us-west1-a --project=my-project
```

Or:

```
gcloud vmware private-clouds subnets describe my-subnet --private-cloud=my-private-cloud
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