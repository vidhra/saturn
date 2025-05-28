# gcloud functions call  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions/call](https://cloud.google.com/sdk/gcloud/reference/functions/call)*

**NAME**

: **gcloud functions call - triggers execution of a Google Cloud Function**

**SYNOPSIS**

: **`gcloud functions call` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/functions/call#NAME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/functions/call#--region)`=`REGION`) [`[--cloud-event](https://cloud.google.com/sdk/gcloud/reference/functions/call#--cloud-event)`=`CLOUD_EVENT`     | `[--data](https://cloud.google.com/sdk/gcloud/reference/functions/call#--data)`=`DATA`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions/call#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Triggers execution of a Google Cloud Function.

**EXAMPLES**

: To call a function, giving it 'Hello World!' in the message field of its event
argument (depending on your environment you might need to escape characters in
`--data` flag value differently), run:

```
gcloud functions call helloWorld --data='{"message": "Hello World!"}'
```

Note that this method has a limited quota which cannot be increased. It is
intended for testing and debugging and should not be used in production.
Calls to HTTP-triggered functions are sent as HTTP POST requests. To use other
HTTP methods, use a dedicated HTTP request tool such as cURL or wget.

**POSITIONAL ARGUMENTS**

: **Function resource - The Cloud Function name to execute. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--cloud-event**

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
gcloud alpha functions call
```

```
gcloud beta functions call
```