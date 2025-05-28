# gcloud app firewall-rules test-ip  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/test-ip](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/test-ip)*

**NAME**

: **gcloud app firewall-rules test-ip - display firewall rules that match a given IP**

**SYNOPSIS**

: **`gcloud app firewall-rules test-ip` `[IP](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/test-ip#IP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/test-ip#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display firewall rules that match a given IP.

**EXAMPLES**

: To test an IP address against the firewall rule set, run:

```
gcloud app firewall-rules test-ip 127.1.2.3
```

**POSITIONAL ARGUMENTS**

: **`IP`**:
An IPv4 or IPv6 address to test against the firewall.

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

: This variant is also available:

```
gcloud beta app firewall-rules test-ip
```