# gcloud vmware private-clouds dns-forwarding describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe)*

**NAME**

: **gcloud vmware private-clouds dns-forwarding describe - describe a Google Cloud VMware Engine dns-forwarding**

**SYNOPSIS**

: **`gcloud vmware private-clouds dns-forwarding describe` (`[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe#--private-cloud)`=`PRIVATE_CLOUD` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display data associated with a VMware Engine DNS forwarding, such as the domains
and their respective name servers.

**EXAMPLES**

: To describe a DNS forwarding config in private cloud
`my-private-cloud` and zone `us-west2-a`, run:

```
gcloud vmware private-clouds dns-forwarding describe --location=us-west2-a --project=my-project --private-cloud=my-private-cloud
```

```
Or:
```

```
gcloud vmware private-clouds dns-forwarding describe --private-cloud=my-private-cloud
```

```
In the second example, the project and location are taken from gcloud properties core/project and compute/zone.
```

**REQUIRED FLAGS**

: **Private cloud resource - private_cloud. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--private-cloud` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--private-cloud**:
ID of the private cloud or fully qualified identifier for the private cloud.
To set the `private-cloud` attribute:

- provide the argument `--private-cloud` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `--private-cloud` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

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