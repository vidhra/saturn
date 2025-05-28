# gcloud network-connectivity regional-endpoints create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create)*

**NAME**

: **gcloud network-connectivity regional-endpoints create - create a new regional endpoint**

**SYNOPSIS**

: **`gcloud network-connectivity regional-endpoints create` (`[REGIONAL_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#REGIONAL_ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--region)`=`REGION`) `[--target-google-api](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--target-google-api)`=`TARGET_GOOGLE_API` [`[--address](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--address)`=`ADDRESS`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--description)`=`DESCRIPTION`] [`[--enable-global-access](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--enable-global-access)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--network)`=`NETWORK`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#--subnetwork)`=`SUBNETWORK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new regional endpoint with the given name.

**EXAMPLES**

: To create a regional endpoint with the name 'my-regional-endpoint' in
us-central1 targeting my-target-endpoint, run:

```
gcloud network-connectivity regional-endpoints create my-regional-endpoint --region=us-central1 [--address=my-address] [--network=my-network] [--subnetwork=my-subnet] --target-google-api=my-target-endpoint [--enable-global-access]
```

**POSITIONAL ARGUMENTS**

: **RegionalEndpoint resource - Name of the regional endpoint to be created. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `regional_endpoint` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REGIONAL_ENDPOINT`**:
ID of the regionalEndpoint or fully qualified identifier for the
regionalEndpoint.
To set the `regional_endpoint` attribute:

- provide the argument `regional_endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The location Id.
To set the `region` attribute:

- provide the argument `regional_endpoint` on the command line with a
fully specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--target-google-api**:
The service endpoint the regional endpoint will connect to.

**OPTIONAL FLAGS**

: **--address**:
The IP Address of the Regional Endpoint. When no address is provided, an IP from
the subnetwork is allocated. Use one of the following formats:

- IPv4 address as in ``10.0.0.1``
- Address resource URI as in
``projects/{project}/regions/{region}/addresses/{address_name}``
for an IPv4 or IPv6 address.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the regional endpoint.

**--enable-global-access**:
Whether the REGIONAL or GLOBAL access is enabled.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--network**:
Consumer's VPC network that this regional endpoint belongs to.

**--subnetwork**:
The name of the subnetwork from which the IP address will be allocated.

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity regional-endpoints create
```