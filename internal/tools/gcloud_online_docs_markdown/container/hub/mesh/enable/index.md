# gcloud container hub mesh enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/enable](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/enable)*

**NAME**

: **gcloud container hub mesh enable - enable Service Mesh Feature**

**SYNOPSIS**

: **`gcloud container hub mesh enable` [`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/enable#--fleet-default-member-config)`=`FLEET_DEFAULT_MEMBER_CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/mesh/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enable the Service Mesh Feature in a fleet.

**EXAMPLES**

: To enable the Service Mesh Feature, run:

```
gcloud container hub mesh enable
```

To enable the Service Mesh Feature with a fleet-level default Membership
configuration, run:

```
gcloud container hub mesh enable --fleet-default-member-config=/path/to/service-mesh.yaml
```

**FLAGS**

: **--fleet-default-member-config**:
The path to a service-mesh.yaml configuration file.

```
To enable the Service Mesh Feature with a fleet-level default
membership configuration, run:
```

```
gcloud container hub mesh enable --fleet-default-member-config=/path/to/service-mesh.yaml
```

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
gcloud alpha container hub mesh enable
```

```
gcloud beta container hub mesh enable
```