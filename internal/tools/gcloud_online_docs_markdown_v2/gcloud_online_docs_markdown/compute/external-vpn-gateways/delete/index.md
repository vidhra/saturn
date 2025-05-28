# gcloud compute external-vpn-gateways delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/delete](https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/delete)*

**NAME**

: **gcloud compute external-vpn-gateways delete - delete a Compute Engine external VPN gateway**

**SYNOPSIS**

: **`gcloud compute external-vpn-gateways delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/delete#NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute external-vpn-gateways delete` is used to delete all
data associated with a Compute Engine external VPN gateway in a project.
An external VPN gateway provides the information to Google Cloud about your
on-premises side or another Cloud provider's VPN gateway.

**EXAMPLES**

: To delete an external VPN gateway, run:

```
gcloud compute external-vpn-gateways delete my-external-gateway
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the external VPN gateways to delete.

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
gcloud alpha compute external-vpn-gateways delete
```

```
gcloud beta compute external-vpn-gateways delete
```