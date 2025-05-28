# gcloud topic cli-trees  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/topic/cli-trees](https://cloud.google.com/sdk/gcloud/reference/topic/cli-trees)*

**NAME**

: **gcloud topic cli-trees - CLI trees supplementary help**

**DESCRIPTION**

: CLI trees are static nested dictionaries that describe all of the groups,
commands, flags, positionals, help text, and completer module paths for a CLI. A
CLI tree is often much faster to load and access than one generated at runtime
from an active CLI. It is also a more compact representation. A properly formed
CLI tree can be used to reproduce the help documentation for an entire CLI.

**CLI Tree Data Files**

: A CLI tree is a dictionary in a JSON file. By convention, the file base name is
the corresponding CLI name. For example, the CLI tree file name for `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` is `gcloud.json`.
CLI trees associated with Google Cloud CLI modules are installed in the
`data/cli` subdirectory of the Google Cloud CLI installation root:

```
$(gcloud info --format="value(installation.sdk_root)")/data/cli
```

This includes tree data for `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` (core component),
`bq`, `gsutil`, and `kubectl`. Note that the
tree data is installed with the component. If the component is not installed
then neither is its CLI tree. An installed component does not require its CLI
tree to run. Only the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)`
CLI tree is required by `$ [gcloud alpha
interactive](https://cloud.google.com/sdk/gcloud/reference/alpha/interactive)`.
By default, CLI trees for other commands are JSON files generated on demand from
their `man`(1) or `man7.org` man pages. They are cached in
the `cli` subdirectory of the global config directory:

```
$(gcloud info --format="value(config.paths.global_config_dir)")/cli
```

**The gcloud CLI Tree**

: The `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI tree is used for
static TAB completion, the corpus for `$ [gcloud alpha](https://cloud.google.com/sdk/gcloud/reference/alpha) help-search`, and the
data source for `$ [gcloud
alpha interactive](https://cloud.google.com/sdk/gcloud/reference/alpha/interactive)` completions and help text generation.

**Other CLI Trees**

: `$ [gcloud alpha
interactive](https://cloud.google.com/sdk/gcloud/reference/alpha/interactive)` uses CLI tree data files for typeahead, command line
completion and active help. A few CLI trees are installed with their respective
Google Cloud CLI components: `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` (core component),
`bq`, `gsutil`, and `kubectl`.
The generated trees are a close approximation. You can construct your own,
especially for hierarchical CLIs like `git`(1) that are hard to
extract from man pages.

**CLI Tree Schema**

: TBD (`gcloud interactive` is still in ALPHA).

**NOTES**

: These variants are also available:

```
gcloud alpha topic cli-trees
```

```
gcloud beta topic cli-trees
```