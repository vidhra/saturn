# gcloud init  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/init](https://cloud.google.com/sdk/gcloud/reference/init)*

**NAME**

: **gcloud init - initialize or reinitialize gcloud**

**SYNOPSIS**

: **`gcloud init` [`[--no-browser](https://cloud.google.com/sdk/gcloud/reference/init#--browser)`] [`[--console-only](https://cloud.google.com/sdk/gcloud/reference/init#--console-only)`, `[--no-launch-browser](https://cloud.google.com/sdk/gcloud/reference/init#--launch-browser)`] [`[--skip-diagnostics](https://cloud.google.com/sdk/gcloud/reference/init#--skip-diagnostics)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/init#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud init launches an interactive Getting Started workflow for the gcloud
command-line tool. It performs the following setup steps:

- Authorizes gcloud and other SDK tools to access Google Cloud using your user
account credentials, or from an account of your choosing whose credentials are
already available.
- Sets up a new or existing configuration.
- Sets properties in that configuration, including the current project and
optionally, the default Google Compute Engine region and zone you'd like to use.

gcloud init can be used for initial setup of gcloud and to create new or
reinitialize gcloud configurations. More information about configurations can be
found by running `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)`.
Properties set by gcloud init are local and persistent, and are not affected by
remote changes to the project. For example, the default Compute Engine zone in
your configuration remains stable, even if you or another user changes the
project-level default zone in the Cloud Platform Console.
To sync the configuration, re-run `gcloud init`.

**EXAMPLES**

: To launch an interactive Getting Started workflow, run:

```
gcloud init
```

To launch an interactive Getting Started workflow without diagnostics, run:

```
gcloud init --skip-diagnostics
```

**FLAGS**

: **--no-browser**:
Prevent the command from launching a browser for authorization. Use this flag if
you are on a machine that does not have a browser but you can install the gcloud
CLI on another machine with a browser.

**--console-only**:
Prevent the command from launching a browser for authorization. Use this flag if
you are on a machine that does not have a browser and you cannot install the
gcloud CLI on another machine with a browser.

**--skip-diagnostics**:
Do not run diagnostics.

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
gcloud alpha init
```

```
gcloud beta init
```

```
gcloud preview init
```