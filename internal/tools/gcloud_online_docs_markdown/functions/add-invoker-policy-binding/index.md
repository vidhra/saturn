# gcloud functions add-invoker-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding)*

**NAME**

: **gcloud functions add-invoker-policy-binding - adds an invoker binding to the IAM policy of a Google Cloud Function**

**SYNOPSIS**

: **`gcloud functions add-invoker-policy-binding` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding#NAME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding#--region)`=`REGION`) `[--member](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding#--member)`=`PRINCIPAL` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adds an invoker role IAM policy binding that allows the specified member to
invoke the specified function.
For Cloud Functions (1st gen), this adds the Cloud Functions Invoker binding to
the IAM policy of the specified function.
For Cloud Functions (2nd gen), this adds the Cloud Run Invoker binding to the
IAM policy of the specified function's underlying Cloud Run service.

**EXAMPLES**

: To add the invoker role policy binding for `FUNCTION-1` for member
`MEMBER-1` run:

```
gcloud functions add-invoker-policy-binding FUNCTION-1 --member=MEMBER-1
```

**POSITIONAL ARGUMENTS**

: **Function resource - The Cloud Function name to add the invoker binding to. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the function or fully qualified identifier for the function.
To set the `function` attribute:

- provide the argument `NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the function. Overrides the default
`functions/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `functions/region`.**

**REQUIRED FLAGS**

: **--member**:
The principal to add to the IAM policy. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

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
gcloud alpha functions add-invoker-policy-binding
```

```
gcloud beta functions add-invoker-policy-binding
```