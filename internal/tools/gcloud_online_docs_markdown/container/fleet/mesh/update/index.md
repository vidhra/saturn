# gcloud container fleet mesh update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update)*

**NAME**

: **gcloud container fleet mesh update - update the configuration of the Service Mesh Feature**

**SYNOPSIS**

: **`gcloud container fleet mesh update` (`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--fleet-default-member-config)`=`FLEET_DEFAULT_MEMBER_CONFIG`     | [(`[--origin](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--origin)`=`ORIGIN` `[--config-api](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--config-api)`=`CONFIG_API` | `[--control-plane](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--control-plane)`=`CONTROL_PLANE` | `[--management](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--management)`=`MANAGEMENT`) : [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#--location)`=`LOCATION`]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the Service Mesh Feature Spec of a Membership.

**EXAMPLES**

: To update the control plane management of comma separated Memberships like
`membership1,membership2`, run:

```
gcloud container fleet mesh update --memberships=membership1,membership2 --control-plane=CONTROL_PLANE
```

**REQUIRED FLAGS**

: **--fleet-default-member-config**

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
gcloud alpha container fleet mesh update
```

```
gcloud beta container fleet mesh update
```