# gcloud artifacts repositories set-cleanup-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies)*

**NAME**

: **gcloud artifacts repositories set-cleanup-policies - set or update cleanup policies for an Artifact Registry repository**

**SYNOPSIS**

: **`gcloud artifacts repositories set-cleanup-policies` (`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies#REPOSITORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies#--location)`=`LOCATION`) (`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies#--dry-run)` `[--policy](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies#--policy)`=`POLICY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set or update cleanup policies for an Artifact Registry repository.
This command can fail for the following reasons:

- The given repository does not exist.
- The active account does not have permission to update repositories.
- A valid cleanup policy format was not provided.
- The repository exceeds the maximum number of cleanup policies.

See [https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy](https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy)
for details of the cleanup policy file format and contents.

**EXAMPLES**

: To create a cleanup policy from a file with the name `policy.json` in
the repository `my-repo`, run:

```
gcloud artifacts repositories set-cleanup-policies my-repo --policy=policy.json
```

**POSITIONAL ARGUMENTS**

: **Repository resource - The parent Artifact Registry repository for the list of
cleanup policies. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPOSITORY`**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the repository. Overrides the default artifacts/location property
value for this command invocation. To configure the default location, use the
command: gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

**REQUIRED FLAGS**

: **--dry-run**

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

**API REFERENCE**

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)