# gcloud edge-cloud networking routers create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create)*

**NAME**

: **gcloud edge-cloud networking routers create - create a Distributed Cloud Edge Network router**

**SYNOPSIS**

: **`gcloud edge-cloud networking routers create` (`[ROUTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#ROUTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--zone)`=`ZONE`) `[--asn](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--asn)`=`ASN` `[--network](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Distributed Cloud Edge Network router.

**EXAMPLES**

: To create a router called 'my-router' with asn 65555 in edge zone
'us-central1-edge-den1', run:

```
gcloud edge-cloud networking routers create my-router --network=my-network --location=us-central1 --zone=us-central1-edge-den1 --asn=65555
```

**POSITIONAL ARGUMENTS**

: **Router resource - Distributed Cloud Edge Network router to create. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROUTER`**:
ID of the router or fully qualified identifier for the router.
To set the `router` attribute:

- provide the argument `router` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The name of the Google Distributed Cloud Edge zone.
To set the `zone` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--asn**:
The locally assigned BGP ASN.

**--network**:
The network that this subnetwork belongs to.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
An optional, textual description for the router.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

**API REFERENCE**

: This command uses the `edgenetwork/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/distributed-cloud-edge/docs](https://cloud.google.com/distributed-cloud-edge/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking routers create
```