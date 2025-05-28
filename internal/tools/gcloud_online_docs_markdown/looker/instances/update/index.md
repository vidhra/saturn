# gcloud looker instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/instances/update](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update)*

**NAME**

: **gcloud looker instances update - update a Looker instance**

**SYNOPSIS**

: **`gcloud looker instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--region)`=`REGION`) [`[--allowed-email-domains](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--allowed-email-domains)`=[`ALLOWED_EMAIL_DOMAINS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--async)`] [`[--custom-domain](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--custom-domain)`=`CUSTOM_DOMAIN`] [`[--linked-lsp-project-number](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--linked-lsp-project-number)`=`LINKED_LSP_PROJECT_NUMBER`] [`[--public-ip-enabled](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--public-ip-enabled)`] [`[--add-developer-users](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--add-developer-users)`=`ADD_DEVELOPER_USERS` `[--add-standard-users](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--add-standard-users)`=`ADD_STANDARD_USERS` `[--add-viewer-users](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--add-viewer-users)`=`ADD_VIEWER_USERS`] [`[--clear-psc-allowed-vpcs](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--clear-psc-allowed-vpcs)`     | `[--psc-allowed-vpcs](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--psc-allowed-vpcs)`=[`PSC_ALLOWED_VPCS`,…] `[--clear-psc-service-attachments](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--clear-psc-service-attachments)`     | `[--psc-service-attachment](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--psc-service-attachment)`=[`attachment`=`ATTACHMENT`],[`domain`=`DOMAIN`]] [`[--deny-maintenance-period-end-date](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--deny-maintenance-period-end-date)`=`DENY_MAINTENANCE_PERIOD_END_DATE` `[--deny-maintenance-period-start-date](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--deny-maintenance-period-start-date)`=`DENY_MAINTENANCE_PERIOD_START_DATE` `[--deny-maintenance-period-time](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--deny-maintenance-period-time)`=`DENY_MAINTENANCE_PERIOD_TIME`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-time](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--maintenance-window-time)`=`MAINTENANCE_WINDOW_TIME`] [`[--oauth-client-id](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--oauth-client-id)`=`OAUTH_CLIENT_ID` `[--oauth-client-secret](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#--oauth-client-secret)`=`OAUTH_CLIENT_SECRET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the metadata and/or configuration parameters of a Looker instance.
This command can fail for the following reasons:

- The instance specified does not exist.
- The active account does not have permission to update the given instance.

**EXAMPLES**

: To update the maintenance window to Sunday at 11:00 PM for a Looker instance
with the name `my-looker-instance`, run:

```
gcloud looker instances update my-looker-instance --maintenance-window-day=sunday --maintenance-window-time='23:00' --async
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Looker instance you
want to update. The arguments in this group can be used to specify the
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

**FLAGS**

: **--allowed-email-domains**

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--custom-domain**

**--linked-lsp-project-number**:
The Looker Studio Pro project number to be linked.

**--public-ip-enabled**:
This specifies whether public IP is enabled on the Looker instance.

**--add-developer-users**

**--clear-psc-allowed-vpcs**

**--deny-maintenance-period-end-date**

**--maintenance-window-day**

**OAuth Application Credentials - Looker Instance OAuth login settings. Setup an
OAuth app that will allow users to authenticate and access the instance. For
more information see: [https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred)

**--oauth-client-id`=`OAUTH_CLIENT_ID``**:
The client ID from an external OAuth application.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--oauth-client-secret`=`OAUTH_CLIENT_SECRET``**:
The client secret from an external OAuth application.
This flag argument must be specified if any of the other arguments in this group
are specified.**

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
gcloud alpha looker instances update
```