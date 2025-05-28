# gcloud alpha beyondcorp app  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app)*

**NAME**

: **gcloud alpha beyondcorp app - manages application connectors and connections**

**SYNOPSIS**

: **`gcloud alpha beyondcorp app` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud beyondcorp command group lets you secure non-gcp
application by managing connectors and connections.
BeyondCorp Enterprise offers a zero trust solution that enables secure access
with integrated threat and data protection.The solution enables secure access to
both Google Cloud Platform and on-prem hosted apps. For remote apps that are not
deployed in Google Cloud Platform, BeyondCorp Enterprise's App connector
provides simplified connectivity and app publishing experience.
More information on Beyondcorp can be found here: [https://cloud.google.com/beyondcorp](https://cloud.google.com/beyondcorp)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[connections](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections)`**:
`(ALPHA)` Create and manipulate beyondcorp connections.

**`[connectors](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors)`**:
`(ALPHA)` Create and manipulate beyondcorp connectors.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/operations)`**:
`(ALPHA)` List and Describe beyondcorp appconnector operations.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta beyondcorp app
```