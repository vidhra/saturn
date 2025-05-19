# gcloud app versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/versions](https://cloud.google.com/sdk/gcloud/reference/app/versions)*

**NAME**

: **gcloud app versions - view and manage your App Engine versions**

**SYNOPSIS**

: **`gcloud app versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing App Engine
versions.
To create new deployments, use `[gcloud app deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy)`.
For more information on App Engine versions, see: [https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine)

**EXAMPLES**

: To list your deployed versions, run:

```
gcloud app versions list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[browse](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse)`**:
Open the specified versions in a browser.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete)`**:
Delete a specified version.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/app/versions/describe)`**:
Display all data about an existing version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/app/versions/list)`**:
List your existing versions.

**`[migrate](https://cloud.google.com/sdk/gcloud/reference/app/versions/migrate)`**:
Migrate traffic from one version to another for a set of services.

**`[start](https://cloud.google.com/sdk/gcloud/reference/app/versions/start)`**:
Start serving specified versions.

**`[stop](https://cloud.google.com/sdk/gcloud/reference/app/versions/stop)`**:
Stop serving specified versions.

**NOTES**

: This variant is also available:

```
gcloud beta app versions
```