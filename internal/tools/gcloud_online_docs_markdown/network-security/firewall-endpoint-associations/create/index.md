# gcloud network-security firewall-endpoint-associations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create)*

**NAME**

: **gcloud network-security firewall-endpoint-associations create - create a Firewall Plus endpoint association**

**SYNOPSIS**

: **`gcloud network-security firewall-endpoint-associations create` [`[ASSOCIATION_ID](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#ASSOCIATION_ID)`] `[--network](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--network)`=`NETWORK` `[--zone](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--zone)`=`ZONE` (`[--endpoint](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--endpoint)`=`ENDPOINT` : `[--endpoint-zone](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--endpoint-zone)`=`ENDPOINT_ZONE` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--max-wait)`=`MAX_WAIT`; default="60m"] [`[--tls-inspection-policy](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--tls-inspection-policy)`=`TLS_INSPECTION_POLICY` : `[--tls-inspection-policy-project](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--tls-inspection-policy-project)`=`TLS_INSPECTION_POLICY_PROJECT` `[--tls-inspection-policy-region](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#--tls-inspection-policy-region)`=`TLS_INSPECTION_POLICY_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Associate the specified network with the firewall endpoint. Successful creation
of a firewall endpoint association results in an association in READY state.
Check the progress of association creation by using `[gcloud
network-security firewall-endpoint-associations list](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To associate a network with a firewall endpoint, run:

```
gcloud network-security firewall-endpoint-associations create --network=projects/my-project/networks/global/myNetwork --endpoint=organizations/1234/locations/us-central1-a/firewallEndpoints/my-endpoint --zone=us-central1-a --project=my-project
```

**POSITIONAL ARGUMENTS**

: **[`ASSOCIATION_ID`]**:
Name to give the association. If not specified, an auto-generated UUID will be
used.

**REQUIRED FLAGS**

: **Network resource - Firewall Plus. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network-name` attribute:

- provide the argument `--network` on the command line.**

**--zone**:
Zone of a firewall endpoint association

**--endpoint**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--tls-inspection-policy**

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

**NOTES**

: These variants are also available:

```
gcloud alpha network-security firewall-endpoint-associations create
```

```
gcloud beta network-security firewall-endpoint-associations create
```