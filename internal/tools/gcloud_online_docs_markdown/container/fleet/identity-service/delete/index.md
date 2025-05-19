# gcloud container fleet identity-service delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete)*

**NAME**

: **gcloud container fleet identity-service delete - delete a resource from the Identity Service Feature**

**SYNOPSIS**

: **`gcloud container fleet identity-service delete` [`[--fleet-default-member-config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete#--fleet-default-member-config)`] [`[--membership](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete#--membership)`=`MEMBERSHIP` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/identity-service/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a resource from the Identity Service Feature.

**EXAMPLES**

: To delete the Identity Service configuration from a membership, run:

```
gcloud container fleet identity-service delete --membership=MEMBERSHIP_NAME
```

To delete the fleet-level default membership configuration, run:

```
gcloud container fleet identity-service delete --fleet-default-member-config
```

**FLAGS**

: **--fleet-default-member-config**:
If specified, deletes the default membership configuration present in your
fleet.

```
To delete the default membership configuration present in your
fleet, run:
```

```
gcloud container fleet identity-service delete --fleet-default-member-config
```

**Membership resource - The group of arguments defining a membership. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--membership` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--membership**:
ID of the membership or fully qualified identifier for the membership.
To set the `membership` attribute:

- provide the argument `--membership` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Location for the membership.
To set the `location` attribute:

- provide the argument `--membership` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.**

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
gcloud alpha container fleet identity-service delete
```

```
gcloud beta container fleet identity-service delete
```