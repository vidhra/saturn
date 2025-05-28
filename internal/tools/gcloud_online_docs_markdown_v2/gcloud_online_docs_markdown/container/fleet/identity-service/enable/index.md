# gcloud container fleet identity-service enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/enable](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/enable)*

**NAME**

: **gcloud container fleet identity-service enable - enable the Identity Service Feature**

**SYNOPSIS**

: **`gcloud container fleet identity-service enable` [`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/enable#--fleet-default-member-config)`=`FLEET_DEFAULT_MEMBER_CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command enables the Identity Service Feature in a fleet.

**EXAMPLES**

: To enable the Identity Service Feature, run:

```
gcloud container fleet identity-service enable
```

To enable the Identity Service Feature with a fleet-level default membership
configuration, run:

```
gcloud container fleet identity-service enable --fleet-default-member-config=/path/to/identity-service.yaml
```

**FLAGS**

: **--fleet-default-member-config**:
The path to an identity-service.yaml identity configuration file. If specified,
this configuration would be the default Identity Service configuration for all
memberships in your fleet. It could be overridden with a membership-specific
configuration by using the the `Apply` command with the
`--config` argument.

```
To enable the Identity Service Feature with a fleet-level default
membership configuration, run:
```

```
gcloud container fleet identity-service enable --fleet-default-member-config=/path/to/identity-service.yaml
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
gcloud alpha container fleet identity-service enable
```

```
gcloud beta container fleet identity-service enable
```