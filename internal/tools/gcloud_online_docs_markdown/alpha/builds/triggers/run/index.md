# gcloud alpha builds triggers run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run)*

**NAME**

: **gcloud alpha builds triggers run - run a build trigger**

**SYNOPSIS**

: **`gcloud alpha builds triggers run` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#TRIGGER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#--region)`=`REGION`) [`[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#--substitutions)`=[`KEY`=`VALUE`,…]] [`[--branch](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#--branch)`=`BRANCH`     | `[--sha](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#--sha)`=`SHA`     | `[--tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#--tag)`=`TAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Run a build trigger.

**EXAMPLES**

: To run a build trigger, run:

```
gcloud alpha builds triggers run MY-TRIGGER --branch=master
```

**POSITIONAL ARGUMENTS**

: **Trigger resource - Build Trigger. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRIGGER`**:
ID of the trigger or fully qualified identifier for the trigger.
To set the `trigger` attribute:

- provide the argument `TRIGGER` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud location for the trigger.
To set the `region` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**FLAGS**

: **--substitutions**:
Parameters to be substituted in the build specification. For example:

```
gcloud alpha builds triggers run … --substitutions _FAVORITE_COLOR=blue,_NUM_CANDIES=10
```

This will result in a build where every occurrence of
`${_FAVORITE_COLOR}` in certain fields is replaced by "blue", and
similarly for `${_NUM_CANDIES}` and "10".
Substitutions can be applied to user-defined variables (starting with an
underscore) and to the following built-in variables: REPO_NAME, BRANCH_NAME,
TAG_NAME, REVISION_ID, COMMIT_SHA, SHORT_SHA.
For more details, see: [https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values)

**--branch**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds triggers run
```

```
gcloud beta builds triggers run
```