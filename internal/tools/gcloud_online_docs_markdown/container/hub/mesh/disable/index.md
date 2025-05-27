# gcloud container hub mesh disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/disable](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/disable)*

**NAME**

: **gcloud container hub mesh disable - disable Service Mesh Feature**

**SYNOPSIS**

: **`gcloud container hub mesh disable` [`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/disable#--fleet-default-member-config)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/disable#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Disable the Service Mesh Feature in a fleet.

**EXAMPLES**

: To disable the Service Mesh Feature, run:

```
gcloud container hub mesh disable
```

To delete the fleet-level default Membership configuration, run:

```
gcloud container hub mesh disable --fleet-default-member-config
```

**FLAGS**

: **--fleet-default-member-config**:
If specified, deletes the default membership configuration present in your
fleet.

```
To delete the fleet-level default Membership configuration present in
your fleet, run:
```

```
gcloud container hub mesh disable --fleet-default-member-config
```

**--force**:
Disable this feature, even if it is currently in use. Force disablement may
result in unexpected behavior.

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
gcloud alpha container hub mesh disable
```

```
gcloud beta container hub mesh disable
```