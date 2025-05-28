# gcloud domains registrations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update)*

**NAME**

: **gcloud domains registrations update - update a Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations update` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#REGISTRATION)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing registration. Currently used for updating labels only. Run:

```
gcloud help alpha domains registrations configure
```

to see how to change management, DNS or contact settings.

**EXAMPLES**

: To add a label with key ``environment`` and
value ``test`` for
``example.com``, run:

```
gcloud domains registrations update example.com --update-labels="project=example,environment=test"
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to update. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- location is always global.

This must be specified.

**`REGISTRATION`**:
ID of the registration or fully qualified identifier for the registration.
To set the `registration` attribute:

- provide the argument `registration` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha domains registrations update
```

```
gcloud beta domains registrations update
```