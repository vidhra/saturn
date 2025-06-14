# gcloud preview help  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/help](https://cloud.google.com/sdk/gcloud/reference/preview/help)*

**NAME**

: **gcloud preview help - search gcloud help text**

**SYNOPSIS**

: **`gcloud preview help` [`[COMMAND](https://cloud.google.com/sdk/gcloud/reference/preview/help#COMMAND)` …] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/preview/help#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/preview/help#--limit)`=`LIMIT`; default=5] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/preview/help#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/preview/help#--sort-by)`=[`FIELD`,…]; default="~relevance"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/help#GCLOUD-WIDE-FLAGS) …`] [-- `[SEARCH_TERMS](https://cloud.google.com/sdk/gcloud/reference/preview/help#SEARCH_TERMS)` …]**

**DESCRIPTION**

: `(PREVIEW)` If a full gcloud command is specified after the
``help`` operand, gcloud preview help prints a
detailed help message for that command.
Otherwise, gcloud preview help runs a search for all commands with help text
matching the given argument or arguments. It prints the command name and a
summary of the help text for any command that it finds as a result.
To run a search directly, you can use remainder arguments, following a
`--`.
By default, command results are displayed in a table that shows the name of the
command and snippets of the help text that relate to your search terms.
By default, search results are sorted from most to least relevant by default,
using a localized rating based on several heuristics. These heuristics may
change in future runs of this command.

**EXAMPLES**

: To get the help for the command `[gcloud projects
describe](https://cloud.google.com/sdk/gcloud/reference/projects/describe)`, run:

```
gcloud preview help projects describe
```

To search for all commands whose help text contains the word
`project`, run:

```
gcloud preview help -- project
```

To search for commands whose help text contains the word `project`
and the string `--foo`, run:

```
gcloud preview help -- project --foo
```

To search and receive more than the default limit of 5 search results, run:

```
gcloud preview help --limit=20 -- project
```

To search for a term and sort the results by a different characteristic, such as
command name, run:

```
gcloud preview help --sort-by=name -- project
```

**POSITIONAL ARGUMENTS**

: **[`COMMAND` …]**:
Sequence of names representing a gcloud group or command name.
If the arguments provide the name of a gcloud command, the full help text of
that command will be displayed. Otherwise, all arguments will be considered
search terms and used to search through all of gcloud's help text.

**[-- `SEARCH_TERMS` …]**:
Search terms. The command will return a list of gcloud commands that are
relevant to the searched term. If this argument is provided, the command will
always return a list of search results rather than displaying help text of a
single command.
For example, to search for commands that relate to the term `project`
or `folder`, run:

```
gcloud preview help -- project folder
```

The '--' argument must be specified between gcloud specific args on the left and
SEARCH_TERMS on the right.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `5`. This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`. The default is `~relevance`.

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

: This command is currently in DEVELOPER PREVIEW and may change without notice. If
this command fails with API permission errors despite specifying the correct
project, you might be trying to access an API with an invitation-only early
access allowlist. These variants are also available:

```
gcloud help
```

```
gcloud alpha help
```

```
gcloud beta help
```