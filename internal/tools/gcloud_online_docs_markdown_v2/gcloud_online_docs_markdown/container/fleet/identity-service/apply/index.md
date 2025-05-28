# gcloud container fleet identity-service apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply)*

**NAME**

: **gcloud container fleet identity-service apply - update the Identity Service Feature**

**SYNOPSIS**

: **`gcloud container fleet identity-service apply` (`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#--fleet-default-member-config)`=`FLEET_DEFAULT_MEMBER_CONFIG` [(`[--config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#--config)`=`CONFIG` | `[--origin](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#--origin)`=`ORIGIN`) : [`[--membership](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#--membership)`=`MEMBERSHIP` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#--location)`=`LOCATION`]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates the Identity Service Feature in a fleet.

**EXAMPLES**

: To apply an Identity Service configuration to a membership, run:

```
gcloud container fleet identity-service apply --membership=MEMBERSHIP_NAME --config=/path/to/identity-service.yaml
```

To create or modify a fleet-level default membership configuration, run:

```
gcloud container fleet identity-service apply --fleet-default-member-config=/path/to/identity-service.yaml
```

To apply an existing fleet-level default membership configuration to a
membership, run:

```
gcloud container fleet identity-service apply --origin=fleet --membership=MEMBERSHIP_NAME
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
gcloud alpha container fleet identity-service apply
```

```
gcloud beta container fleet identity-service apply
```