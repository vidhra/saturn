# gcloud run services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services](https://cloud.google.com/sdk/gcloud/reference/run/services)*

**NAME**

: **gcloud run services - view and manage your Cloud Run services**

**SYNOPSIS**

: **`gcloud run services` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/run/services#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/services#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing Cloud Run
services.
To create new deployments, use `[gcloud run deploy](https://cloud.google.com/sdk/gcloud/reference/run/deploy)`.

**EXAMPLES**

: To list your deployed services, run:

```
gcloud run services list
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[logs](https://cloud.google.com/sdk/gcloud/reference/run/services/logs)`**:
Read logs for Cloud Run services.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/run/services/add-iam-policy-binding)`**:
Add IAM policy binding to a Cloud Run service.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/run/services/delete)`**:
Delete a service.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/services/describe)`**:
Obtain details about a given service.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/run/services/get-iam-policy)`**:
Get the IAM policy for a Cloud Run service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/services/list)`**:
List available services.

**`[proxy](https://cloud.google.com/sdk/gcloud/reference/run/services/proxy)`**:
Proxy a service to localhost authenticating as the active account or with the
specified token.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/run/services/remove-iam-policy-binding)`**:
Remove IAM policy binding of a Cloud Run service.

**`[replace](https://cloud.google.com/sdk/gcloud/reference/run/services/replace)`**:
Create or replace a service from a YAML service specification.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/run/services/set-iam-policy)`**:
Set the IAM policy for a service.

**`[update](https://cloud.google.com/sdk/gcloud/reference/run/services/update)`**:
Update Cloud Run environment variables and other configuration settings.

**`[update-traffic](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic)`**:
Adjust the traffic assignments for a Cloud Run service.

**NOTES**

: These variants are also available:

```
gcloud alpha run services
```

```
gcloud beta run services
```