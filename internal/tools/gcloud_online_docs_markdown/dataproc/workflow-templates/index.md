# gcloud dataproc workflow-templates  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates)*

**NAME**

: **gcloud dataproc workflow-templates - create and manage Dataproc workflow templates**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manage Dataproc workflow templates.

**EXAMPLES**

: To create a workflow template, run:

```
gcloud dataproc workflow-templates create my_template
```

To instantiate a workflow template, run:

```
gcloud dataproc workflow-templates instantiate my_template
```

To instantiate a workflow template from a file, run:

```
gcloud dataproc workflow-templates instantiate-from-file --file template.yaml
```

To delete a workflow template, run:

```
gcloud dataproc workflow-templates delete my_template
```

To view the details of a workflow template, run:

```
gcloud dataproc workflow-templates describe my_template
```

To see the list of all workflow templates, run:

```
gcloud dataproc workflow-templates list
```

To remove a job from a workflow template, run:

```
gcloud dataproc workflow-templates remove-job my_template --step-id id
```

To update managed cluster in a workflow template, run:

```
gcloud dataproc workflow-templates set-managed-cluster my_template --num-masters 5
```

To update cluster selector in a workflow template, run:

```
gcloud dataproc workflow-templates set-cluster-selector my_template --cluster-labels environment=prod
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[add-job](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job)`**:
Add Dataproc jobs to workflow template.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create)`**:
Create a workflow template.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/delete)`**:
Delete a workflow template.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/describe)`**:
Describe a workflow template.

**`[export](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export)`**:
Export a workflow template.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/get-iam-policy)`**:
Get IAM policy for a workflow template.

**`[import](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/import)`**:
Import a workflow template.

**`[instantiate](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate)`**:
Instantiate a workflow template.

**`[instantiate-from-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file)`**:
Instantiate a workflow template from a file.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/list)`**:
List workflow templates.

**`[remove-dag-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-dag-timeout)`**:
Remove DAG timeout from a workflow template.

**`[remove-job](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-job)`**:
Remove a job from workflow template.

**`[set-cluster-selector](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-cluster-selector)`**:
Set cluster selector for the workflow template.

**`[set-dag-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-dag-timeout)`**:
Set DAG timeout on a workflow template.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-iam-policy)`**:
Set IAM policy for a template.

**`[set-managed-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster)`**:
Set a managed cluster for the workflow template.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc workflow-templates
```

```
gcloud beta dataproc workflow-templates
```