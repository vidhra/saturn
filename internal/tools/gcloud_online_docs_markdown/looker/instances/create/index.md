# gcloud looker instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/instances/create](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create)*

**NAME**

: **gcloud looker instances create - create a Looker instance**

**SYNOPSIS**

: **`gcloud looker instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--region)`=`REGION`) `[--edition](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--edition)`=`EDITION` `[--oauth-client-id](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--oauth-client-id)`=`OAUTH_CLIENT_ID` `[--oauth-client-secret](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--oauth-client-secret)`=`OAUTH_CLIENT_SECRET` [`[--async](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--async)`] [`[--fips-enabled](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--fips-enabled)`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--kms-key)`=`KMS_KEY`] [`[--no-public-ip-enabled](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--public-ip-enabled)`] [`[--consumer-network](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--consumer-network)`=`CONSUMER_NETWORK` `[--private-ip-enabled](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--private-ip-enabled)` : `[--reserved-range](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--reserved-range)`=`RESERVED_RANGE`] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE` `[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE` `[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-time](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--maintenance-window-time)`=`MAINTENANCE_WINDOW_TIME`] [`[--psc-enabled](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--psc-enabled)` : `[--psc-allowed-vpcs](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#--psc-allowed-vpcs)`=[`PSC_ALLOWED_VPCS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Looker instance.
This command can fail for the following reasons:

- An instance with the same name already exists.
- The active account does not have permission to create instances.
- `--async` flag is not passed

**EXAMPLES**

: To create a basic tier instance with the name `my-looker-instance` in
region `us-central-1` with an edition of
`LOOKER_CORE_STANDARD`, run:

```
gcloud looker instances create my-looker-instance --region=us-central1 --edition="core-standard" --oauth-client-id='looker' --oauth-client-secret='looker' --async
```

Note: It is `recommended` that the `--async` argument is
provided when creating a Looker instance.

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Looker instance you
want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Looker region of the instance. Overrides the default
looker/region property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `looker/region`.**

**REQUIRED FLAGS**

: **--edition**:
The edition of the Looker instance. `EDITION` must be one
of:

**`core-embed-annual`**:
A Looker (Google Cloud core) product for deploying and maintaining external
analytics and custom applications at scale. This can be purchased via an annual
contract.

**`core-enterprise-annual`**:
A Looker (Google Cloud core) product with enhanced security features for a wide
variety of internal BI and analytics use cases. This can be purchased via an
annual contract.

**`core-standard`**:
A Looker (Google Cloud core) product for small organizations or teams with fewer
than 50 users. This will be billed monthly while the instance is active.

**`core-standard-annual`**:
A Looker (Google Cloud core) product for small organizations or teams with fewer
than 50 users. This can be purchased via an annual contract.

**`core-trial`**:
Trial edition of Looker.

**`nonprod-core-embed-annual`**:
A non-production edition of Looker (Google Cloud core) product for deploying and
maintaining external analytics and custom applications at scale. This can be
purchased via an annual contract.

**`nonprod-core-enterprise-annual`**:
A non-production edition of Looker (Google Cloud core) product with enhanced
security features for a wide variety of internal BI and analytics use cases.
This can be purchased via an annual contract.

**`nonprod-core-standard-annual`**:
A non-production edition of Looker (Google Cloud core) product for small
organizations or teams with fewer than 50 users. This can be purchased via an
annual contract.

**--oauth-client-id**:
The client ID from an external OAuth application.
OAuth Application Credentials - Looker Instance OAuth login settings. Setup an
OAuth app that will allow users to authenticate and access the instance. For
more information see: [https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred)

**--oauth-client-secret**:
The client secret from an external OAuth application.
OAuth Application Credentials - Looker Instance OAuth login settings. Setup an
OAuth app that will allow users to authenticate and access the instance. For
more information see: [https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred)

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--fips-enabled**:
This specifies whether FIPS is enabled on the Looker instance.

**--kms-key**

**--public-ip-enabled**:
This specifies whether public IP is enabled on the Looker instance. Enabled by
default, use `--no-public-ip-enabled` to disable.

**Private IP - Assigns an internal, Google-hosted VPC IP address. Private IP
connectivity requires additional APIs and permissions. Private IP cannot be
disabled once it has been enabled. If enabled, `consumer-network`
must be assigned.

**--consumer-network**:
The network name within the consumer project. This MUST be delared if enabling
private IP.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--private-ip-enabled**:
This specifies whether private IP is enabled on the Looker instance.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--reserved-range**:
The name of a reserved IP address range within the consumer network to be used
for private service access connection.**

**--deny-maintenance-period-end-date**

**--maintenance-window-day**

**--psc-enabled**

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

**API REFERENCE**

: This command uses the `looker/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/looker/docs/reference/rest/](https://cloud.google.com/looker/docs/reference/rest/)

**NOTES**

: This variant is also available:

```
gcloud alpha looker instances create
```