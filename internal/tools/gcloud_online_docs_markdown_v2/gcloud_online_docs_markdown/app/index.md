# gcloud app  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app](https://cloud.google.com/sdk/gcloud/reference/app)*

**NAME**

: **gcloud app - manage your App Engine deployments**

**SYNOPSIS**

: **`gcloud app` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/app#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud app command group lets you deploy and manage your Google App Engine
apps. These commands replace their equivalents in the appcfg tool.
App Engine is a platform for building scalable web applications and mobile
backends. App Engine provides you with built-in services and APIs such as NoSQL
datastores, memcache, and a user authentication API, common to most
applications.
More information on App Engine can be found here: [https://cloud.google.com/appengine](https://cloud.google.com/appengine)
and detailed documentation can be found here: [https://cloud.google.com/appengine/docs/](https://cloud.google.com/appengine/docs/)

**EXAMPLES**

: To run your app locally in the development application server to simulate your
application running in production App Engine with sandbox restrictions and
services provided by App Engine SDK libraries, use the
`dev_appserver.py` command and your app's `app.yaml`
configuration file to run:

```
dev_appserver.py ~/my_app/app.yaml
```

For an in-depth look into using the local development server, follow this guide
: [https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server)
To deploy the code and configuration of your app to the App Engine server, run:

```
gcloud app deploy ~/my_app/app.yaml
```

To list all versions of all services of your existing deployments, run:

```
gcloud app versions list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[domain-mappings](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings)`**:
View and manage your App Engine domain mappings.

**`[firewall-rules](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules)`**:
View and manage your App Engine firewall rules.

**`[instances](https://cloud.google.com/sdk/gcloud/reference/app/instances)`**:
View and manage your App Engine instances.

**`[logs](https://cloud.google.com/sdk/gcloud/reference/app/logs)`**:
Manage your App Engine logs.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/app/operations)`**:
View and manage your App Engine Operations.

**`[regions](https://cloud.google.com/sdk/gcloud/reference/app/regions)`**:
View regional availability of App Engine runtime environments.

**`[runtimes](https://cloud.google.com/sdk/gcloud/reference/app/runtimes)`**:
List runtimes available to Google App Engine.

**`[services](https://cloud.google.com/sdk/gcloud/reference/app/services)`**:
View and manage your App Engine services.

**`[ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/app/ssl-certificates)`**:
View and manage your App Engine SSL certificates.

**`[versions](https://cloud.google.com/sdk/gcloud/reference/app/versions)`**:
View and manage your App Engine versions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[browse](https://cloud.google.com/sdk/gcloud/reference/app/browse)`**:
Open the current app in a web browser.

**`[create](https://cloud.google.com/sdk/gcloud/reference/app/create)`**:
Create an App Engine app within the current Google Cloud Project.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy)`**:
Deploy the local code and/or configuration of your app to App Engine.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/app/describe)`**:
Display all data about an existing service.

**`[open-console](https://cloud.google.com/sdk/gcloud/reference/app/open-console)`**:
Open the App Engine dashboard, or log viewer, in a web browser.

**`[update](https://cloud.google.com/sdk/gcloud/reference/app/update)`**:
Updates an App Engine application.

**NOTES**

: These variants are also available:

```
gcloud alpha app
```

```
gcloud beta app
```