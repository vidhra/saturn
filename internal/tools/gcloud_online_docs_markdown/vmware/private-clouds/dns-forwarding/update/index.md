# gcloud vmware private-clouds dns-forwarding update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update)*

**NAME**

: **gcloud vmware private-clouds dns-forwarding update - update a Google Cloud VMware Engine dns-forwarding**

**SYNOPSIS**

: **`gcloud vmware private-clouds dns-forwarding update` (`[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#--private-cloud)`=`PRIVATE_CLOUD` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#--async)`] [`[--rule](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#--rule)`=[`domain`=`DOMAIN`,`name-servers`="`[NAME_SERVER1](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#NAME_SERVER1)`;`[NAME_SERVER2](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#NAME_SERVER2)`[;`[NAME_SERVER3](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#NAME_SERVER3)`]",…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update DNS forwarding.

**EXAMPLES**

: To update a DNS forwarding config in private cloud `my-private-cloud`
and zone `us-west2-a` to forward DNS requests for domain
`activedirectory.my.corp` to name servers `192.168.20.15`
and `192.168.20.16` and for domain `proxy.my.corp` to
nameservers `192.168.30.15` and `192.168.30.16`, run:

```
gcloud vmware private-clouds dns-forwarding update --location=us-west2-a --project=my-project --private-cloud=my-private-cloud --rule=domain=activedirectory.my.corp,name-servers=192.168.20.15;192.168.20.16 --rule=domain=proxy.my.corp,name-servers=192.168.30.15;192.168.30.16
```

```
Or:
```

```
gcloud vmware private-clouds dns-forwarding update --private-cloud=my-private-cloud --rule=domain=activedirectory.my.corp,name-servers=192.168.20.15;192.168.20.16 --rule=domain=proxy.my.corp,name-servers=192.168.30.15;192.168.30.16
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

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--rule**:
Domain name and the name servers used to resolve DNS requests for this domain.

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