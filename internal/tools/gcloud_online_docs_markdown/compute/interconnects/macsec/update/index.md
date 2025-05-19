# gcloud compute interconnects macsec update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update)*

**NAME**

: **gcloud compute interconnects macsec update - update a Compute Engine interconnect MACsec configuration**

**SYNOPSIS**

: **`gcloud compute interconnects macsec update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update#NAME)` [`[--enabled](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update#--enabled)`] [`[--fail-open](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update#--fail-open)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects macsec update` is used to update MACsec
configuration of interconnect. An interconnect represents a single specific
connection between Google and the customer.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To enable MACsec on an interconnect, run:

```
gcloud compute interconnects macsec update example-interconnect --enabled
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect to update.

**FLAGS**

: **--enabled**:
Enable or disable MACsec on this Interconnect. MACsec enablement will fail if
the MACsec configuration is not specified. Use --no-enabled to disable it.

**--fail-open**:
If enabled, the Interconnect will be configured with a should-secure MACsec
security policy, that allows the Google router to fallback to cleartext traffic
if the MKA session cannot be established. By default, the Interconnect will be
configured with a must-secure security policy that drops all traffic if the MKA
session cannot be established with your router. Use --no-fail-open to disable
it.

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
gcloud alpha compute interconnects macsec update
```

```
gcloud beta compute interconnects macsec update
```