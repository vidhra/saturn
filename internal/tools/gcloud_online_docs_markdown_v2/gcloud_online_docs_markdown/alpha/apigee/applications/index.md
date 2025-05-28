# gcloud alpha apigee applications  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications)*

**NAME**

: **gcloud alpha apigee applications - manage third-party applications which call Apigee API proxies**

**SYNOPSIS**

: **`gcloud alpha apigee applications` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage third-party applications which call Apigee API
proxies.
`gcloud alpha apigee applications` manages applications that want to
use APIs exposed via Apigee.

**EXAMPLES**

: To get the names and UUIDs of all applications in the active Cloud Platform
project, run:

```
gcloud alpha apigee applications list
```

To get a JSON representation of an application in the active Cloud Platform
project, including its API keys, run:

```
gcloud alpha apigee applications describe APP_UUID --format=json
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe)`**:
`(ALPHA)` Describe an Apigee application.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list)`**:
`(ALPHA)` List Apigee applications.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee applications
```

```
gcloud beta apigee applications
```