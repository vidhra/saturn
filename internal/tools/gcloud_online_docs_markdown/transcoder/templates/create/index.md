# gcloud transcoder templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create)*

**NAME**

: **gcloud transcoder templates create - create Transcoder job templates**

**SYNOPSIS**

: **`gcloud transcoder templates create` (`[TEMPLATE_ID](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#TEMPLATE_ID)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#--location)`=`LOCATION`) (`[--file](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#--file)`=`FILE`     | `[--json](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#--json)`=`JSON`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transcoder/templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create Transcoder job templates.

**EXAMPLES**

: To create a job template with json format configuration:

```
gcloud transcoder templates create TEMPLATE_ID --json="config: json-format" --location=us-central1
```

To create a job template with json format configuration file:

```
gcloud transcoder templates create TEMPLATE_ID --file="config.json" --location=us-central1
```

To create a job template with json format configuration and labels

```
gcloud transcoder templates create TEMPLATE_ID --file="config.json" --location=us-central1 --labels=key=value
```

**POSITIONAL ARGUMENTS**

: **JobTemplate resource - Transcoder job template id The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `template_id` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TEMPLATE_ID`**:
ID of the jobTemplate or fully qualified identifier for the jobTemplate.
To set the `template_id` attribute:

- provide the argument `template_id` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Transcoder location for resources
To set the `location` attribute:

- provide the argument `template_id` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `transcoder/location`.**

**REQUIRED FLAGS**

: **--file**

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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