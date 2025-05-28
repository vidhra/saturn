# gcloud app services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/services](https://cloud.google.com/sdk/gcloud/reference/app/services)*

**NAME**

: **gcloud app services - view and manage your App Engine services**

**SYNOPSIS**

: **`gcloud app services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing App Engine
services.
To create new deployments, use `[gcloud app deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy)`.
For more information on App Engine services, see: [https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine)

**EXAMPLES**

: To list your deployed services, run:

```
gcloud app services list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[browse](https://cloud.google.com/sdk/gcloud/reference/app/services/browse)`**:
Open the specified service(s) in a browser.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/app/services/delete)`**:
Delete services in the current project.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/app/services/describe)`**:
Display all data about an existing service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/app/services/list)`**:
List your existing services.

**`[set-traffic](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic)`**:
Set traffic splitting settings.

**`[update](https://cloud.google.com/sdk/gcloud/reference/app/services/update)`**:
Update service-level settings.

**NOTES**

: This variant is also available:

```
gcloud beta app services
```