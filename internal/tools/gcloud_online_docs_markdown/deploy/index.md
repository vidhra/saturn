# gcloud deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy](https://cloud.google.com/sdk/gcloud/reference/deploy)*

**NAME**

: **gcloud deploy - create and manage Cloud Deploy resources**

**SYNOPSIS**

: **`gcloud deploy` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/deploy#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deploy#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manage Cloud Deploy resources.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[automation-runs](https://cloud.google.com/sdk/gcloud/reference/deploy/automation-runs)`**:
Manages AutomationRuns resources for Cloud Deploy.

**`[automations](https://cloud.google.com/sdk/gcloud/reference/deploy/automations)`**:
Manages Automations resources for Cloud Deploy.

**`[custom-target-types](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types)`**:
Create and manage Custom Target Type resources for Cloud Deploy.

**`[delivery-pipelines](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines)`**:
Create and manage Delivery Pipeline resources for Cloud Deploy.

**`[deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies)`**:
Create and manage Deploy Policy resources for Google Cloud Deploy.

**`[job-runs](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs)`**:
Manages job runs resources for Cloud Deploy.

**`[releases](https://cloud.google.com/sdk/gcloud/reference/deploy/releases)`**:
Create and manage Release resources for Cloud Deploy.

**`[rollouts](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts)`**:
Create and manage Rollout resources for Cloud Deploy.

**`[targets](https://cloud.google.com/sdk/gcloud/reference/deploy/targets)`**:
Create and manage Target resources for Cloud Deploy.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[apply](https://cloud.google.com/sdk/gcloud/reference/deploy/apply)`**:
Applies a yaml configuration containing Delivery Pipeline(s), Target(s), Custom
Target Type(s), Deploy Policy(ies), and Automation(s) declarative definitions.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/deploy/delete)`**:
Deletes Delivery Pipeline(s), Target(s), Custom Target Type(s), and
Automation(s) in a yaml configuration.

**`[get-config](https://cloud.google.com/sdk/gcloud/reference/deploy/get-config)`**:
Get the Cloud Deploy config for the provided region and project.

**NOTES**

: These variants are also available:

```
gcloud alpha deploy
```

```
gcloud beta deploy
```