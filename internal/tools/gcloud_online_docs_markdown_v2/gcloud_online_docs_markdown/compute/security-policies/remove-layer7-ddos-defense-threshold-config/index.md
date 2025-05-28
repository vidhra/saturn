# gcloud compute security-policies remove-layer7-ddos-defense-threshold-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config)*

**NAME**

: **gcloud compute security-policies remove-layer7-ddos-defense-threshold-config - remove a layer7 ddos defense threshold config from a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies remove-layer7-ddos-defense-threshold-config` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config#NAME)` `[--threshold-config-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config#--threshold-config-name)`=`THRESHOLD_CONFIG_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies
remove-layer7-ddos-defense-threshold-config` is used to remove layer7 ddos
defense threshold configs from security policies.

**EXAMPLES**

: To remove a layer7 ddos defense threshold config run the following command:

```
gcloud compute security-policies remove-layer7-ddos-defense-threshold-config NAME --threshold-config-name=my-threshold-config-name
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to update.

**REQUIRED FLAGS**

: **--threshold-config-name**:
The name for the threshold config.

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
gcloud alpha compute security-policies remove-layer7-ddos-defense-threshold-config
```

```
gcloud beta compute security-policies remove-layer7-ddos-defense-threshold-config
```