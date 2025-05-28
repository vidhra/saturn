# gcloud network-security firewall-endpoints create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create)*

**NAME**

: **gcloud network-security firewall-endpoints create - create a Firewall Plus endpoint**

**SYNOPSIS**

: **`gcloud network-security firewall-endpoints create` (`[FIREWALL_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#FIREWALL_ENDPOINT)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--organization)`=`ORGANIZATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--zone)`=`ZONE`) `[--billing-project](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--billing-project)`=`BILLING_PROJECT` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#--max-wait)`=`MAX_WAIT`; default="60m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a firewall endpoint. Successful creation of an endpoint results in an
endpoint in READY state. Check the progress of endpoint creation by using
`[gcloud
network-security firewall-endpoints list](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To create a firewall endpoint called `my-endpoint`, in zone
`us-central1-a` and organization ID 1234, run:

```
gcloud network-security firewall-endpoints create my-endpoint --zone=us-central1-a --organization=1234
```

**POSITIONAL ARGUMENTS**

: **Firewall endpoint resource - Firewall Plus. The arguments in this group can be
used to specify the attributes of this resource.
This must be specified.

**`FIREWALL_ENDPOINT`**:
ID of the firewall endpoint or fully qualified identifier for the firewall
endpoint.
To set the `endpoint-name` attribute:

- provide the argument `FIREWALL_ENDPOINT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Organization ID of the firewall endpoint.
To set the `organization` attribute:

- provide the argument `FIREWALL_ENDPOINT` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.

**--zone**:
Zone of the firewall endpoint.
To set the `zone` attribute:

- provide the argument `FIREWALL_ENDPOINT` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--billing-project**:
The Google Cloud project ID to use for API enablement check, quota, and endpoint
uptime billing. Overrides the default `billing/quota_project`
property value for this command invocation.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the endpoint

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
gcloud alpha network-security firewall-endpoints create
```

```
gcloud beta network-security firewall-endpoints create
```