# gcloud functions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions](https://cloud.google.com/sdk/gcloud/reference/functions)*

**NAME**

: **gcloud functions - manage Google Cloud Functions**

**SYNOPSIS**

: **`gcloud functions` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/functions#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/functions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Google Cloud Functions.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[event-types](https://cloud.google.com/sdk/gcloud/reference/functions/event-types)`**:
List types of events that can be a trigger for a Google Cloud Function.

**`[logs](https://cloud.google.com/sdk/gcloud/reference/functions/logs)`**:
Display log entries produced by Google Cloud Functions.

**`[regions](https://cloud.google.com/sdk/gcloud/reference/functions/regions)`**:
List regions available to Google Cloud Functions.

**`[runtimes](https://cloud.google.com/sdk/gcloud/reference/functions/runtimes)`**:
List runtimes available to Google Cloud Functions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/functions/add-iam-policy-binding)`**:
Adds an IAM policy binding for a Google Cloud Function.

**`[add-invoker-policy-binding](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding)`**:
Adds an invoker binding to the IAM policy of a Google Cloud Function.

**`[call](https://cloud.google.com/sdk/gcloud/reference/functions/call)`**:
Triggers execution of a Google Cloud Function.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/functions/delete)`**:
Delete a Google Cloud Function.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/functions/deploy)`**:
Create or update a Google Cloud Function.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/functions/describe)`**:
Display details of a Google Cloud Function.

**`[detach](https://cloud.google.com/sdk/gcloud/reference/functions/detach)`**:
Detach a Cloud Functions v2 function from its existing environment and make it a
native Cloud Run function.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/functions/get-iam-policy)`**:
Get IAM policy for a Google Cloud Function.

**`[list](https://cloud.google.com/sdk/gcloud/reference/functions/list)`**:
List Google Cloud Functions.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/functions/remove-iam-policy-binding)`**:
Removes an IAM policy binding from a Google Cloud Function.

**`[remove-invoker-policy-binding](https://cloud.google.com/sdk/gcloud/reference/functions/remove-invoker-policy-binding)`**:
Removes an invoker binding from the IAM policy of a Google Cloud Function.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/functions/set-iam-policy)`**:
Sets IAM policy for a Google Cloud Function.

**NOTES**

: These variants are also available:

```
gcloud alpha functions
```

```
gcloud beta functions
```