# gcloud network-security firewall-endpoints describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe)*

**NAME**

: **gcloud network-security firewall-endpoints describe - describe a Firewall Plus endpoint**

**SYNOPSIS**

: **`gcloud network-security firewall-endpoints describe` (`[FIREWALL_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe#FIREWALL_ENDPOINT)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe#--organization)`=`ORGANIZATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a firewall endpoint.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of a firewall endpoint called `my-endpoint` in
zone `us-central1-a` and organization ID 1234, run:

```
gcloud network-security firewall-endpoints describe my-endpoint --zone=us-central1-a --organization=1234
```

OR

```
gcloud network-security firewall-endpoints describe organizations/1234/locations/us-central1-a/firewallEndpoints/my-endpoint
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
gcloud alpha network-security firewall-endpoints describe
```

```
gcloud beta network-security firewall-endpoints describe
```